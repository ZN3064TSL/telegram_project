import random
from api_tools import apod, epic, mars_rover_photo
from keyboard import markup
from project_tools import joined


class TelegramBot():
    '''
    Класс телеграм бота
    '''

    async def start(self, update, context):
        '''
        Функция обрабатывает команду /start
        :param update:
        :param context:
        :return:
        '''

        user_name = update.effective_user.first_name
        chat_id = update.message.chat_id
        joined('joined.sqlite', chat_id, user_name)
        await update.message.reply_text(f'Приветствую тебя, {user_name}',
                                        reply_markup=markup)

    async def help(self, update, context):
        '''
        Функция обрабатывает команду /help
        :param update:
        :param context:
        :return:
        '''

        text = '''Данный бот предназначен для получения фотографий с серверов nasa
Бот имеет следующие команды:
/start - Команда для запуска бота, после неё бот сможет отправлять
пользователю ежедневную картину космоса (Рассылка будет добавлена позже)
/help - Команда для вызова справочного меню о командах бота

/apod - Команда для получения ежедневной картинки космоса
/epic - Команда для получения последнего снимка Земли со спутника Кассегрена
/mars_rover_photos - Команда для получения случайного фото Марса с марсоходов.'''

        await update.message.reply_text(text)

    async def dialog(self, update, context):
        '''
        Функция обрабатывает текст введённый пользователем
        :param update:
        :param context:
        :return:
        '''

        await update.message.reply_text('Неизвестная команда')
        await update.message.reply_text('Для получения справки воспользуйтесь командой /help')

    async def send_apod(self, update, context):
        '''
        Функция делает запрос и присылает пользователю
        ежедневную картинку или видео с описанием
        :param update:
        :param context:
        :return:
        '''

        apod_info = await apod()
        apod_content_url = apod_info['content_url']

        sender_info = [update.message.chat_id, update.effective_user.first_name]

        if apod_info['apod_media_type'] == 'image':
            await context.bot.send_photo(chat_id=update.message.chat_id,
                                         photo=apod_content_url,
                                         caption=f"{apod_info['apod_title']}\n\n\n{apod_info['apod_info']}")
        elif apod_info['apod_media_type'] == 'video':
            await update.message.reply_text(f"{apod_info['apod_title']}\n\n\n{apod_info['apod_info']}\n\n"
                                            f"https://www.youtube.com/embed/w5uUcq__vMo?rel=0")

    async def send_epic(self, update, context):
        '''
        Функция делает запрос и присылает пользователю
        последний фотоснимок Земли сделанный телескопом Кассегрена
        :param update:
        :param context:
        :return:
        '''

        epic_info = await epic()
        epic_image_url = epic_info[-1]

        await context.bot.send_photo(chat_id=update.message.chat_id,
                                     photo=epic_image_url,
                                     caption=f'The newest image of the Earth.\n\n'
                                             f"Photo date: {'-'.join([i for i in epic_info[0].values()])}")

    async def send_mars_rover_photos(self, update, context):
        '''
        Функция делает запрос и присылает пользователю
        последние фотоснимки Марса с марсаходов
        :param update:
        :param context:
        :return:
        '''

        mars_rover_photo_info = await mars_rover_photo()
        photo = random.choice(mars_rover_photo_info['photos'])
        date = mars_rover_photo_info['date']

        await context.bot.send_photo(chat_id=update.message.chat_id,
                                     photo=photo,
                                     caption=(f'The latest images of Mars taken by the rovers.\n\n'
                                              f'Photo date: {date}'))
