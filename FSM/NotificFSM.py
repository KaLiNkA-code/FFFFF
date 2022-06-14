from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from create_bot import dp
from aiogram import Dispatcher
#  from  import cursor
import asyncio


class FSMsAdmin(StatesGroup):
    photo = State()
    text = State()
    date = State()
    time = State()


# @dp.message_handler(commands='Загрузить', state=None)
async def cms_start(message: types.Message, state: FSMContext):
    await FSMsAdmin.photo.set()
    await message.reply('Загрузите фото')


# @dp.message_handler(commands='Загрузить', state=None)
async def cms_start1(message: types.Message, state: FSMContext):
    #  async with state.proxy()
    await FSMsAdmin.next()
    await message.reply('Напишите текст')


# @dp.message_handler(state=FSMAdmin.name)
async def cms_start2(message: types.Message, state: FSMContext):
    # message.text Сохраняем в бд (Имя)
    await FSMsAdmin.next()
    await message.reply("Поставьте число в формате 31 12  (день\пробел\месяц)")


# @dp.message_handler(state=FSMAdmin.mail)
async def cms_start3(message: types.Message, state: FSMContext):
    # message.text Сохраняем в бд (Почта)
    await FSMsAdmin.next()
    await message.reply("Поставьте время в формате 12:30 (час\двоеточие\минуты)")


# @dp.message_handler(state=FSMAdmin.how)
async def cms_start4(message: types.Message, state: FSMContext):
    # message.text Сохраняем в бд (Как узнали)
    await state.finish()
    await message.reply("Спасибо, вы зарегистрированы")


# def register_user(tg_id, name, email, phone, from_where):
#   cursor.execute("INSERT INTO USERS(user_id_tg, name, email, phone, where_know) VALUES('{0}', '{1}', '{2}', '{3}', {4});".format(tg_id, name, email, phone, from_where))
#   return 0


def register_message_handler(dp: Dispatcher):
    dp.register_message_handler(cms_start, text='Регистрация', state=None)
    dp.register_message_handler(cms_start2, state=FSMsAdmin.photo)
    dp.register_message_handler(cms_start3, state=FSMsAdmin.date)
    dp.register_message_handler(cms_start4, state=FSMsAdmin.time)
