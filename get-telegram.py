
# Import necessary libraries
from telethon import TelegramClient, events
import asyncio
import os

# Replace with your own API ID and API Hash
api_id = 'api-id'  # API ID you obtained from my.telegram.org
api_hash = 'api_hash'  # API Hash you obtained from my.telegram.org
channel_username = 'AjaNews'  # Username of the public channel you want to scrape

# Define path for the session file and log file
session_path = 'anon.session'  # Replace with your desired path for session file
log_file = 'messages.txt'

# Create a new TelegramClient instance
client = TelegramClient(session_path, api_id, api_hash)

async def main():
    # Start the Telegram client
    await client.start()

    # Define an event handler for new messages in the specified channel
    @client.on(events.NewMessage(chats=channel_username))
    async def handler(event):
        # Print the message to the console
        print(event.message.message)
        
        # Append the message text to a file named messages.txt
        try:
            with open(log_file, "a", encoding="utf-8") as f:
                f.write(f"{event.message.message}\n")
        except IOError as e:
            print(f"Error writing to file {log_file}: {e}")

    # Inform the user that the client is listening for new messages
    print(f"Listening to new messages in {channel_username}...")

    # Run the client until manually stopped or disconnected
    await client.run_until_disconnected()

# Run the main function in an asyncio event loop
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
