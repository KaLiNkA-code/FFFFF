from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import state
from aiogram import types
from create_bot import dp
from aiogram import Dispatcher
#  from  import cursor
from TempUserBD import users


"""
dict = {
    id = [user_id_tg, name, email, phone, where_know]
}
"""


class FSMAdmin(StatesGroup):
    name = State()
    mail = State()
    how = State()


# @dp.message_handler(commands='Загрузить', state=None)
async def cm_start(message: types.Message, state: FSMContext):
    await FSMAdmin.name.set()
    await message.reply('Введите свое имя)')


# @dp.message_handler(state=FSMAdmin.name)
async def cm_start2(message: types.Message, state: FSMContext):
    # message.text Сохраняем в бд (Имя)
    users[message.from_user.id] = [message.text]
    await FSMAdmin.mail.set()
    await message.reply("Введите почту")


# @dp.message_handler(state=FSMAdmin.mail)
async def cm_start3(message: types.Message, state: FSMContext):
    # message.text Сохраняем в бд (Почта)
    temp = users[message.from_user.id]
    temp += message.text
    users[message.from_user.id] = temp
    await FSMAdmin.how.set()
    await message.reply("Скажите пожалуйста, как вы узнали об этой школе?")


# @dp.message_handler(state=FSMAdmin.how)
async def cm_start4(message: types.Message, state: FSMContext):
    # message.text Сохраняем в бд (Как узнали)
    temp = users[message.from_user.id]
    temp += message.text
    users[message.from_user.id] = temp
    register_user(message.from_user.id, users[message.from_user.id][1], users[message.from_user.id][2], users[message.from_user.id][0], users[message.from_user.id][3])
    await state.finish()
    await message.reply("Спасибо, вы зарегистрированы!")


def register_user(tg_id, name, email, phone, from_where):
    cursor.execute("INSERT INTO USERS(user_id_tg, name, email, phone, where_know) VALUES('{0}', '{1}', '{2}', '{3}', {4});".format(tg_id, name, email, phone, from_where))
    return 0


def register_message_handler(dp: Dispatcher):
    dp.register_message_handler(cm_start, text='Регистрация', state=None)
    dp.register_message_handler(cm_start2, state=FSMAdmin.name)
    dp.register_message_handler(cm_start3, state=FSMAdmin.mail)
    dp.register_message_handler(cm_start4, state=FSMAdmin.how)
