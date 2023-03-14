import os
import sys
import logging
import openai

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def chatgpt(input: str) -> str:
    logging.info(f"ChatGPT input: {input}")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": input},
        ],
    )
    text = response["choices"][0]["message"]["content"]
    logging.info(f">> {text}")
    return text


if __name__ == "__main__":
    if len(sys.argv) > 1:
        input = " ".join(sys.argv[1:])
        print("Input:", input)
        chatgpt(input)
    else:
        print("Specifiy an input for ChatGPT")
