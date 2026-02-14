import requests
from algemene_functies import vraag_menu_keuze
from menus import print_grap_menu, print_tweedelig_single_grap, print_grap_actie_menu
from api_keys import JOKE_API_BASE_URL

hoofdmenu = "Hoofdmenu"

def get_grap (categorie, joke_type):
    """
    :param categorie:"Programming", "Mics", "Any"
    :param joke_type: "single" of "twopart"
    :return: dict uit JokeApi
    """
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
    """
    Vraagt de gebruiker naar input voor de soort grap

    :return: "Programming", "Misc", "Any" of "Hoofdmenu"
    """

    while True:
        print_grap_menu()
        keuze = vraag_menu_keuze("Selecteer je optie (0 - 3): ", 0, 3)

        if keuze == 1:
            return "Programming"

        elif keuze == 2:
            return "Misc"

        elif keuze == 3:
            return "Any"

        elif keuze == 0:
            return hoofdmenu


def keuze_tweedelig_single_grap():
    """
    Vraagt de gebruiker keuze te maken tussen een single of two-part joke

    :return: "single" of "twopart"
    """
    while True:
        print_tweedelig_single_grap()
        keuze = vraag_menu_keuze("Selecteer je optie (1 - 2): ", 1, 2)
        if keuze == 1:
            return "single"
        if keuze == 2:
            return "twopart"


def print_grap():
    """
    Print de grap a.d.h.v. de keuzes

    :return: grap_actie_menu()
    """
    categorie = keuze_grap_menu()

    if categorie == hoofdmenu:
        return hoofdmenu

    while True:
        single_two_part = keuze_tweedelig_single_grap()
        grap_data = get_grap(categorie, single_two_part)

        print("\n😂 Hier komt je grap:\n")

        if single_two_part == "single":
            print(grap_data["joke"])
            return grap_actie_menu()


        elif single_two_part == "twopart":
            print(grap_data["setup"])
            input("\n(Druk op Enter voor de punchline...)")
            print(f"\n{grap_data['delivery']}")

            return grap_actie_menu()




def grap_actie_menu():
    """
    Genereert nog een grap indien dit de keuze is en brengt weer terug naar het menu

    :return: hoofdmenu
    """
    while True:
        print_grap_actie_menu()
        actie = vraag_menu_keuze("Selecteer je optie (0 - 1) : ", 0, 1)

        if actie == 1:
            resultaat = print_grap()
            if resultaat == hoofdmenu:
                return hoofdmenu
        elif actie == 0:
            return hoofdmenu








