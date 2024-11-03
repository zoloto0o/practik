# main.py

from telegram.ext import Updater
from config import TELEGRAM_API_KEY
from bot_handlers import setup_dispatcher

def main() -> None:
    """Запускает бота."""
    updater = Updater(TELEGRAM_API_KEY)
    dispatcher = updater.dispatcher

    # Настраиваем обработчики
    setup_dispatcher(dispatcher)

    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
