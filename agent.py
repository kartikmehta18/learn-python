# agent.py
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_llm(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Or "gpt-4"
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content

def main():
    print("Hello! I'm your LLM Agent. Ask me anything.")
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() in ['exit', 'quit']:
                print("Goodbye!")
                break
            answer = ask_llm(user_input)
            print(f"AI: {answer}")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    main()
