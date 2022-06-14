import time

from aiogram import types, Dispatcher
from create_bot import bot
from keyboards import client_kb
from FSM.RegisterFSM import *
from FSM.NotificFSM import *
# from main import cursor

ALL_USERS_BD = [814991257]
admin_idBD = 814991257
ALL_Notif = [11]
"""//////////////////////////////////////////////////////////////////////////////////////////////////////////////////"""

NOTIFICATIONS = {
    'text': ['photo', 'date', 'time']
}


def get_ids_of_users():
    # cursor.execute("SELECT user_id_tg FROM users;")
    # return [i[0] for i in cursor.fetchall()]
    pass


async def command_start(message: types.Message):
    try:
        if message.from_user.id == admin_idBD:
            await bot.send_message(message.from_user.id, '🤖')
            await bot.send_message(message.from_user.id, 'Админ, добрый день!', reply_markup=client_kb.AdminMenu)
        else:
            await bot.send_message(message.from_user.id, '👨‍🏫')
            await bot.send_message(message.from_user.id, 'Добрый день, это онлайн школа "....". '
                                                         'Пожалуйста, введите свой номер телефона,'
                                                         ' чтобы продолжить!)')
    except Exception:
        await message.reply('Общение с ботом через группы - запрещено!')

"""//////////////////////////////////////////////////////////////////////////////////////////////////////////////////"""


async def OneTen(message: types.Message):
    if 1 >= int(message.text):
        await bot.send_message(message.from_user.id, 'Спасибо за ваш отзыв! \nПостараемся работать лучше!')
    elif 1 < int(message.text) <= 10:
        print("Спасибо за ваш отзыв!")
    elif int(message.text) > 10:
        temp = 10
        print("Спасибо за ваш отзыв!")
    else:
        temp = 0
        print("Спасибо за ваш отзыв! \nПостараемся работать лучше!")


async def text(message: types.Message):
    if message.text == 'Регистрация':
        await bot.send_message(message.from_user.id, 'Регистрация')
        # запрос

    elif message.text == 'Опрос':
        await bot.send_message(message.from_user.id, 'Оцените наш сервис!)', reply_markup=client_kb.one_ten)

    elif message.text == 'Посмотреть статистику' and message.from_user.id == admin_idBD:
        await bot.send_message(message.from_user.id, 'Статистика')

    elif message.text == 'Регистрация' and message.from_user.id == admin_idBD:
        await bot.send_message(message.from_user.id, 'Рассылка')
    else:
        temp = message.text
        temp = temp.replace(' ', '')
        temp = temp.replace('+7', '8')
        if len(temp) == 11 and temp[0] == '8':
            await bot.send_message(message.from_user.id, 'Все сохранено!)', reply_markup=client_kb.AccountMenu)
        elif temp[0] == '8':
            await bot.send_message(message.from_user.id, 'Что то пошло не так( Попробуйте еще раз!')
        else:
            if 1 >= int(message.text):
                await bot.send_message(message.from_user.id, 'Спасибо за ваш отзыв! \nПостараемся работать лучше!', reply_markup=client_kb.AccountMenu)
            elif 1 < int(message.text) <= 10:
                await bot.send_message(message.from_user.id, "Спасибо за ваш отзыв!", reply_markup=client_kb.AccountMenu)
            elif int(message.text) > 10:
                temp = 10
                await bot.send_message(message.from_user.id, "Спасибо за ваш отзыв!", reply_markup=client_kb.AccountMenu)
            elif 1 > int(message.text):
                temp = 0
                await bot.send_message(message.from_user.id, "Спасибо за ваш отзыв! \nПостараемся работать лучше!",
                                       reply_markup=client_kb.AccountMenu)
            else:
                await bot.send_message(message.from_user.id, 'Что то пошло не так( Попробуйте еще раз')


async def task():
    while True:
        await asyncio.sleep(58)
        for j in ALL_Notif:
            if time.time() == time.time():  # == j
                temp = get_ids_of_users()
                for i in temp:
                    await bot.send_message(i, '')


"""//////////////////////////////////////////////////////////////////////////////////////////////////////////////////"""


def register_handlers_client(dp: Dispatcher):  # Функция регистрации хендлеров
    dp.register_message_handler(command_start, commands=['start'])

    #  dp.register_message_handler(OneTen, text='Опрос')

    dp.register_message_handler(cm_start, text='Регистрация', state=None)
    dp.register_message_handler(cm_start2, state=FSMAdmin.name)
    dp.register_message_handler(cm_start3, state=FSMAdmin.mail)
    dp.register_message_handler(cm_start4, state=FSMAdmin.how)

    dp.register_message_handler(cms_start, text='Рассылка', state=None)
    dp.register_message_handler(cms_start2, state=FSMsAdmin.photo)
    dp.register_message_handler(cms_start2, state=FSMsAdmin.text)
    dp.register_message_handler(cms_start3, state=FSMsAdmin.date)
    dp.register_message_handler(cms_start4, state=FSMsAdmin.time)

    dp.register_message_handler(text)
