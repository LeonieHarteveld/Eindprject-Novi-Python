

import requests
from algemene_functies import vraag_menu_keuze
from menus import print_grap_menu
from api_keys import JOKE_API_BASE_URL

def get_grap (categorie: str, joke_type: str):
    url = f"{JOKE_API_BASE_URL}/{categorie}"
    params = {
        "type": joke_type,
        "safe-mode": "true",
        "blacklistFlags": "nsfw,religious,political,racist,sexist,explicit"
    }

    response = requests.get(url, params=params)

    if response.ok:
        grappen_data = response.json()
        return grappen_data

    else:
        return f"Er is iets misgegaan. Status code: {response.status_code}"

print(get_grap("Any", "single"))


# def keuze_grap_menu():
#
#     while True:
#         print_grap_menu()
#         keuze = vraag_menu_keuze("Selecteer je optie (1 - 3): ", 1, 3)
#
#         if keuze == 1:
#             pass
#
#         elif keuze == 2:
#             pass
#
#         elif keuze == 3:
#             break
