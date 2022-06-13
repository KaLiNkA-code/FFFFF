from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage
""" async: Если в исполнении какой либо функции получился участок времени, когда ничего не используется,
он позволяет в эти промежутки исполнять что то другое"""
storage = MemoryStorage()
# Получение токена
token = os.getenv("TOKEN")

bot = Bot('5569185301:AAG-EBE1FvR1eFRq8Mlx2N-k83hYjQANo7Q')
dp = Dispatcher(bot, storage=storage)  # Инициализируем диспачер
