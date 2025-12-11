from flask import Flask
import threading
import os
from bot_telegram import run_telegram_bot

app = Flask(__name__)

@app.route("/")
def healthcheck():
    return {"status": "ok"}

def run_flask():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    # Flask — в отдельном потоке, только для healthcheck
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()

    # Telegram-бот — в главном потоке (как любит python-telegram-bot 20.x)
    run_telegram_bot()
