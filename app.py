import os
from bot import setup_bot

if __name__ == '__main__':
    app = setup_bot()
    app.run_webhook(
        listen="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        webhook_url=os.environ["WEBHOOK_URL"],
    )