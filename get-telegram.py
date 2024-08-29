from telethon import TelegramClient, events
import asyncio
import os

# خواندن متغیرهای محیطی
api_id = os.getenv('TELEGRAM_API_ID', 'default_api_id')
api_hash = os.getenv('TELEGRAM_API_HASH', 'default_api_hash')
channel_username = os.getenv('TELEGRAM_CHANNEL_USERNAME', 'AjaNews')

session_path = 'anon.session'
log_file = 'messages.txt'

client = TelegramClient(session_path, api_id, api_hash)

async def main():
    await client.start()

    @client.on(events.NewMessage(chats=channel_username))
    async def handler(event):
        print(event.message.message)
        try:
            with open(log_file, "a", encoding="utf-8") as f:
                f.write(f"{event.message.message}\n")
        except IOError as e:
            print(f"Error writing to file {log_file}: {e}")

    print(f"Listening to new messages in {channel_username}...")
    await client.run_until_disconnected()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
