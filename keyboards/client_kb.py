from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


AccountMenu = ReplyKeyboardMarkup(row_width=1)
b1 = KeyboardButton(text='Регистрация')
b2 = KeyboardButton(text='Опрос')
AccountMenu.add(b1, b2)


AdminMenu = ReplyKeyboardMarkup(row_width=1)
SubscribeAccount = KeyboardButton(text='Посмотреть статистику')
X = KeyboardButton(text='Рассылка')
AdminMenu.add(SubscribeAccount, X)


Yes_No_kb = ReplyKeyboardMarkup(row_width=2)
Yes = KeyboardButton(text='Да!', callback_data='Yes')
No = KeyboardButton(text='Нет', callback_data='No')
Yes_No_kb.add(Yes, No)


Statistic_kb = ReplyKeyboardMarkup(row_width=1)
b1 = KeyboardButton(text='Кол-во пользователей')
b2 = KeyboardButton(text='Кол-во новых пользователей')
b3 = KeyboardButton(text='Сред. провождение в боте')
Statistic_kb.add(b1, b2, b3)

Statistic_kb2 = ReplyKeyboardMarkup(row_width=1)
b1 = KeyboardButton(text='День')
b2 = KeyboardButton(text='Неделя')
b3 = KeyboardButton(text='Месяц')
Statistic_kb2.add(b1, b2, b3)


one_ten = ReplyKeyboardMarkup(row_width=2)
b1 = KeyboardButton(text='1')
b2 = KeyboardButton(text='2')
b3 = KeyboardButton(text='3')
b4 = KeyboardButton(text='4')
b5 = KeyboardButton(text='5')
b6 = KeyboardButton(text='6')
b7 = KeyboardButton(text='7')
b8 = KeyboardButton(text='8')
b9 = KeyboardButton(text='9')
b10 = KeyboardButton(text='10')
one_ten.add(b10).add(b9, b8, b7, b6, b5, b4, b3, b2).add(b1)
