from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest
from datetime import datetime
import asyncio

# --- Telegram API ma'lumotlari ---
api_id = 22711238     # my.telegram.org saytidan olganingizni yozing
api_hash = "7b9846aeb45be9ac95e7ce0ba21e947e"  # shu yerga haqiqiy API_HASH yozing
phone = "998904781877"  # sizning raqamingiz

# --- Telegram sessiyasi ---
client = TelegramClient("bio_session", api_id, api_hash)

async def update_bio_forever():
    async with client:
        while True:
            now = datetime.now().strftime("%H:%M")
            text = f"⏰ Time clock: {now}"
            await client(UpdateProfileRequest(about=text))
            print(f"Bio updated: {text}")
            await asyncio.sleep(60)  # har 60 soniyada yangilansin

if __name__ == "__main__":
    asyncio.run(update_bio_forever())
