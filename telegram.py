import telebot
import config
#import pb
import datetime
import pytz
import json
import traceback
import main
from reverso_context_api import Client
import random
import time
import datetime
from multiprocessing import *
import schedule
import requests
import test
import re

bot = telebot.TeleBot(config.TOKEN)

# Функция, которая будет отправлять сообщение
def send_message():
    client = Client("en", "ru", credentials=(config.USER, config.PASSWORD))
    result = list(client.get_favorites())
    ran = random.choice(result)
    source_text = str('@'+ ran['source_text'] + '  ::::::')
    target_text = str(ran['target_text'])
    source_context = str(ran['source_context'])
    remove_context = re.sub('[-,.\-/=!&?-]', '', source_context)
    target_context = str(ran['target_context'])
    remove_target = re.sub('[-,.\-/=!&?-]', '', target_context)
    new_line = '\n'
    total_source = f"{source_text}  ||{target_text}||{new_line}{remove_context}"
    total_target = f"||{remove_target}||"
    bot.send_message(config.CHAT_ID, text = total_source , parse_mode="MarkdownV2")
    bot.send_message(config.CHAT_ID, text = total_target , parse_mode="MarkdownV2")

# Задаем время отправки сообщения
schedule.every(30).minutes.do(send_message)

# Бесконечный цикл для проверки расписания
while True:
    schedule.run_pending()
    time.sleep(1)





