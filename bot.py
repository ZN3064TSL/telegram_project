import random
from api_tools import apod, epic, mars_rover_photos
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
        joined(chat_id)
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
/mars_rover_photos - Команда для получения 10(будет добавлено позже) случайных
фотографий Марса с марсоходов.'''

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
        ежедневную картинку с описанием
        :param update:
        :param context:
        :return:
        '''

        apod_info = await apod()
        apod_image_url = apod_info['image_url']

        await context.bot.send_photo(chat_id=update.message.chat_id,
                                     photo=apod_image_url,
                                     caption=f'{apod_info['apod_title']}\n\n\n{apod_info['apod_info']}')

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
                                     caption=f'Новейшее изображение Земли.\n\n'
                                             f'Дата снимка: {'-'.join([i for i in epic_info[0].values()])}')

    async def send_mars_rover_photos(self, update, context):
        '''
        Функция делает запрос и присылает пользователю
        последние фотоснимки Марса с марсаходов
        :param update:
        :param context:
        :return:
        '''

        mars_rover_photos_info = await mars_rover_photos()
        photos = random.choices(mars_rover_photos_info['photos'], k=10)
        date = mars_rover_photos_info['date']

        await context.bot.send_photo(chat_id=update.message.chat_id,
                                     photo=photos[0],
                                     caption=(f'Новейшие изображения Марса, сделанные марсоходами.\n\n'
                                              f'Дата снимка: {date}'))
