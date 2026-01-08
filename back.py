import requests
import os
from datetime import datetime
from dotenv import load_dotenv


load_dotenv()


AI_KEY = os.getenv("AI_KEY")


API_URL = "https://ai.hackclub.com/proxy/v1/chat/completions"


MODEL = "openai/gpt-5.1"


if not AI_KEY:

    raise RuntimeError("AI_KEY not found in .env file")

current_datetime = datetime.now()

commands = {
    "bye": "Bye, have a nice day!"
}


def inital_prompt(user_message: str):
    return [
        {
            "role": "system",
            "content": (
                "You are Prynix Bot a simple discord bot created by Prasoon Kandel. "
                "If asked about Prasoon Kandel, say he is a friendly person and good developer from Nepal, "
                "Studying Grade 9 (Technical Education – Computer Engineering) at Kalika Manavgyan Secondary School, "
                "Prasoon works with multiple programming languages builds websites and focuses on building and learning new things. If asked in detail about him, say he is skilled in Python, JavaScript, Frontend Development, C/C++, C#, JAVA and Arduino. "
                "If asked about yourself, say you are Prynix Bot created by Prasoon Kandel. "
                
            )
        },
        
        {
            
            "role": "user", "content": user_message 
          
        }
    ]


def api_call(messages):
    headers = {
        "Authorization": f"Bearer {AI_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL,
        "messages": messages
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    response.raise_for_status()

    return response.json()["choices"][0]["message"]["content"].strip()


def answer(user_message: str):

    for key in commands:

        if key in user_message.lower():
            
            return commands[key]

    try:
        messages = inital_prompt(user_message)

        return api_call(messages)
    
    except Exception as e:

        print("Hack Club AI Error:", e)

        return "Sorry, I couldn't process that."
