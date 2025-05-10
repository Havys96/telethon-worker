# telethon_worker.py
import asyncio
from telethon import TelegramClient, events
import os
from dotenv import load_dotenv

load_dotenv()

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

client = TelegramClient("user_forward_session", api_id, api_hash, system_version="4.16.30-vxCUSTOM")

source_channels = [
    -1001386345244, -1001363666182, -1002390221197,
    -1001584728369, -1002446954490, -1001506613982,
    -1001496860175, -1001938236225, -1001685688905, -1002682741959
]
destination_channel = -1002451608794

@client.on(events.NewMessage(chats=source_channels))
async def handler(event):
    await client.forward_messages(destination_channel, event.message)

async def main():
    await client.start()
    print("🟢 Telethon 포워딩 전용 봇 작동 시작")
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
