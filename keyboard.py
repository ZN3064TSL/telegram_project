from telegram import ReplyKeyboardMarkup

# Импорт необходимых библиотек

reply_keyboard = [['/start', '/help'], ['/apod', '/epic'], ['/mars_rover_photos']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
# Создание клавиатуры
