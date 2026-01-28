import sys

import requests

from api_keys import API_KEY_API_NINJAS, API_NINJAS_BASE_URL

to_do_lijst = []

# Algemene functies

def vraag_menu_keuze(vraag: str, min_keuze: int, max_keuze: int):
    """ Vraagt de input en vangt error's op

    params: vraag(str): De keuze die de gebruiker kan maken in het menu
            min_keuze(int): Minimal keuze
            max_keuze(int): Maximale keuze

    Returns: keuze
    """
    while True:
        try:
            keuze = int(input(vraag))
            if min_keuze <= keuze <= max_keuze:
                return keuze
            print(f"Kies een getal tussen {min_keuze} en {max_keuze}: ")
        except ValueError:
            print(f"Voer een geldig getal in ({min_keuze} - {max_keuze}): ", file=sys.stderr)

# Hoofdmenu

def print_hoofdmenu():
    """Print het hoofdmenu.

      Returns:
          print hoofdmenu
      """
    print(
        "\n✨ Welkom bij MoodBooster ✨\n"
        + "-" * 30 + "\n"
        "Wat kan ik vandaag voor je doen?\n\n"
        "1. Geef me een motiverende boost\n"
        "2. Verras me met een grap\n"
        "3. Ik voel me overweldigd, geef me overzicht\n"
        "4. Afsluiten\n"
    )

def keuze_hoofdmenu ():
    """
    Vraagt om gekozen input
    Roep het gekozen menu aan of sluit af indien gewenst

    :return: gekozen menu of afsluiten
    """

    while True:
        print_hoofdmenu()
        keuze = vraag_menu_keuze("Selecteer je optie (1 - 4): ", 1,4)

        if keuze == 1:
            keuze_motivatie_menu()
        elif keuze == 2:
            keuze_grap_menu()
        elif keuze == 3:
            keuze_to_do_list()
        elif keuze == 4:
            print("Tot ziens! 👋")
            break

# Motivatie

def print_motivatie_menu():
    """
      Toont het motivatie-menu.

      Returns:
          print van het motivatie menu
      """
    print(
        "\n💡 Motivatie\n"
        "Waar heb je vandaag behoefte aan?\n\n"
        "1. Inspiratie quote\n"
        "2. Moed quote\n"
        "3. Succes quote\n"
        "4. Terug naar hoofdmenu\n"
    )

def keuze_motivatie_menu():
    """
    Motivatie-menu loop
    :return: quote met passende categorie of naar het hoofdmenu
    """
    while True:
        print_motivatie_menu()
        keuze = vraag_menu_keuze("Selecteer je optie: (1 - 4): ", 1,4)

        if keuze == 1:
            categorie = "inspirational"
        elif keuze == 2:
            categorie = "courage"
        elif keuze == 3:
            categorie = "success"
        elif keuze == 4:
            return

        print(haal_quote_op(categorie))
        keuze_actie_motivatie_menu(categorie)

def print_motivatie_actie_menu():
    """
        Toont het vervolgmenu na het tonen van een quote.

        De gebruiker kan een nieuwe quote opvragen, van categorie wisselen,
        of teruggaan naar het hoofdmenu.

        Returns:
            print van het actie motivatie menu
        """
    print("\nWat wil je nu doen?\n\n"
        "1. Nog een quote\n"
        "2. Andere categorie kiezen\n"
        "3. Terug naar hoofdmenu\n")

def keuze_actie_motivatie_menu(categorie):
    while True:
        print_motivatie_actie_menu()
        keuze = vraag_menu_keuze("Selecteer je optie (1 - 3): ", 1,3)

        if keuze == 1:
            print(haal_quote_op(categorie))
        elif keuze == 2:
            keuze_motivatie_menu()
        elif keuze == 3:
            keuze_hoofdmenu()

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


def print_grap_menu():
    """
        Toont het grappen-menu.

        Returns:
            print grap menu
        """
    print(
        "\n😂 Tijd voor een glimlach\n"
        "Wat voor grap mag het zijn?\n\n"
        "1. Programmeer / nerdy grap\n"
        "2. Algemene grap\n"
        "0. Terug naar hoofdmenu\n")

def grap_actie_menu():
    """
      Toont het vervolg menu na het tonen van een grap.

      De gebruiker kan nog een grap opvragen of teruggaan
      naar het hoofdmenu.

      Returns:
          None
      """
    return(
        "\nWil je nog even doorgaan?\n\n"
        "1. Nog een grap\n"
        "0. Terug naar hoofdmenu\n"
    )

def print_todo_menu():
    """
       Toont het to-do menu voor wanneer de gebruiker overweldigd is.

       In dit menu kan de gebruiker taken toevoegen, bekijken, verwijderen en
       sorteren.

       Returns:
           print van to do menu
       """

    print(
        "\n🧠 Rust in je hoofd\n"
        "Wat wil je doen?\n\n"
        "1. Taak toevoegen\n"
        "2. Taken bekijken\n"
        "3. Taak verwijderen\n"
        "4. Sorteren op prioriteit\n"
        "5. Sorteren op stressniveau\n"
        "6. Terug naar hoofdmenu\n")

def keuze_to_do_list ():
    while True:
        print_todo_menu()
        keuze = vraag_menu_keuze("Selecteer je optie: (1 - 6): ", 1,6)

        if keuze == 1:
            taak = input("Voer de uit te voeren taak in: ")
            prioriteit = int(input("Hoe hoog is de prioriteit (1 - 5): "))
            stressniveau = int(input("Hoe hoog is het stressniveau (1 - 5): "))


            to_do_lijst.append( {
                "taak": taak,
                "prioriteit": prioriteit,
                "stressniveau": stressniveau
            })

            print(f'"{taak}" is toegevoegd aan de to do lijst')
            print("*" * 50)

        if keuze == 2:
            if not to_do_lijst:
                print("Je to-do lijst is leeg")
            else:
                for taken in to_do_lijst:
                    print(taken["taak"])


def main():
    keuze_hoofdmenu()

main()
