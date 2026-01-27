
def hoofdmenu():
    """
      Toont het hoofdmenu.

      Dit menu is het startpunt van de applicatie. De gebruiker kiest hier
      welke hoofdfunctionaliteit gestart wordt: motivatie, grap, overzicht/to-do,
      of afsluiten.

      Returns:
          None
      """
    return(
        "\n✨ Welkom bij MoodBooster ✨\n"
        + "-" * 30 + "\n"
        "Wat kan ik vandaag voor je doen?\n\n"
        "1. Geef me een motiverende boost\n"
        "2. Verras me met een grap\n"
        "3. Ik voel me overweldigd, geef me overzicht\n"
        "0. Afsluiten\n"
    )

def motivatie_menu():
    """
      Toont het motivatie-menu.

      De gebruiker kiest een categorie (Focus, Doorzetten, Zelfvertrouwen.

      Returns:
          None
      """
    return(
        "\n💡 Motivatie\n"
        "Waar heb je vandaag behoefte aan?\n\n"
        "1. Focus\n"
        "2. Doorzetten\n"
        "3. Zelfvertrouwen\n"
        "0. Terug naar hoofdmenu\n"
    )

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

#Soorten grap aanpassen
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


print(hoofdmenu())