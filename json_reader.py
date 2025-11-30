import json

import asyncio

JSON_DIR = "conf"

class JSON_NAMES:
    ALL_DISEASES = "all.json"





async def get_all_ru_diseases() -> [str]:
    ru_list = []

    with open(f"{JSON_DIR}/{JSON_NAMES.ALL_DISEASES}", "r", encoding="UTF-8") as file:
        content = json.load(file)

        for key, value in content.items():
            ru_list.append(value)

    return ru_list

async def get_all_diseases() -> {str : str}:
    with open(f"{JSON_DIR}/{JSON_NAMES.ALL_DISEASES}", "r", encoding="UTF-8") as file:
        content = json.load(file)

    return content





