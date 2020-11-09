# import the random library to help us generate the random numbers
import random
import pymongo
import os
import wikipedia
import pageviewapi  

DATABASE="nestor"
COLLECTION="wikipedia"

class NestorBot:

    # The constructor for the class. It takes the channel name as the a
    # parameter and then sets it as an instance variable
    def __init__(self, channel):
        self.channel = channel

    def _choose_message(self):
        text = ""
        #Conexión a MONGO
        myclient = pymongo.MongoClient(host=os.environ['MONGO_HOST'], port=int(os.environ['MONGO_PORT']))
        db = myclient[DATABASE]
        col = db[COLLECTION]
        
        #Consulta hacia la base de datos de citaciones para extraer una muestra aleatoria
        var = [{'$sample':{'size':1}}]
        results = col.aggregate(var)

        for doc in results:
            text=doc["text"]

        return {"type": "section", "text": {"type": "mrkdwn", "text": text}},

    # Craft and return the entire message payload as a dictionary.
    def get_message_payload(self):
        return {
            "channel": self.channel,
            "blocks": [
                *self._choose_message(),
            ],
        }
    def buscar_en_wikipedia(self, query):
        #return "pa k quieres saber eso jaja salu2"
        wikipedia.set_lang("es")
        return "{}\n\nBusca mas info en: {}".format(wikipedia.summary(query), wikipedia.page(query).url)
