import sys

import requests

from api_keys import API_KEY_API_NINJAS, API_NINJAS_BASE_URL

def hoofdmenu():
    """
      Toont het hoofdmenu.

      Dit menu is het startpunt van de applicatie. De gebruiker kiest hier
      welke hoofdfunctionaliteit gestart wordt: motivatie, grap, overzicht/to-do,
      of afsluiten.

      Returns:
          keuze getal (1 - 4)
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

    while True:
        try:
            keuze = int(input("Selecteer je optie (1 - 4): "))
            if 1 <= keuze <= 4:
                return keuze
            print("Kies een getal tussen 1 en 4: ")
        except ValueError:
            print("Voer een geldig getal in: ", file=sys.stderr)

def keuze_hoofdmenu ():

    while True:
        user_input = hoofdmenu()

        if user_input == 1:
            return motivatie_menu()
        elif user_input == 2:
            return grap_menu()
        elif user_input == 3:
            return todo_menu()
        elif user_input == 4:
            print("Tot ziens! 👋")
            break

def motivatie_menu():
    """
      Toont het motivatie-menu.

      De gebruiker kiest een categorie (Focus, Doorzetten, Zelfvertrouwen.

      Returns:
          None
      """
    print(
        "\n💡 Motivatie\n"
        "Waar heb je vandaag behoefte aan?\n\n"
        "1. Inspiratie\n"
        "2. Moed\n"
        "3. Succes\n"
        "4. Terug naar hoofdmenu\n"
    )

    while True:
        try:
            keuze = int(input("Selecteer je optie (1 - 4): "))
            if 1 <= keuze <= 4:
                return keuze
            print("Kies een getal tussen 1 en 4: ")
        except ValueError:
            print("Voer een geldig getal in: ", file=sys.stderr)

def keuze_motivatie_menu():
    while True:
        keuze = motivatie_menu()

        if keuze == 1:
            categorie = "inspirational"  # let op: categorie moet bestaan bij API Ninjas
        elif keuze == 2:
            categorie = "courage"
        elif keuze == 3:
            categorie = "success"
        elif keuze == 4:
            return hoofdmenu()

        print(haal_quote_op(categorie))

def motivatie_actie_menu():
    """
        Toont het vervolgmenu na het tonen van een quote.

        De gebruiker kan een nieuwe quote opvragen, van categorie wisselen,
        of teruggaan naar het hoofdmenu.

        Returns:
            None
        """
    return(
        "\nWat wil je nu doen?\n\n"
        "1. Nog een quote\n"
        "2. Andere categorie kiezen\n"
        "0. Terug naar hoofdmenu\n"
    )

def haal_quote_op (categorie):
    headers = {
        "X-Api-Key" : API_KEY_API_NINJAS
    }

    params = {
        "categories": categorie
    }

    response = requests.get(API_NINJAS_BASE_URL, headers=headers, params=params)
    if response.ok:
        data = response.json()
        quote = data[0]["quote"]
        author = data[0]["author"]
        return f"{quote} - {author}"

    else:
        print(f"Er is iets misgegaan. Status code: {response.status_code}")




def grap_menu():
    """
        Toont het grappen-menu.

        De gebruiker kiest het type grap. Op basis van deze keuze kan de applicatie.

        Returns:
            None
        """
    return(
        "\n😂 Tijd voor een glimlach\n"
        "Wat voor grap mag het zijn?\n\n"
        "1. Programmeer / nerdy grap\n"
        "2. Algemene grap\n"
        "0. Terug naar hoofdmenu\n"
    )

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

def todo_menu():
    """
       Toont het to-do menu voor wanneer de gebruiker overweldigd is.

       In dit menu kan de gebruiker taken toevoegen, bekijken, verwijderen en
       sorteren.

       Returns:
           None
       """

    return(
        "\n🧠 Rust in je hoofd\n"
        "Wat wil je doen?\n\n"
        "1. Taak toevoegen\n"
        "2. Taken bekijken\n"
        "3. Taak verwijderen\n"
        "4. Sorteren op prioriteit\n"
        "5. Sorteren op stressniveau\n"
        "0. Terug naar hoofdmenu\n"
    )


print(keuze_hoofdmenu())