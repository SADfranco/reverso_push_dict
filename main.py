

from reverso_context_api import Client
import random
import config

client = Client("en", "ru", credentials=(config.USER, config.PASSWORD))

#client = Client("en", "ru")
#print(list(Client("de", "en").get_translations("braucht")))


def favorword():
        result = list(client.get_favorites())
        list_result = []
        for i in result:
            favor = f"{i['source_text']}-{i['target_text']}"
            list_result.append(favor)
        print(list_result)
        ran = random.choice(list_result)
        return print(ran)

favorword()