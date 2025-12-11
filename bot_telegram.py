import os
from telegram.ext import ApplicationBuilder, MessageHandler, filters
from pinterest_ai import generate_pinterest_post

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

async def process_message(update, context):
    text = update.message.text.strip()
    result = generate_pinterest_post(text)
    await update.message.reply_text(result)

def run_telegram_bot():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, process_message))
    app.run_polling()