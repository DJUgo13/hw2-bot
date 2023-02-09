from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor  # для запуска бота
import logging
import decouple
from decouple import config

# длЯ выведение расгиренной инфы
# токен бота 6222906080:AAEu074Vlq2EZ30FUmpzRRCqinVLtQNp4C8
# диспестчер это перехватчик смс
# types

TOKEN=config('TOKEN')

bot = Bot(TOKEN)
db = Dispatcher(bot=bot)

if __name__=='__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(db, skip_updates=True)