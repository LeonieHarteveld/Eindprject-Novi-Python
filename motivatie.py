import requests
from api_keys import API_KEY_API_NINJAS, API_NINJAS_BASE_URL
from algemene_functies import vraag_menu_keuze
from menus import print_motivatie_menu, print_motivatie_actie_menu

hoofdmenu = "Hoofdmenu"


def haal_quote_op (categorie):
    """
    Haalt quote op via API Ninja

    :param categorie: "inspirational", "courage", "succes", "Hoofdmenu"
    :return: quote + auteur
    """
    headers = {"X-Api-Key" : API_KEY_API_NINJAS}
    params = {"categories": categorie}

    response = requests.get(API_NINJAS_BASE_URL, headers=headers, params=params)
    if response.ok:
        data = response.json()
        quote = data[0]["quote"]
        author = data[0]["author"]
        return f"\nJouw inspiratie quote is:\n\n{quote} \n- {author}\n"

    else:
        return f"Er is iets misgegaan. Status code: {response.status_code}"

def toon_quote_en_vervolg(categorie):
    """
    Print een quote en start het actie-menu.

    :param categorie: "inspirational", "courage", "success"
    :return: hoofdmenu
    """
    print(haal_quote_op(categorie))

    actie = keuze_actie_motivatie_menu(categorie)
    if actie == hoofdmenu:
        return hoofdmenu

    return None

def keuze_motivatie_menu():
    """
    Motivatie-menu loop

    :return: quote met passende categorie of naar het hoofdmenu
    """
    while True:
        print_motivatie_menu()
        keuze = vraag_menu_keuze("Selecteer je optie: (0 - 3): ", 0,3)
        categorie = ""

        if keuze == 1:
            categorie = "inspirational"
        elif keuze == 2:
            categorie = "courage"
        elif keuze == 3:
            categorie = "success"
        elif keuze == 0:
            return hoofdmenu

        resultaat = toon_quote_en_vervolg(categorie)
        if resultaat == hoofdmenu:
            return hoofdmenu


# Dit menu geeft o.a. de optie om nog een quote van dezelfde categorie op te halen.
# Helaas kan dit alleen met de betaalde functie.
# Echter, heb ik hem er wel ingelaten, voor eventuele doorontwikkeling.

def keuze_actie_motivatie_menu(categorie):
    """
    Vraagt naar de vervolg stappen van de gebruiker

    :param categorie: "inspirational", "courage", "succes", "Hoofdmenu"
    :return: hoofdmenu
    """
    while True:
        print_motivatie_actie_menu()
        keuze = vraag_menu_keuze("Selecteer je optie (0 - 2): ", 0,2)

        if keuze == 1:
            print(haal_quote_op(categorie))
        elif keuze == 2:
            break
        elif keuze == 0:
            return hoofdmenu