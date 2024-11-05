from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
api = ""
bot = Bot(token = api)
dp= Dispatcher(bot, storage= MemoryStorage())

# Обработчик для команд "/start"
@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.")  # Отвечаем на сообщение



# Обработчик для всех остальных сообщений
@dp.message_handler()
async def all_message(message: types.Message):
    await message.answer("Введите команду /start, чтобы начать общение.")

# Запускаем бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)