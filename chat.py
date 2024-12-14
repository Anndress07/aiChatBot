from dotenv import load_dotenv
import os
from openai import OpenAI



""" API Init"""
load_dotenv()
client = OpenAI(
    # api_key=os.environ.get("oai_api"),  # This is the default and can be omitted
    api_key=os.getenv('oai_api'),
)


# print(chatBot_Personality1)

def chatWithGPT(personality, prompt):
    if personality == "pers1":
        with open("chatBot_Personality1.txt", "r") as file:
            personality = file.read()


    messages = [
        {"role": "system", "content": personality},  # Adding personality as a system message
        {"role": "user", "content": prompt}  # The user's prompt follows
    ]
    chat_completion = client.chat.completions.create(
        messages=messages,
        model="gpt-3.5-turbo",
    )
    return chat_completion

def userInput():
    prompt = input("Send a message to the GPT!: ")
    return prompt

if __name__ == "__main__":
    message = userInput()
    while message != ".exit":
        response = chatWithGPT("pers1", message)
        print(f"Response: {response.choices[0].message.content}")
        message = userInput()

# print(chat_completion)
# print(chat_completion.choices[0].message.content)


