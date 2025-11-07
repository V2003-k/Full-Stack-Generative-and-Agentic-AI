from dotenv import load_dotenv
from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain.chat_models import init_chat_model

load_dotenv()

llm = init_chat_model(
    model="gpt-4.1-mini",
    model_provider="openai"
)

class State(TypedDict):
    messages: Annotated[list, add_messages]

def chatbot(state: State):
    response = llm.invoke(state.get("messages"))
    return { "messages": [response] }

def sampleNode(state: State):
    print("\n\n\nInside sample node", state)
    return { "messages": ["Sample Message Appended"] }

graph_builder = StateGraph(State)
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("sampleNode", sampleNode)

graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", "sampleNode")
graph_builder.add_edge("sampleNode", END)

graph = graph_builder.compile()

updated_state = graph.invoke(State({ "messages": ["What is my name?`"] }))
print("\n\n\nupdated_state", updated_state)

# START -> chatbot -> sampleNode

# state { messages: ["Hey, There"] }
# node runs: chatbot(state: ["Hey, There"]) -> ["Hi, This is a message from chatbot Node"]
# state: { "messages": ["Hey, There", "Hi, This is a message from chatbot Node"] }