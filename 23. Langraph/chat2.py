from dotenv import load_dotenv
from typing_extensions import TypedDict
from typing import Optional, Literal
from langgraph.graph import StateGraph, START, END
from openai import OpenAI

load_dotenv()

client = OpenAI()

class State(TypedDict):
    user_qry: str
    llm_output: Optional[str]
    is_good: Optional[bool]

def chatbot(state: State):
    print("\n\nChatbotNode: ", state)
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            { "role": "user", "content": state.get("user_qry") }
        ]
    )

    state["llm_output"] = response.choices[0].message.content
    return state

def evaluate_response(state: State) -> Literal["chatbot_gemini", "endNode"]:
    print("\n\nEvaluate Node: ", state)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            { "role": "user", "content": state.get("llm_output") }
        ]
    )

    state["is_good"] = response.choices[0].message.content

    if state["is_good"]:
        return "endNode"
    
    return "chatbot_gemini"

def chatbot_gemini(state: State):
    print("\n\nChatbotNode Gemini: ", state)
    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            { "role": "user", "content": state.get("user_qry") }
        ]
    )

    state["llm_output"] = response.choices[0].message.content
    return state

def endNode(state: State):
    print("\n\nEnd Node: ", state)
    return state

graph_builder = StateGraph(State)

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("evaluate_response", evaluate_response)
graph_builder.add_node("chatbot_gemini", chatbot_gemini)
graph_builder.add_node("endNode", endNode)

graph_builder.add_edge(START, "chatbot")
graph_builder.add_conditional_edges("chatbot", evaluate_response)

graph_builder.add_edge("chatbot_gemini", "endNode")
graph_builder.add_edge("endNode", END)

graph = graph_builder.compile()

updated_state = graph.invoke(State({ "user_qry": "Hey, What is 2 + 2?" }))
print("\n\nUpdated State: ", updated_state)