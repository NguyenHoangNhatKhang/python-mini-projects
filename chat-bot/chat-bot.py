import openai
import os
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def save_log(user_input, bot_reply):
    with open("chat_log.txt", "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}]\nYou: {user_input}\nBot: {bot_reply}\n\n")

def chat_with_bot(messages, model="gpt-4o"):
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages
        )
        reply = response["choices"][0]["message"]["content"]
        return reply
    except Exception as e:
        return f"[ERROR]: {str(e)}"

def main():
    user_name = input("あなたのお名前は？: ")
    print(f"{user_name}さん、こんにちは！「end」と入力すると終了します。")

    messages = [
        {"role": "system", "content": "多言語のチャットボットとして対応してください"},
        {"role": "user", "content": f"私は {user_name}.{user_name}で呼んでください！"}
    ]

    while True:
        user_input = input("> ")
        if user_input.lower() == "end":
            print(f"Bye bye {user_name}")
            break

        messages.append({"role": "user", "content": user_input})
        reply = chat_with_bot(messages)
        print("Kelvin:", reply)
        messages.append({"role": "assistant", "content": reply})

        save_log(user_input, reply)

if __name__ == "__main__":
    main()