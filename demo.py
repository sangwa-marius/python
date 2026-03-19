import json
from datetime import datetime

FILE_NAME = "data.jsonl"

def save_message(name, text):
    message = {
        "sender": name,
        "text": text,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    with open(FILE_NAME, "a") as f:
        f.write(json.dumps(message) + "\n")


def display_messages():
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                try:
                    msg = json.loads(line)
                    sender = msg.get("sender", "Unknown")
                    text = msg.get("text", "")
                    time = msg.get("time", "No time")

                    print(f"{sender} ({time}): {text}")
                except json.JSONDecodeError:
                    print("Skipping invalid line...")
    except FileNotFoundError:
        print("No messages yet.")


name = input("Enter your name: ")
text = input("Enter your message: ")

save_message(name, text)

print("\n--- All Messages ---")
display_messages()