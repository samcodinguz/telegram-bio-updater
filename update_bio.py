from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest
from datetime import datetime, timedelta
import asyncio

# --- Telegram API ma'lumotlari ---
api_id = 22711238
api_hash = "7b9846aeb45be9ac95e7ce0ba21e947e"
phone = "998904781877"

# --- Telegram sessiyasi ---
client = TelegramClient("bio_session", api_id, api_hash)

# Progress bar belgilarini tayyorlaymiz
progress_states = ["[■□□□□]%", "[■■□□□]%", "[■■■□□]%", "[■■■■□]%", "[■■■■■]%"]
progress_bio = ["🚀 {t} — Push & Commit", "🌐 {t} | Deploying...", "🌌 {t} | Debugging under stars", "⚡ {t} — Algorithm mode", "🎯 {t} | Goals: 100% code"] 

async def update_bio_forever():
    async with client:
        counter = 0
        while True:
            tz_offset = timedelta(hours=5)
            now = datetime.utcnow() + tz_offset
            time_str = now.strftime("%H:%M:%S")
            
            # Progress bar har soniyada o'zgaradi
            progress = progress_states[counter % len(progress_states)]
            bio_template = progress_bio[counter % len(progress_bio)]
            text = f"{bio_template.format(t=time_str)} {progress}"
            
            await client(UpdateProfileRequest(about=text))
            print(f"Bio updated: {text}")
            
            counter += 1
            await asyncio.sleep(10)  # har 10 soniyada yangilansin

if __name__ == "__main__":
    asyncio.run(update_bio_forever())
