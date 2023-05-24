import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Установка уровня логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Функция-обработчик для команды /start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я бот. Как дела?")

# Функция-обработчик для простых текстовых сообщений
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

# Функция, которая будет запускать бота
def main():
    # Инициализация бота и получение токена
    updater = Updater(token='YOUR_TELEGRAM_TOKEN', use_context=True)

    # Получение диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Регистрация обработчика команды /start
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    # Регистрация обработчика текстовых сообщений
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dispatcher.add_handler(echo_handler)

    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
