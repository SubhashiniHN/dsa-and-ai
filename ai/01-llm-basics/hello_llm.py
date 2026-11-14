"""First LLM call. Run: python hello_llm.py "Explain tokens in one paragraph" """
import os
import sys

from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))


def main():
    prompt = sys.argv[1] if len(sys.argv) > 1 else "Explain what a token is in two sentences."
    import anthropic

    client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY
    msg = client.messages.create(
        model="claude-sonnet-4-5",  # change to any model your key can use
        max_tokens=300,
        messages=[{"role": "user", "content": prompt}],
    )
    print(msg.content[0].text)
    print("\n--- usage ---")
    print("input tokens :", msg.usage.input_tokens)
    print("output tokens:", msg.usage.output_tokens)


if __name__ == "__main__":
    main()
