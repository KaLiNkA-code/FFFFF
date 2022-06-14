from aiogram.utils import executor
from create_bot import dp
from handlers import client
import asyncio
import psycopg2
import requests


conn = psycopg2.connect(dbname='online_school', user='kalinka',
                        password='kalinka15682936124169236187238172638', host='localhost')
cursor = conn.cursor()

cursor.execute('CREATE TABLE users (id serial PRIMARY KEY, user_id_tg VARCHAR ( 50 ) UNIQUE NOT NULL, name VARCHAR ( 50 ) NOT NULL, email VARCHAR ( 255 ) UNIQUE NOT NULL, phone VARCHAR ( 50 ) NOT NULL, where_know VARCHAR ( 100 ));')
cursor.fetchall()

def register_user(tg_id, name, email, phone, from_where):
    cursor.execute("INSERT INTO USERS(user_id_tg, name, email, phone, where_know) VALUES('{0}', '{1}', '{2}', '{3}', '{4}');".format(tg_id, name, email, phone, from_where))
    cursor.fetchall()
    return 0

def check_user_exists(tg_id, phone):
    cursor.execute("SELECT * FROM users WHERE user_id_tg = " + tg_id + " AND phone = " + phone + ";")
    try:
        res = cursor.fetchall()[0]
    except:
        """register_user_func() """


def send_activity(chat_id, bot_id):
    headers = {
        'X-Token': 'e12d72fab4dc966c3040b955ffbce079',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = 'title=Активность&name=activity&bot={0}&chat_id={1}'.format(bot_id, chat_id)
    response = requests.post('https://api.bottec.webmasterskaya.xyz/api/v1/targets/hit', headers=headers, data=data)


def send_start(chat_id, bot_id):
  headers = {
    'X-Token': 'e12d72fab4dc966c3040b955ffbce079',
    'Content-Type': 'application/x-www-form-urlencoded',
  }

  data = 'title=Запуск бота&name=start&bot={0}&chat_id={1}'.format(bot_id, chat_id)
  response = requests.post('https://api.bottec.webmasterskaya.xyz/api/v1/targets/hit', headers=headers, data=data)


async def on_startup():
    loop = asyncio.get_event_loop()
    loop.create_task(client.task())
    print('Бот вышел в online')


client.register_handlers_client(dp)
# RegisterFSM.register_message_handler(dp)


executor.start_polling(dp, skip_updates=True) #  on_startup=on_startup)  # Команда запуска бота
