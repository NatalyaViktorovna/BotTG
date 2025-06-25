import os
from db import log_message_to_db
from telegram.ext import ApplicationBuilder, MessageHandler, filters
from openai_service import translate_text

async def handle_message(update, context):
    user_text = update.message.text
    user_id = update.effective_user.id
    username = update.effective_user.username or update.effective_user.first_name or "unknown"

    translated = translate_text(user_text)

    # Логирование в базу данных
    log_message_to_db(user_id=user_id, username=username, original=user_text, translated=translated)

    await update.message.reply_text(translated)

def setup_bot():
    app = ApplicationBuilder().token(os.environ["TELEGRAM_BOT_TOKEN"]).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    return app
