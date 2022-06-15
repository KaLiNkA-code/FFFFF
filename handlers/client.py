import time

import TempUserBD
from TempUserBD import users
from aiogram import types, Dispatcher
from create_bot import bot
from keyboards import client_kb
from FSM.RegisterFSM import *
from FSM.NotificFSM import *
from main import cursor
from datetime import datetime
#  from FSM.NotificFSM import storage
from Statistic import new_users30, new_users29, new_users28, new_users27, new_users26, \
        new_users25, new_users24, new_users23, new_users22, new_users21, new_users20, new_users19, new_users18, \
        new_users17, new_users16, new_users15, new_users14, new_users13, new_users12, new_users11, new_users10, \
        new_users9, new_users8, new_users7, new_users6, new_users5, new_users4, new_users3, new_users2, new_users1, \
        day_sum, week_sum, month_sum

ALL_USERS_BD = [814991257]
admin_idBD = 81499257
ALL_Notif = [11]


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
                                                         ' чтобы продолжить!')
    except Exception:
        await message.reply('Общение с ботом через группы - запрещено!')


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
        await bot.send_message(message.from_user.id, 'Оцените наш сервис!', reply_markup=client_kb.one_ten)

        """kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk    """

    elif message.text == 'Посмотреть статистику' and message.from_user.id == admin_idBD:
        await bot.send_message(message.from_user.id, 'Статистика', reply_markup=client_kb.Statistic_kb)

    elif message.text == 'Кол-во пользователей' and message.from_user.id == admin_idBD:
        await bot.send_message(message.from_user.id, 'Кол-во пользователей')

    elif message.text == 'Сред. провождение в боте' and message.from_user.id == admin_idBD:
        await bot.send_message(message.from_user.id, 'Сред. провождение в боте')

    elif message.text == 'Кол-во новых пользователей' and message.from_user.id == admin_idBD:
        await bot.send_message(message.from_user.id, 'Кол-во новых пользователей за:',
                               reply_markup=client_kb.Statistic_kb2)

    elif message.text == 'День' and message.from_user.id == admin_idBD:
        await bot.send_message(message.from_user.id, f'Сегодня к нам присоединилось: {day_sum}', reply_markup=client_kb.Statistic_kb)

    elif message.text == 'Неделя' and message.from_user.id == admin_idBD:
        await bot.send_message(message.from_user.id, f'За эту неделю к нам присоединилось: {week_sum}', reply_markup=client_kb.Statistic_kb)

    elif message.text == 'Месяц' and message.from_user.id == admin_idBD:
        await bot.send_message(message.from_user.id, f'За этот месяц к нам присоединилось: {month_sum}', reply_markup=client_kb.Statistic_kb)

        """kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk    """

    elif message.text == 'Регистрация' and message.from_user.id == admin_idBD:
        await bot.send_message(message.from_user.id, 'Рассылка')
    else:
        temp = message.text
        temp = temp.replace(' ', '')
        temp = temp.replace('+7', '8')
        if len(temp) == 11 and temp[0] == '8':
            users[message.from_user.id] = [temp]
            global new_users1
            new_users1 += 1
            await bot.send_message(message.from_user.id, 'Все сохранено!)', reply_markup=client_kb.AccountMenu)

        elif temp[0] == '8':
            await bot.send_message(message.from_user.id, 'Что то пошло не так( Попробуйте еще раз!')
        else:
            if 1 >= int(message.text):
                await bot.send_message(message.from_user.id, 'Спасибо за ваш отзыв! \nПостараемся работать лучше!',
                                       reply_markup=client_kb.AccountMenu)
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
    global new_users30, new_users29, new_users28, new_users27, new_users26, \
        new_users25, new_users24, new_users23, new_users22, new_users21, new_users20, new_users19, new_users18, \
        new_users17, new_users16, new_users15, new_users14, new_users13, new_users12, new_users11, new_users10, \
        new_users9 , new_users8 , new_users7, new_users6, new_users5, new_users4, new_users3, new_users2, new_users1, j
    while True:
        now = datetime.now()
        '''Получение текущей даты'''

        current_hour = now.hour
        '''Получение текущего часа'''
        current_min = now.minute

        now_day = datetime.day
        now_month = datetime.month

        await asyncio.sleep(58)
        for j in TempUserBD.notifications:  # ['text', 'day', 'month', 'hour', minute]
            if current_hour == 00 and current_min == 00:
                new_users30 = new_users29
                new_users29 = new_users28
                new_users28 = new_users27
                new_users27 = new_users26
                new_users26 = new_users25
                new_users25 = new_users24
                new_users24 = new_users23
                new_users23 = new_users22
                new_users22 = new_users21
                new_users21 = new_users20
                new_users20 = new_users19
                new_users19 = new_users18
                new_users18 = new_users17
                new_users17 = new_users16
                new_users16 = new_users15
                new_users15 = new_users14
                new_users14 = new_users13
                new_users13 = new_users12
                new_users12 = new_users11
                new_users11 = new_users10
                new_users10 = new_users9
                new_users9 = new_users8
                new_users8 = new_users7
                new_users7 = new_users6
                new_users6 = new_users5
                new_users5 = new_users4
                new_users4 = new_users3
                new_users3 = new_users2
                new_users2 = new_users1
                new_users1 = 0

            if j[1] == now_day and j[2] == now_month and j[3] == current_hour and j[4] == current_min:  # == j
                temp = get_ids_of_users()
                for i in temp:
                    await bot.send_message(i, j[0])


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
