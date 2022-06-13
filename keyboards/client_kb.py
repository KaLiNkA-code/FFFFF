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


one_ten = ReplyKeyboardMarkup(row_width=2)
b1 = KeyboardButton(text='1', callback_data='1')
b2 = KeyboardButton(text='2', callback_data='2')
b3 = KeyboardButton(text='3', callback_data='3')
b4 = KeyboardButton(text='4', callback_data='4')
b5 = KeyboardButton(text='5', callback_data='5')
b6 = KeyboardButton(text='6', callback_data='6')
b7 = KeyboardButton(text='7', callback_data='7')
b8 = KeyboardButton(text='8', callback_data='8')
b9 = KeyboardButton(text='9', callback_data='9')
b10 = KeyboardButton(text='10', callback_data='10')
one_ten.add(b10).add(b9, b8, b7, b6, b5, b4, b3, b2).add(b1)
