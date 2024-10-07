from aiogram.utils import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = "7793991805:AAFKnYYeJDajkfpEsQqZPtGhexX93-_aNCQ"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
executor.start_polling(dp, skip_updates=True)
