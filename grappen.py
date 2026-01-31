import requests
from algemene_functies import vraag_menu_keuze
from menus import print_grap_menu, print_tweedelig_single_grap, print_grap_actie_menu
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


def keuze_grap_menu():

    while True:
        print_grap_menu()
        keuze = vraag_menu_keuze("Selecteer je optie (1 - 4): ", 1, 4)

        if keuze == 1:
            return "Programming"

        elif keuze == 2:
            return "Misc"

        elif keuze == 3:
            return "Any"

        elif keuze == 4:
            return "Hoofdmenu"



def keuze_tweedelig_single_grap():
    print_tweedelig_single_grap()
    keuze = vraag_menu_keuze("Selecteer je optie (1 - 2): ", 1, 2)

    if keuze == 1:
        return "single"
    else:
        return "twopart"

def print_grap():
    categorie = keuze_grap_menu()

    if categorie == "Hoofdmenu":
        return

    single_twopart = keuze_tweedelig_single_grap()
    grap_data = get_grap(categorie, single_twopart)

    print("\n😂 Hier komt je grap:\n")

    if single_twopart == "single":
        print(grap_data["joke"])
        return grap_actie_menu()


    elif single_twopart == "twopart":
        print(grap_data["setup"])
        input("\n(Druk op Enter voor de punchline...)")
        print(grap_data["delivery"])
        return grap_actie_menu()




def grap_actie_menu():
    while True:
        print_grap_actie_menu()
        actie = vraag_menu_keuze("Selecteer je optie: ", 1, 2)

        if actie == 1:
            print_grap()
        elif actie == 2:
            return "Hoofdmenu"








