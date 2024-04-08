import asyncio
import logging
from telegram.ext import Application, ApplicationBuilder, MessageHandler, CommandHandler, filters
from project_tools import get_config, joined, get_joined_users_id
from api_tools import apod

# Импорт всех необходимых библиотек

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


async def start(update, context):
    '''
    Функция обрабатывает команду /start
    :param update:
    :param context:
    :return:
    '''

    user_name = update.effective_user.first_name
    chat_id = update.message.chat_id
    joined(chat_id)
    await update.message.reply_text(f'Приветствую тебя, {user_name}')


async def help(update, context):
    '''
    Функция обрабатывает команду /help
    :param update:
    :param context:
    :return:
    '''

    await update.message.reply_text('здесь будет инструкция к боту')


async def dialog(update, context):
    '''
    Функция обрабатывает текст введённый пользователем
    :param update:
    :param context:
    :return:
    '''

    await update.message.reply_text('я не знаю как на это отвечать')


async def send_apod(update, context):
    '''
    Функция делает запрос и присылает пользователю
    ежедневную картинку с описанием (будет добавлено позже)
    :param update:
    :param context:
    :return:
    '''

    apod_info = apod()
    apod_image_url = apod_info['image_url']

    await context.bot.send_photo(chat_id=update.message.chat_id,
                                 photo=apod_image_url,
                                 caption=apod_info['apod_title'])


def main():
    '''
    Основная функция которая организует работу всех частей бота
    :return:
    '''

    application = Application.builder().token(get_config('config.json')['TOKEN']).build()
    text_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, dialog)
    start_handler = CommandHandler("start", start)
    help_handler = CommandHandler("help", help)
    apod_handler = CommandHandler('apod', send_apod)
    application.add_handler(text_handler)
    application.add_handler(start_handler)
    application.add_handler(help_handler)
    application.add_handler(apod_handler)
    application.run_polling()


if __name__ == '__main__':
    main()
