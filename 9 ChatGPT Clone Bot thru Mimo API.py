import os
import requests


def send_message(user_message, thread_id):
    body = {
        "message": user_message
    }
    if thread_id:
        body["threadId"] = thread_id
    response = requests.post(url, headers=headers, json=body)
    return response.json()


api_key = os.getenv("MIMO_OPENAI_API_KEY")
url = "https://ai.mimo.org/v1/openai/message"
headers = {
    "api-key": api_key
}

current_thread_id = None
threads = []

print("⚠️  This bot only works in the Mimo App's dedicated Python playground environment.")
print("⚠️  This is because Mimo holds the API keys for the ChatGPT bot. You're free to copy this code and paste it there!\n")
print("Welcome! Type your message and press Enter to send.")
print("Type 'exit' to end the program")
print("Type 'new' to switch conversation thread.")
print("Starting a new thread for you.\n")

while True:
    user_message = input("You: ")
    if user_message == "exit":
        break
    elif user_message == "new":
        current_thread_id = None
        print("New thread\n")
        continue

    response_data = send_message(user_message, current_thread_id)
    latest_message = response_data.get("response")
    current_thread_id = response_data.get("threadId")
    print(f"GPT: {latest_message}")
    threads.append(current_thread_id)