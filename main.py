from aiogram import Bot,Dispatcher,types
import json

def load_types():
    with open("conf/types.json","r") as json_file:
        typess = json.load(json_file)
        print(typess)


load_types()