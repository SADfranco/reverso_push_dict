

from reverso_context_api import Client
import random
import config


#client = Client("en", "ru")
#print(list(Client("de", "en").get_translations("braucht")))

#client = Client("en", "ru", credentials=("shabaevandrew@gmail.com", "Aw253634"))
#result = list(client.get_favorites())
#for i in result:
#        new_line = '\n'
#        favor = f"{i['source_text']}-{i['target_text']}{new_line}{i['source_context']}-{i['target_context']}"
#        print(favor)


def favorword():
        client = Client("en", "ru", credentials=("shabaevandrew@gmail.com", "Aw253634"))
        result = list(client.get_favorites())
        list_result = []
        new_line = '\n'
        for i in result:
            favor = f"{i['source_text']}{new_line}{i['source_context']}{new_line}{i['target_text']}{new_line}{i['target_context']}"
            list_result.append(favor)
        ran = random.choice(list_result)
        return ran


#def favorwordruen():
#      client = Client("ru", "en", credentials=("shabaevandrew@gmail.com", "Aw253634"))
#      result = list(client.get_favorites())
#      list_result = []
#      for i in result:
#        favor = f"{i['source_text']}-{i['target_text']}"
#        list_result.append(favor)
#      print(list_result)
#      ran = random.choice(list_result)
#      return ran