from aiogram import Bot, Dispatcher, executor, types
import pyqrcode

API_TOKEN = '5447380579:AAEKsA-ENVQqXcmEti-Daxs2cGHmsewYNWE'

# Initialize bot and dispatcher
bot = Bot(token = API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    await message.reply("Hello")

@dp.message_handler()
async def qr(message: types.Message):
    text = pyqrcode.create(message.text)
    text.png('code.png', scale=5)
    await bot.send_photo(chat_id=message.chat.id, photo=open('code.png', 'rb'))


executor.start_polling(dp)