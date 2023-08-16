from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.storage import FSMContext

TOKEN = '6328095775:AAFVrneyP5Mbxz0Hd43tLDm503I6tG6JUa8'

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

class AnketStates(StatesGroup):
    wait_fio = State()
    wait_city = State()
    wait_time = State()


@dp.message_handler(text='Привет!')
async def hello_func(message: Message):
    await message.answer(text=f'Привет, {message.from_user.first_name}!')

@dp.message_handler(text='Пока!')
async def hello_func(message: Message):
    await message.answer(text='Пока!')

@dp.message_handler(commands='anket')
async def start_anket(message: Message):
    await message.answer(text='Введите ФИО')
    await AnketStates.wait_fio.set()

@dp.message_handler(state=AnketStates.wait_fio)
async def get_fio(message: Message, state: FSMContext):
    data = await state.get_data()
    data['fio'] = message.text
    await state.update_data(data)
    await message.answer(text='Введите город')
    await AnketStates.wait_city.set()

@dp.message_handler(state=AnketStates.wait_city)
async def get_city(message: Message, state: FSMContext):
    data = await state.get_data()
    data['city'] = message.text
    await state.update_data(data)
    await message.answer(text='Введите время')
    await AnketStates.wait_time.set()

@dp.message_handler(state=AnketStates.wait_time)
async def get_city(message: Message, state: FSMContext):
    data = await state.get_data()
    data['time'] = message.text
    print(data)
    await state.update_data(data)
    await message.answer(text=f'Успешно!\n{data}')
    await state.reset_state()

executor.start_polling(dispatcher=dp)
