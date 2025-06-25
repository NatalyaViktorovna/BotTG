import os
from telegram.ext import ApplicationBuilder, MessageHandler, filters
from openai_service import translate_text

async def handle_message(update, context):
    user_text = update.message.text
    translated = translate_text(user_text)
    await update.message.reply_text(translated)

def setup_bot():
    app = ApplicationBuilder().token(os.environ["TELEGRAM_BOT_TOKEN"]).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    return app