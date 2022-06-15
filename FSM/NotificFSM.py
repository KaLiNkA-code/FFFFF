from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from create_bot import dp
from aiogram import Dispatcher
#  from  import cursor
import asyncio
from TempUserBD import notifications
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from TempUserBD import notifications, notif_count


class FSMsAdmin(StatesGroup):
    photo = State()
    text = State()
    date = State()
    time = State()


# @dp.message_handler(commands='Загрузить', state=None)
async def cms_start(message: types.Message, state: FSMContext):
    await FSMsAdmin.photo.set()
    await message.reply('Загрузите фото  (Пока что не работает)')


# @dp.message_handler(commands='Загрузить', state=None)
async def cms_start1(message: types.Message, state: FSMContext):
    global x
    #  async with state.proxy()
    await FSMsAdmin.text.set()
    await message.reply('Напишите текст')


# @dp.message_handler(state=FSMAdmin.name)
async def cms_start2(message: types.Message, state: FSMContext):
    global notif_count
    # message.text Сохраняем в бд (Имя)
    notifications[notif_count] = [message.text]
    await FSMsAdmin.next()
    await message.reply("Поставьте число в формате 31 12  (день\пробел\месяц)")


# @dp.message_handler(state=FSMAdmin.mail)
async def cms_start3(message: types.Message, state: FSMContext):
    global notif_count
    temp = notifications[notif_count]
    a = message.text
    a.strip(' ')
    a, b = a.split(' ')
    temp += [a]
    temp += [b]
    notifications[notif_count] = temp
    await FSMsAdmin.date.set()
    await message.reply("Поставьте время в формате 12:30 (час\двоеточие\минуты)")


# @dp.message_handler(state=FSMAdmin.how)
async def cms_start4(message: types.Message, state: FSMContext):
    global notif_count
    # message.text Сохраняем в бд (Как узнали)
    temp = notifications[x]
    a = message.text
    a, b = a.split(':')
    temp += [a]
    temp += [b]
    notifications[notif_count] = temp  # ['text', 'day', 'month', 'hour', minute]
    notif_count += 1
    await state.finish()
    await message.reply("Спасибо, вы зарегистрированы!")


def register_user(tg_id, name, email, phone, from_where):
    cursor.execute("INSERT INTO USERS(user_id_tg, name, email, phone, where_know) VALUES('{0}', '{1}', '{2}', '{3}', {4});".format(tg_id, name, email, phone, from_where))
    return 0


def register_message_handler(dp: Dispatcher):
    dp.register_message_handler(cms_start, text='Регистрация', state=None)
    dp.register_message_handler(cms_start2, state=FSMsAdmin.photo)
    dp.register_message_handler(cms_start3, state=FSMsAdmin.date)
    dp.register_message_handler(cms_start4, state=FSMsAdmin.time)
