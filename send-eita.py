import requests
import os
import time


input_file = 'translated_messages.txt'
ita_api_url = os.getenv('ITA_API_URL', 'https://eitaayar.ir/api/api-hash/sendMessage')
chat_id = os.getenv('CHAT_ID', 'chat-id')
RED_CIRCLE = "🔴"
channel_link = os.getenv('CHANNEL_LINK', 'channel_link')

def correct_foori(text):
    if text.startswith("فوری"):
        text = text.replace("فوری", "فوری: ", 1)
    return text

def format_message(text):
    text = correct_foori(text)
    formatted_text = f"{RED_CIRCLE} {text}\n\n{channel_link}"
    return formatted_text

def send_message_to_channel(text):
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML"
    }
    try:
        response = requests.post(ita_api_url, json=payload)
        response.raise_for_status()
        print(f"Message sent successfully: {text}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send message: {e}")

def read_and_send_messages():
    if not os.path.exists(input_file):
        print(f"{input_file} not found.")
        return
    
    with open(input_file, "r", encoding="utf-8") as infile:
        lines = infile.readlines()
        for line in lines:
            if line.strip():
                formatted_message = format_message(line.strip())
                send_message_to_channel(formatted_message)

def monitor_file():
    print("Monitoring file for new messages...")
    sent_lines = set()

    while True:
        with open(input_file, "r", encoding="utf-8") as infile:
            lines = infile.readlines()
            for line in lines:
                if line.strip() and line.strip() not in sent_lines:
                    formatted_message = format_message(line.strip())
                    send_message_to_channel(formatted_message)
                    sent_lines.add(line.strip())
        time.sleep(10)

if __name__ == "__main__":
    monitor_file()
