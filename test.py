import sys
import requests

from api_keys import API_KEY_API_NINJAS, API_NINJAS_BASE_URL


# ---------------------------
# Algemene helpers
# ---------------------------

def vraag_menu_keuze(vraag: str, min_keuze: int, max_keuze: int) -> int:
    """
    Vraagt input en valideert een numerieke menu-keuze.

    Args:
        vraag: input prompt
        min_keuze: minimale geldige keuze
        max_keuze: maximale geldige keuze

    Returns:
        int: keuze binnen [min_keuze, max_keuze]
    """
    while True:
        try:
            keuze = int(input(vraag))
            if min_keuze <= keuze <= max_keuze:
                return keuze
            print(f"Kies een getal tussen {min_keuze} en {max_keuze}.")
        except ValueError:
            print(
                f"Voer een geldig getal in ({min_keuze} - {max_keuze}).",
                file=sys.stderr
            )


# ---------------------------
# Hoofdmenu
# ---------------------------

def print_hoofdmenu() -> None:
    """Print het hoofdmenu."""
    print(
        "\n✨ Welkom bij MoodBooster ✨\n"
        + "-" * 30 + "\n"
        "Wat kan ik vandaag voor je doen?\n\n"
        "1. Geef me een motiverende boost\n"
        "2. Verras me met een grap\n"
        "3. Ik voel me overweldigd, geef me overzicht\n"
        "4. Afsluiten\n"
    )


def keuze_hoofdmenu() -> None:
    """Hoofdloop van de applicatie."""
    while True:
        print_hoofdmenu()
        keuze = vraag_menu_keuze("Selecteer je optie (1 - 4): ", 1, 4)

        if keuze == 1:
            keuze_motivatie_menu()
        elif keuze == 2:
            keuze_grap_menu()   # placeholder (werkt, maar simpel)
        elif keuze == 3:
            keuze_todo_menu()   # placeholder (werkt, maar simpel)
        elif keuze == 4:
            print("Tot ziens! 👋")
            break


# ---------------------------
# Motivatie
# ---------------------------

def print_motivatie_menu() -> None:
    """Print het motivatie-menu."""
    print(
        "\n💡 Motivatie\n"
        "Waar heb je vandaag behoefte aan?\n\n"
        "1. Inspiratie quote\n"
        "2. Moed quote\n"
        "3. Succes quote\n"
        "4. Terug naar hoofdmenu\n"
    )


def print_motivatie_actie_menu() -> None:
    """Print het actie-menu na een quote."""
    print(
        "\nWat wil je nu doen?\n\n"
        "1. Nog een quote (zelfde categorie)\n"
        "2. Andere categorie kiezen\n"
        "3. Terug naar hoofdmenu\n"
    )


def keuze_motivatie_menu() -> None:
    """
    Motivatie-menu loop.
    Keuze 4 returnt terug naar het hoofdmenu (caller).
    """
    while True:
        print_motivatie_menu()
        keuze = vraag_menu_keuze("Selecteer je optie (1 - 4): ", 1, 4)

        if keuze == 1:
            categorie = "inspirational"
        elif keuze == 2:
            categorie = "courage"
        elif keuze == 3:
            categorie = "success"
        elif keuze == 4:
            return  # terug naar hoofdmenu

        # Toon eerste quote
        print(haal_quote_op(categorie))

        # Daarna actie-menu (nog een quote / andere categorie / terug)
        actie = keuze_actie_motivatie_menu(categorie)

        if actie == "andere_categorie":
            continue  # opnieuw motivatie-menu tonen
        elif actie == "terug_hoofdmenu":
            return


def keuze_actie_motivatie_menu(categorie: str) -> str:
    """
    Actie-menu na een quote.

    Returns:
        "nog_een" (blijft in dit menu),
        "andere_categorie" (terug naar motivatie-menu),
        "terug_hoofdmenu" (terug naar hoofdmenu).
    """
    while True:
        print_motivatie_actie_menu()
        keuze = vraag_menu_keuze("Selecteer je optie (1 - 3): ", 1, 3)

        if keuze == 1:
            print(haal_quote_op(categorie))
        elif keuze == 2:
            return "andere_categorie"
        elif keuze == 3:
            return "terug_hoofdmenu"


def haal_quote_op(categorie: str) -> str:
    """Haalt een quote op via API Ninjas en geeft een string terug."""
    headers = {"X-Api-Key": API_KEY_API_NINJAS}
    params = {"categories": categorie}

    try:
        response = requests.get(API_NINJAS_BASE_URL, headers=headers, params=params, timeout=10)
    except requests.RequestException as e:
        return f"Netwerkfout bij ophalen quote: {e}"

    if response.ok:
        data = response.json()
        if not data:
            return "Geen quote gevonden (lege response)."
        quote = data[0].get("quote", "")
        author = data[0].get("author", "Onbekend")
        return f"\nJouw quote ({categorie}):\n{quote} — {author}"

    return f"Er is iets misgegaan. Status code: {response.status_code}"


# ---------------------------
# Grap (placeholder)
# ---------------------------

def print_grap_menu() -> None:
    print(
        "\n😂 Tijd voor een glimlach\n"
        "Wat voor grap mag het zijn?\n\n"
        "1. Programmeer / nerdy grap\n"
        "2. Algemene grap\n"
        "0. Terug naar hoofdmenu\n"
    )


def keuze_grap_menu() -> None:
    """
    Placeholder: zodat je programma niet crasht.
    Later kun je hier je echte grap-API of graplogica bouwen.
    """
    while True:
        print_grap_menu()
        keuze = vraag_menu_keuze("Selecteer je optie (0 - 2): ", 0, 2)

        if keuze == 0:
            return

        # Tijdelijke grapjes:
        if keuze == 1:
            print("\n🤓 Waarom kunnen programmeurs niet liegen? Omdat ze altijd ‘True’ zeggen.\n")
        elif keuze == 2:
            print("\n😄 Wat zegt een muur tegen de andere muur? Zien we je bij de hoek!\n")

        # mini actie
        doorgaan = vraag_menu_keuze("Nog een grap? (1=ja, 0=nee): ", 0, 1)
        if doorgaan == 0:
            return


# ---------------------------
# To-do (placeholder)
# ---------------------------

def print_todo_menu() -> None:
    print(
        "\n🧠 Rust in je hoofd\n"
        "Dit onderdeel bouw je later verder.\n\n"
        "0. Terug naar hoofdmenu\n"
    )


def keuze_todo_menu() -> None:
    while True:
        print_todo_menu()
        keuze = vraag_menu_keuze("Selecteer je optie (0): ", 0, 0)
        if keuze == 0:
            return


# ---------------------------
# Main
# ---------------------------

def main() :
    keuze_hoofdmenu()

main()



