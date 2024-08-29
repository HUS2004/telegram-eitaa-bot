from telethon import TelegramClient, events
import asyncio
import json
import os

# بارگذاری تنظیمات از فایل پیکربندی
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

api_id = config['api_id']
api_hash = config['api_hash']
phone_number = config['phone_number']
channel_username = 'AjaNews'

# تعریف مسیر برای فایل نشست و فایل لاگ
session_path = 'anon.session'
log_file = 'messages.txt'

# ایجاد نمونه جدید از TelegramClient
client = TelegramClient(session_path, api_id, api_hash)

async def main():
    # شروع به کار TelegramClient
    await client.start(phone_number)

    # تعریف هندلر رویداد برای پیام‌های جدید در کانال مشخص شده
    @client.on(events.NewMessage(chats=channel_username))
    async def handler(event):
        print(event.message.message)
        try:
            with open(log_file, "a", encoding="utf-8") as f:
                f.write(f"{event.message.message}\n")
        except IOError as e:
            print(f"Error writing to file {log_file}: {e}")

    print(f"Listening to new messages in {channel_username}...")

    # اجرای کلاینت تا زمان قطع اتصال
    await client.run_until_disconnected()

# اجرای تابع اصلی در حلقه رویداد asyncio
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
