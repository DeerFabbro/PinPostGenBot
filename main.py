from flask import Flask
import threading
from bot_telegram import run_telegram_bot

app = Flask(__name__)

@app.route("/")
def healthcheck():
    return {"status": "ok"}

def start_bot():
    run_telegram_bot()

if __name__ == "__main__":
    # Запуск Telegram-бота в отдельном потоке
    bot_thread = threading.Thread(target=start_bot, daemon=True)
    bot_thread.start()

    # Запуск веб-сервера (Render слушает переменную PORT)
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)