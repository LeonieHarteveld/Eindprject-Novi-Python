

def print_hoofdmenu():
    """
    Toont het hoofdmenu. De gebruiker kan kiezen tussen een motiverende quote, een grap,
    het maken van een to lijst of afsluiten

      Returns:
          print hoofdmenu
      """
    print(
        "\n✨ Welkom bij MoodBooster ✨\n"
        + "-" * 30 + "\n"
        "Wat kan ik vandaag voor je doen?\n\n"
        "1. 💬 Inspiratieboost (motiverende quote) \n"
        "2. 😂 Lachmomentje (grap)\n"
        "3. 🧠 Rust in je hoofd (to-do lijst maken)\n"
        "0. 👋 Afsluiten\n"
    )

def print_motivatie_menu():
    """
      Toont het motivatie-menu.
      De gebruiker kan kiezen tussen een inspirerende quote, moed quote,
      succes quote of terug naar het hoofdmenu

      Returns:
          print motivatie menu
      """
    print(
        "\n💡 Motivatie\n"
        + "-" * 30 + "\n"
        "Waar heb je vandaag behoefte aan?\n\n"
        "1. ✨ Een inspirerende quote\n"
        "2. 💪 Een moed-gevende quote\n"
        "3. 🚀 Een succesquote\n"
        "0. ↩ Terug naar het hoofdmenu\n"
    )

def print_motivatie_actie_menu():
    """
        Toont het vervolgmenu na het tonen van een quote.

        De gebruiker kan een nieuwe quote opvragen, van categorie wisselen,
        of teruggaan naar het hoofdmenu.

        Returns:
            print actie motivatie menu
        """
    print("-" * 30 + "\n" +
        "Wat wil je nu doen?\n\n"
        "1. 🔁 Ontvang nog een quote\n"
        "2. 📂 Kies een andere categorie\n"
        "0. ↩ Terug naar het hoofdmenu\n")

def print_grap_menu():
    """
        Toont het grappen-menu.
        De gebruiker kan kiezen tussen een programmeergrap, algemene grap, willekeurige grap
        of terug naar het hoofdmenu

        Returns:
            print grap menu
        """
    print(
        "\n😂 Tijd voor een glimlach\n"
        + "-" * 30 + "\n"
        "Wat voor grap mag het zijn?\n\n"
        "1. 💻 Een programmeergrap\n"
        "2. 😄 Een algemene grap\n"
        "3. 🎲 Verras me met een willekeurige grap\n"
        "0. ↩ Terug naar het hoofdmenu\n")

def print_tweedelig_single_grap ():
    """
    Toont het menu voor een single liner of two-part joke

    :return: print menu single of two-part joke
    """
    print(
        f"\n{"-" * 30} \n"
        f"Waar heb je zin in?\n\n"
        f"1. ⚡ One-liner (korte grap)\n"
        f"2. 🧩 Two-part grap (opzet + punchline)\n")


def print_grap_actie_menu():
    """
      Toont het vervolg menu na het tonen van een grap.

      De gebruiker kan nog een grap opvragen of teruggaan
      naar het hoofdmenu.

      Returns:
          print grap actie menu
      """
    print(
        f"\n{"-" * 30} "
        "\nWil je nog even doorgaan?\n\n"
        "1. 😂 Ontvang nog een grap\n"
        "0. ↩ Terug naar het hoofdmenu\n"
    )

def print_todo_menu():
    """
       Toont het to-do menu.

       In dit menu kan de gebruiker taken toevoegen, bekijken, verwijderen en
       sorteren.

       Returns:
           print to do menu
       """

    print(
        "\n🧠 Rust in je hoofd\n"
        + "-" * 30 + "\n"
         "Wat wil je nu doen?\n\n"
         "1. ➕ Voeg een taak toe\n"
         "2. 📋 Bekijk je taken\n"
         "3. 🗑 Verwijder een taak\n"
         "4. ⭐ Sorteer taken op prioriteit\n"
         "5. 🌊 Sorteer taken op stressniveau\n"
         "0. ↩ Terug naar het hoofdmenu\n"
    )

