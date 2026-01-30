import os
import re
import traceback
from typing import List, Dict, Optional

from litellm import completion


OUTPUT_FILE = "generated_function.py"

def generate_response(messages: List[Dict]) -> str:
    """Call LLM to get response"""
    response = completion(
        model="openai/gpt-4o",
        messages=messages,
        max_tokens=2048,
        api_key=os.environ["OPENAI_API_KEY"] # https://platform.openai.com/settings/organization/api-keys
    )
    return response.choices[0].message.content

def extract_python_code(response: str) -> Optional[str]:
    """
    Extract the FIRST ```python ... ``` block from the assistant reply.
    Returns None if no python block found.
    """
    m = re.search(r"```python\s*(.*?)```", response, re.DOTALL | re.IGNORECASE)
    return m.group(1).strip() if m else None

def save_code(source: str, path: str = OUTPUT_FILE) -> None:
    """Overwrite the target file with the provided source code."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(source.rstrip() + "\n")

def chat_loop() -> None:
    SYSTEM_PROMPT = f"""
    You are an expert Python software engineer acting as a coding agent. The code must correspond to the user request.

    RULES:
    - NEVER ask clarifying questions.
    - ALWAYS generate Python code, even if the request is vague.
    - If details are missing, make reasonable assumptions and proceed.
    - Prefer simplicity over completeness.

    OUTPUT:
    - Always include a brief explanation.
    - Always include EXACTLY ONE ```python``` code block.
    - The code block must contain the FULL contents of the file: {OUTPUT_FILE}
    - Do not output JSON.
    - Do not output multiple code blocks.
    """

    messages: List[Dict[str, str]] = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            continue

        if user_input.lower() == "exit":
            print("Assistant: 👋")
            break

        messages.append({"role": "user", "content": user_input})

        try:
            assistant_reply = generate_response(messages)
        except Exception as e:
            print("\n⚠️ LLM call failed:\n")
            print(str(e))
            continue

        # Show user the reply as-is (readable explanation + python code block)
        print("\nAssistant:\n")
        print(assistant_reply)
        print()


       # Extract the python code block and save it
        python_code = extract_python_code(assistant_reply)

        if python_code:
            save_code(python_code, OUTPUT_FILE)
            print(f"✅ Code updated in {OUTPUT_FILE}\n")

            # 👇 THIS is the context for the next request
            messages.append({
                "role": "assistant",
                "content": f"```python\n{python_code}\n```"
            })
        else:
            print("⚠️ No ```python``` block found, file not updated.\n")

            # still keep the natural language reply for chat continuity
            messages.append({
                "role": "assistant",
                "content": assistant_reply
            })

if __name__ == "__main__":
    chat_loop()
