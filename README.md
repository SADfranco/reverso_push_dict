
# push notification in Telegram from favorites list in Recorso Context App
At first, you create an account in Reverco Context. Then you can add words into your favorites. This bot will send you notifications from favorites list with Russian translation, English definition and transcription (connection with https://api.dictionaryapi.dev). Also you can create your own schedule when bot will send notifications 
One more function of this bot is sending list of twenty last or random words with Russian translation on schedule.
The dictionary is saved in json file automatically every night and send you notification about that.

Example notifications:







# reverso_context_api
Simple Python API for [Reverso Context](https://context.reverso.net)

## Installation
```pip install reverso-context-api```

## Entry point
All operations are implemented in class `Client`.     
```python3
from reverso_context_api import Client
```

It takes source and target languages ("de"/"en"/"ru"/etc) as required arguments. They will be used as defaults, but you can set another pair for each operation. <br>
```python3
client = Client("de", "en")
```

Also you can pass login credentials to be able to work with your favorites:<br>
```python3
client = Client("en", "ru", credentials=("email", "password"))
```

## Supported features
* Getting translations:<br>
```python3
>>> list(client.get_translations("braucht"))
['needed', 'required', 'need', 'takes', 'requires', 'take', 'necessary'...]
```
* Getting translation samples (context):<br>
```python3
>>> client = Client("en", "ru")
>>> for context in client.get_translation_samples("shenanigans", cleanup=True):
...     print(context)
("The simple fact is the city is going broke cleaning up after Homer's drunken shenanigans...", 
 "Простой факт: город разорится, восстанавливаясь после пьяных проделок Гомера...")
("You need a 12-step program for shenanigans addicts.", 
 "Тебе нужно пройти 12-ти ступенчатую программу зависимости от проделок.")
```
* Getting search suggestions:<br>
```python3
>>> list(Client("de", "en").get_search_suggestions("bew")))
['Bewertung', 'Bewegung', 'bewegen', 'bewegt', 'bewusst', 'bewirkt', 'bewertet'...]
```
* Getting your saved favorites (you'll have to pass login credentials):
```python3
>>> client = Client("en", "de", credentials=("email", "password"))
>>> next(client.get_favorites())
{'source_lang': 'de', 'source_text': 'imstande', 'source_context': 'Ich würde lachen, doch ich bin biologisch nicht imstande dazu.', 
 'target_lang': 'ru', 'target_text': 'способен', 'target_context': 'Я бы посмеялся, но мой вид на это не способен.'}
```

All the methods return iterators (to hide paging and to not request more results than needed)
