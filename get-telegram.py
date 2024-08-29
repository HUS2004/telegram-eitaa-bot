import os
from telethon import TelegramClient, events
import asyncio

# دریافت مقادیر از متغیرهای محیطی
api_id = os.getenv('TELEGRAM_API_ID')  # API ID شما
api_hash = os.getenv('TELEGRAM_API_HASH')  # API Hash شما
channel_username = os.getenv('TELEGRAM_CHANNEL_USERNAME')  # نام کاربری کانال

if not api_id or not api_hash:
    raise ValueError("API ID and API Hash must be set as environment variables.")

# تعریف مسیر برای فایل نشست
session_path = 'anon.session'  # مسیر فایل نشست

# ایجاد نمونه جدید TelegramClient
client = TelegramClient(session_path, api_id, api_hash)

async def main():
    # شروع Telegram client
    await client.start()

    # تعریف یک هندلر برای پیام‌های جدید
    @client.on(events.NewMessage(chats=channel_username))
    async def handler(event):
        print(event.message.message)
        try:
            with open('messages.txt', "a", encoding="utf-8") as f:
                f.write(f"{event.message.message}\n")
        except IOError as e:
            print(f"Error writing to file: {e}")

    print(f"Listening to new messages in {channel_username}...")
    await client.run_until_disconnected()

# اجرای تابع اصلی
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
