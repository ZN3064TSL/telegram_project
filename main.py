import logging
import random
from telegram.ext import Application, MessageHandler, CommandHandler, filters
from project_tools import get_config, joined
from api_tools import apod, epic, mars_rover_photos
from keyboard import markup
from bot import TelegramBot


# Импорт всех необходимых библиотек

def main():
    '''
    Основная функция которая организует работу всех частей бота
    :return:
    '''

    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
    )

    logger = logging.getLogger(__name__)

    bot = TelegramBot()
    application = Application.builder().token(get_config('config.json')['TOKEN']).build()

    text_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, bot.dialog)
    start_handler = CommandHandler("start", bot.start)
    help_handler = CommandHandler("help", bot.help)
    apod_handler = CommandHandler('apod', bot.send_apod)
    epic_handler = CommandHandler('epic', bot.send_epic)

    mars_rover_photos_handler = CommandHandler('mars_rover_photos', bot.send_mars_rover_photos)
    application.add_handler(text_handler)
    application.add_handler(start_handler)
    application.add_handler(help_handler)
    application.add_handler(apod_handler)
    application.add_handler(epic_handler)
    application.add_handler(mars_rover_photos_handler)

    application.run_polling()


if __name__ == '__main__':
    main()
