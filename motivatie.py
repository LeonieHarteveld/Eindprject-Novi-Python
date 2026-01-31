import requests
from api_keys import API_KEY_API_NINJAS, API_NINJAS_BASE_URL
from algemene_functies import vraag_menu_keuze
from menus import print_motivatie_menu, print_motivatie_actie_menu


def haal_quote_op (categorie):
    """
    Haalt quote op via API Ninja
    :param categorie:
    :return: quote + auteur
    """
    headers = {"X-Api-Key" : API_KEY_API_NINJAS}
    params = {"categories": categorie}

    response = requests.get(API_NINJAS_BASE_URL, headers=headers, params=params)
    if response.ok:
        data = response.json()
        quote = data[0]["quote"]
        author = data[0]["author"]
        return f"\nJouw inspiratie quote is:\n{quote} - {author}"

    else:
        return f"Er is iets misgegaan. Status code: {response.status_code}"

def keuze_motivatie_menu():
    """
    Motivatie-menu loop
    :return: quote met passende categorie of naar het hoofdmenu
    """
    while True:
        print_motivatie_menu()
        keuze = vraag_menu_keuze("Selecteer je optie: (1 - 4): ", 1,4)
        categorie = ""

        if keuze == 1:
            categorie = "inspirational"
        elif keuze == 2:
            categorie = "courage"
        elif keuze == 3:
            categorie = "success"
        elif keuze == 4:
            categorie = "Hoofdmenu"
            return "Hoofdmenu"


        print(haal_quote_op(categorie))

        actie = keuze_actie_motivatie_menu(categorie)
        if actie == "Hoofdmenu":
            return "Hoofdmenu"



def keuze_actie_motivatie_menu(categorie):
    while True:
        print_motivatie_actie_menu()
        keuze = vraag_menu_keuze("Selecteer je optie (1 - 3): ", 1,3)

        if keuze == 1:
            print(haal_quote_op(categorie))
        elif keuze == 2:
            break
        elif keuze == 3:
            return "Hoofdmenu"