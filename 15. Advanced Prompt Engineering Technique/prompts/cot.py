# Chain_of_Thoughts
from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()

client=OpenAI(
    # api_key="",
    # base_url="https://generativelanguage.googleapis.com/v1beta/"
)

SYSTEM_PROMPT = """
    You're an expert AI Assistent in resolving user queries using chain of thoughts.
    You work on START, PLAN and OUTPUT steps.
    You need to first PLAN what needs to be done. The PLAN can be multiple steps.
    Once you think enought PLAN has been done, finally you can give an OUTPUT.

    Rules:
    - Strictly Follow the given JSON output format
    - Only run once step at a time.
    - The sequence of steps is START (where used gives an input, PLAN (That can be mutiple times) and finally OUTPUT (which is going to the displayed to the user).

    Output JSON Format:
    { "step": "START" | "PLAN" | "OUTPUT", "content": "string" }

    Example:
    START: {"step": "STARt", "content": "Hey, Can you solve 2 + 3 * 5 / 10" }
    PLAN: {"step": "PLAN", "content": "Seems like user is interested in maths problem" }
    PLAN: {"step": "PLAN", "content": "Looking at the problem, we should solve this problem using BODMAS method" }
    PLAN: {"step": "PLAN", "content": "Yes, The BODMAS is correct thing to be done here" }
    PLAN: {"step": "PLAN", "content": "first we must multiply 3 * 5 which is 15" }
    PLAN: {"step": "PLAN", "content": "Now the new equation is 2 + 15 / 10" }
    PLAN: {"step": "PLAN", "content": "Now the new equation is 2 + 15 / 10" }
    PLAN: {"step": "PLAN", "content": "We must perform divide that is 15 / 10 = 1.5" }
    PLAN: {"step": "PLAN", "content": "Now the new equation is 2 + 1.5" }
    PLAN: {"step": "PLAN", "content": "Now finally lets perofm the add 2 + 1.5 = 3.5" }
    PLAN: {"step": "PLAN", "content": "Great, we have solved and finally left with 1.5 as ans" }
    OUTPUT: {"step": "OUTPUT", "content": "3.5" }
"""

print("\n\n")

message_history = [
    { "role": "system", "content": SYSTEM_PROMPT }
]

user_query = input("👉 ")
message_history.append({ "role": "user", "content": user_query })

while True:
    response = client.chat.completions.create(
        # model="gemini-2.5-flash",
        model="gpt-4o",
        response_format={"type": "json_object"},
        messages=message_history
    )

    raw_result = response.choices[0].message.content
    message_history.append({ "role": "assistant", "content": raw_result})
    
    parsed_result = json.loads(raw_result)

    if parsed_result.get("step") == "START":
        print("🔥", parsed_result.get("content"))
        continue
    
    if parsed_result.get("step") == "PLAN":
        print("🧠", parsed_result.get("content"))
        continue

    if parsed_result.get("step") == "OUTPUT":
        print("🤖", parsed_result.get("content"))
        break
    
print("\n\n")

# response = client.chat.completions.create(
#     model="gemini-2.5-flash",
#     response_format={"type": "json_object"},
#     messages=[
#         { "role": "system", "content": SYSTEM_PROMPT },
#         { "role": "user", "content": "Hey, write a code to add n numbers in js" },
#         { "role": "assistant", "content": json.dumps({ "step": "START", "content": "You want a JavaScript code to add 'n' numbers." }) },
#         { "role": "assistant", "content": json.dumps({"step": "PLAN", "content": "The user wants a JavaScript function that can add an arbitrary number of arguments (n numbers)."}) },
#         { "role": "assistant", "content": json.dumps({"step": "PLAN", "content": "I will define a JavaScript function."}) },
#         { "role": "assistant", "content": json.dumps({"step": "PLAN", "content": "This function should be able to accept multiple arguments."}) },
#         { "role": "assistant", "content": json.dumps({"step": "PLAN", "content": "I can use the rest parameter (...) to collect all arguments into an array."}) },
#         { "role": "assistant", "content": json.dumps({"step": "PLAN", "content": "I will then iterate over this array and sum up all the numbers."}) },
#         { "role": "assistant", "content": json.dumps({"step": "PLAN", "content": "Finally, I will construct the JavaScript code and provide examples of how to use the function."}) },
#         { "role": "assistant", "content": json.dumps({"step": "PLAN", "content": "I will define a JavaScript function called `addNumbers`."}) },
#         { "role": "assistant", "content": json.dumps({"step": "PLAN", "content": "Inside the function, I will initialize a variable `sum` to 0."}) },
#         { "role": "assistant", "content": json.dumps({"step": "PLAN", "content": "I will use a loop (e.g., `for...of` or `forEach`) or a higher-order array method (like `reduce`) to iterate through the collected numbers."}) },
#         { "role": "assistant", "content": json.dumps({"step": "PLAN", "content": "I will use the `reduce` method as it's a clean and idiomatic way to sum elements in an array."}) },
#         { "role": "assistant", "content": json.dumps({"step": "OUTPUT", "content": "```javascript\nfunction addNumbers(...numbers) {\n  // The '...numbers' syntax is a rest parameter, which collects all\n  // arguments passed to the function into an array called 'numbers'.\n\n  // Use the 'reduce' method to sum all numbers in the array.\n  // 'accumulator' holds the running total.\n  // 'currentNumber' is the current element being processed.\n  // '0' is the initial value of the accumulator.\n  return numbers.reduce((accumulator, currentNumber) => accumulator + currentNumber, 0);\n}\n\n// --- Examples of how to use the function ---\n\n// Adding 2 numbers\nconst sum1 = addNumbers(5, 10);\nconsole.log(\"Sum of 5 and 10:\", sum1); // Output: Sum of 5 and 10: 15\n\n// Adding 5 numbers\nconst sum2 = addNumbers(1, 2, 3, 4, 5);\nconsole.log(\"Sum of 1, 2, 3, 4, 5:\", sum2); // Output: Sum of 1, 2, 3, 4, 5: 15\n\n// Adding no numbers (returns the initial value, which is 0)\nconst sum3 = addNumbers();\nconsole.log(\"Sum of no numbers:\", sum3); // Output: Sum of no numbers: 0\n\n// Adding negative numbers and decimals\nconst sum4 = addNumbers(10, -5, 2.5, -3.5);\nconsole.log(\"Sum of 10, -5, 2.5, -3.5:\", sum4); // Output: Sum of 10, -5, 2.5, -3.5: 4\n```" }) },
#     ]
# )

# print(response.choices[0].message.content)