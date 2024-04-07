import asyncio
import logging
from telegram.ext import Application, ApplicationBuilder, MessageHandler, CommandHandler, filters
from project_tools import get_config, joined

# Импорт всех необходимых библиотек

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


async def dialog(update, context):
    '''
    Функция обрабатывает текст введённый пользователем
    :param update:
    :param context:
    :return:
    '''

    await update.message.reply_text('я не знаю как на это отвечать')


async def start(update, context):
    '''
    Функция обрабатывает команду /start
    :param update:
    :param context:
    :return:
    '''

    user_name = update.effective_user.first_name
    user_id = update.effective_user.username
    joined(user_id)
    await update.message.reply_text(f'Приветствую тебя, {user_name}')


async def help(update, context):
    '''
    Функция обрабатывает команду /help
    :param update:
    :param context:
    :return:
    '''

    await update.message.reply_text('здесь будет инструкция к боту')


def main():
    '''
    Основная функция которая организует работу всех частей бота
    :return:
    '''

    application = Application.builder().token(get_config('config.json')['TOKEN']).build()
    text_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, dialog)
    start_handler = CommandHandler("start", start)
    help_handler = CommandHandler("help", help)
    application.add_handler(text_handler)
    application.add_handler(start_handler)
    application.add_handler(help_handler)
    application.run_polling()


if __name__ == '__main__':
    main()
