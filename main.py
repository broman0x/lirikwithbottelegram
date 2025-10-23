import os
import asyncio
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

load_dotenv()

LYRICS = [
    "Dia tanya aku punya plan (hei)",
    "Dia tahu kalau I'm the man (hei, hei)",
    "Kamu Tinker Bell, aku Peter Pan",
    "Tapi ini nyata, no, bukan cerpen",
    "Ini bukan cerpen, she's ten out of ten",
    "Pilih mau mana, dollar atau yen?",
    "Angkat koper, kita pergi Japan",
    "I'll give you the best that I can"
]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    message = await update.message.reply_text(LYRICS[0])
    for i in range(1, len(LYRICS)):
        if i < 2:
            delay = 2
        else:
            delay = 1.5
            
        await asyncio.sleep(delay)
        
        try:
            await message.edit_text(text=LYRICS[i])
        except Exception as e:
            print(f"Tidak bisa mengedit pesan: {e}")
            break 

    await update.message.reply_text("hidup blonde")

def main() -> None:
    """Jalankan bot."""
    TOKEN = os.getenv("TELEGRAM_TOKEN")
    
    if not TOKEN:
        print("Error: Token bot Telegram tidak ditemukan. Pastikan Anda sudah membuat file .env dan mengisinya.")
        return
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))

    print("Bot sedang berjalan")
    application.run_polling()

if __name__ == "__main__":
    main()

