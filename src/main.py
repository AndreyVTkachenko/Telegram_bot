from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor

TOKEN = '6328095775:AAFVrneyP5Mbxz0Hd43tLDm503I6tG6JUa8'

bot = Bot(token=TOKEN)

dp = Dispatcher(bot)

@dp.message_handler(text='Привет!')
async def hello_func(message: Message):
    await message.answer(text=f'Привет, {message.from_user.first_name}!')

@dp.message_handler(text='Пока!')
async def hello_func(message: Message):
    await message.answer(text='Пока!')

executor.start_polling(dispatcher=dp)
