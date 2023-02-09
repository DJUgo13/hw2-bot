from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor  # для запуска бота
import logging
import decouple
from decouple import config

# длЯ выведение расгиренной инфы
# токен бота 6222906080:AAEu074Vlq2EZ30FUmpzRRCqinVLtQNp4C8
# диспестчер это перехватчик смс
# types

TOKEN = config('TOKEN')

bot = Bot(TOKEN)
db = Dispatcher(bot=bot)


@db.message_handler(commands=['start', 'hello'])
async def start_handler(massege: types.Message):
    await bot.send_message(massege.from_user.id, f'еще раз напишешь {massege.from_user.first_name} уебу')
    await massege.answer('ты блять не понял')
    await massege.reply(massege.from_user.first_name)


@db.message_handler()
async def echo(massege: types.Message):
    await bot.send_message(massege.from_user.id, massege.text)
    await massege.answer('отъебись')

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(db, skip_updates=True)
