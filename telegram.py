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


P_TIMEZONE = pytz.timezone(config.TIMEZONE)
TIMEZONE_COMMON_NAME = config.TIMEZONE_COMMON_NAME

bot = telebot.TeleBot(config.TOKEN)

# Функция, которая будет отправлять сообщение
def send_message():
    message = main.favorword
    bot.send_message(config.CHAT_ID, text=message)

# Задаем время отправки сообщения
schedule.every(60).minutes.do(send_message)

# Бесконечный цикл для проверки расписания
while True:
    schedule.run_pending()
    time.sleep(1)



























#from telebot import types
#
#import telebot;
#bot = telebot.TeleBot('6166691144:AAFu7ozWXPF1w_iQ7zPsxoaKYXix7P_0jQU');
#
#
#
#@bot.message_handler(content_types=['text'])
#def get_text_messages(message):
#    if message.text == "Привет":
#        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
#
#bot.polling(none_stop=True, interval=0)