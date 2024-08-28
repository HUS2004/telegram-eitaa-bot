import requests
import time
import os

# تنظیمات
input_file = 'translated_messages.txt'
ita_api_url = "https://eitaayar.ir/api/api-hash/sendMessage"  # آدرس API با توکن ربات شما
chat_id = "chat-id"  # نام کاربری کانال ایتا
RED_CIRCLE = "🔴"  # استفاده مستقیم از ایموجی دایره قرمز
channel_link = "channel_link"  # لینک کانال ایتا

def correct_foori(text):
    # بررسی وجود کلمه "فوری" در ابتدای متن و افزودن ": " در صورت لزوم
    if text.startswith("فوری"):
        text = text.replace("فوری", "فوری: ", 1)  # فقط اولین "فوری" را تغییر دهید
    return text

def format_message(text):
    # تصحیح "فوری" در ابتدای پیام
    text = correct_foori(text)
    # افزودن دایره قرمز و لینک کانال
    formatted_text = f"{RED_CIRCLE} {text}\n\n{channel_link}"
    return formatted_text

def send_message_to_channel(text):
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML"  # برای فرمت کردن متن پیام (اختیاری)
    }
    try:
        response = requests.post(ita_api_url, json=payload)  # استفاده از json به جای data
        response.raise_for_status()  # بررسی وضعیت پاسخ و بالا بردن استثناء در صورت خطا
        print(f"Message sent successfully: {text}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send message: {e}")

def read_and_send_messages():
    # بررسی وجود فایل
    if not os.path.exists(input_file):
        print(f"{input_file} not found.")
        return
    
    # باز کردن فایل برای خواندن
    with open(input_file, "r", encoding="utf-8") as infile:
        lines = infile.readlines()
        for line in lines:
            if line.strip():
                formatted_message = format_message(line.strip())
                send_message_to_channel(formatted_message)

# بررسی تغییرات فایل و ارسال پیام‌ها به صورت پیوسته
def monitor_file():
    print("Monitoring file for new messages...")
    sent_lines = set()  # برای ذخیره‌سازی خطوطی که ارسال شده‌اند

    while True:
        # خواندن پیام‌های جدید
        with open(input_file, "r", encoding="utf-8") as infile:
            lines = infile.readlines()
            for line in lines:
                if line.strip() and line.strip() not in sent_lines:
                    formatted_message = format_message(line.strip())
                    send_message_to_channel(formatted_message)
                    sent_lines.add(line.strip())
        time.sleep(10)  # بررسی فایل هر 10 ثانیه

if __name__ == "__main__":
    monitor_file()
