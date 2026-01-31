

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

def print_grap_menu():
    """
        Toont het grappen-menu.

        Returns:
            print grap menu
        """
    print(
        "\n😂 Tijd voor een glimlach\n"
        "Wat voor grap mag het zijn?\n\n"
        "1. Programmeer grap\n"
        "2. Algemene grap\n"
        "3. Verras me! \n"
        "4. Terug naar hoofdmenu\n")

def print_tweedelig_single_grap ():
    print(
       f"Wil je een single liner, of ben je in de mood voor two part grap?\n"
       f"1. Single\n"
       f"2. Two part\n"
    )


def print_grap_actie_menu():
    """
      Toont het vervolg menu na het tonen van een grap.

      De gebruiker kan nog een grap opvragen of teruggaan
      naar het hoofdmenu.

      Returns:
          print van het grap actie menu
      """
    print(
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

