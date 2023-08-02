import telebot
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
import env
import schedule
import env
import json
import time
from reverso_context_api import Client
from random import sample

bot = telebot.TeleBot(env.TOKEN)


def reverso():
    client = Client("en", "ru", credentials=(env.USER, env.PASSWORD))
    result = list(client.get_favorites())
    #jsonStr = json.dumps(result)
    #json_obj = json.loads(jsonStr)
    #with open('data.json', 'w') as f:
    #    json.dump(json_obj, f)
    with open('dictonary.json') as f:
        templates = json.load(f)
    dict_sum = list(result + templates)
    dict_sum[:] = [x for i, x in enumerate(dict_sum) if i == dict_sum.index(x)]
    with open("dictonary.json", "w", encoding="utf-8") as file:
        json.dump(dict_sum, file)
    len_dict = str(len(dict_sum))
    bot.send_message(env.CHAT_ID, text = "Dictonary is created! Amout of words: " + len_dict )

def dictonary_read():
    with open('dictonary.json') as f:
        templates = json.load(f)
    return templates

def defin(x):
    try:
        response = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/'+ x)
        json_res = response.json()
        definition = json_res[0]['meanings'][0]['definitions'][0]['definition']
        pronounce = json_res[0]['phonetic']
    except TypeError:
        print('Ошибка TypeError')
        definition = '#'
        pronounce = '#'
    except SystemError:
        print('Ошибка SystemError')
        definition = '#'
        pronounce = '#'
    except ValueError:
        print('Ошибка ValueError')
        definition = '#'
        pronounce = '#'
    except SyntaxError:
        print('Ошибка SyntaxError')
        definition = '#'
        pronounce = '#'
    except KeyError:
        print('Ошибка KeyError')
        definition = '#'
        pronounce = '#'
    except UnboundLocalError:
        print('Ошибка UnboundLocalError')
        definition = '#'
        pronounce = '#'
    return [definition,pronounce]



# Функция, которая будет отправлять сообщение
def send_message():
    result = dictonary_read()
    ran = random.choice(result)
    source_text = str('@'+ ran['source_text'] + ' --- ')
    source_text_def = str(ran['source_text'])   
    dp = defin(source_text_def)
    defenition = str(dp[0])
    pronounce = str('[' + dp[1] + ']')
    remove_soorce_text = re.sub('[-,.\-/=!&?-]', '', source_text)
    target_text = str(ran['target_text'] + ' --- ')
    remove_targ_text = re.sub('[-,.\-/=!&?-]', '', target_text)
    source_context = str(ran['source_context'])
    remove_context = re.sub(source_text_def, source_text_def.upper(), source_context)
    target_context = str(ran['target_context'])
    remove_target = re.sub('[-,.\-/=!&?-]', '', target_context)
    new_line = '\n'
    d = 'D: '
    e = 'E: '
    total_source = f"{source_text.upper()}{target_text}{pronounce}{new_line}{d}{defenition}{new_line}{e}{remove_context}"
    bot.send_message(env.CHAT_ID, text = total_source ) #parse_mode="MarkdownV2")


def send_last20():
    list_ten_ = dictonary_read()
    ran = list_ten_[0:19]
    string_words = ''
    for i in ran:
        string_words += f"{i['source_text']} - {i['target_text']}" + '\n'
    bot.send_message(env.CHAT_ID, text = string_words)

def send_ran20():
    list_ten_ = dictonary_read()
    ran = sample(list_ten_,20)
    string_words = ''
    for i in ran:
        string_words += f"{i['source_text']} - {i['target_text']}" + '\n'
    bot.send_message(env.CHAT_ID, text = string_words)

# Задаем время отправки сообщения
#schedule.every(0.05).minutes.do(reverso)
schedule.every(60).minutes.do(send_message)
schedule.every().day.at("00:30").do(reverso)
schedule.every().day.at("10:00").do(send_last20)
schedule.every().day.at("17:00").do(send_ran20)

# Бесконечный цикл для проверки расписания
while True:
    schedule.run_pending()
    time.sleep(1)





