from operator import itemgetter
from algemene_functies import vraag_menu_keuze
from menus import print_todo_menu
import sys

to_do_lijst = []

def value_error ():
    """
    :return: Print een foutmelding naar stderr wanneer de gebruiker
    een ongeldige invoer geeft.
    """
    print("Ongeldige invoer. Gebruik alleen cijfers.", file=sys.stderr)

def juiste_invoer (min_keuze: int, max_keuze: int ):
    """
    :param min_keuze: Ondergrens van toegestane invoer.
    :param max_keuze: Bovengrens van toegestane invoer.
    :return: Print dat de gebruiker een getal moet invoeren binnen een bepaald bereik.
    """
    print(f"Voer een getal in tussen {min_keuze} en {max_keuze}.")

def lege_to_do_list ():
    """
    :return: Print dat de to-do lijst leeg is.
    """
    print("Je to-do lijst is leeg")


def get_list ():
    """
    :return: Print de taken, prioriteit en stressniveau op de lijst.
    """
    for taak in to_do_lijst:
        print(
            f"{'-' * 30}"
            f"\nTaak : {taak["taak"]}\n"
            f"Prioriteit: {taak["prioriteit"]}\n"
            f"Stressniveau: {taak["stressniveau"]}"
        )

def sort_list (soort:str):
    """
    :param soort: "prioriteit" of "stressniveau"
    :return: Sorteert de to-do lijst aflopend op basis van prioriteit of stressniveau
    """
    to_do_lijst.sort(key=itemgetter(soort), reverse=True)


def keuze_to_do_list ():
    """

    :return: Start het to-do menu, blijft actief totdat de gebruiker kiest voor afsluiten
    """

    while True:
        print_todo_menu()
        keuze = vraag_menu_keuze("Selecteer je optie: (0 - 5): ", 0,5)

        if keuze == 1:
            taak = input("Voer de uit te voeren taak in: ")
            while True:
                try:
                    prioriteit = int(input("Hoe hoog is de prioriteit (1 - 5): "))
                    if 1 <= prioriteit <= 5:
                        break
                    else:
                        juiste_invoer (1, 5)
                except ValueError:
                    value_error()

            while True:
                try:
                    stressniveau = int(input("Hoe hoog is het stressniveau (1 - 5): "))
                    if 1 <= stressniveau <= 5:
                        break
                    else:
                        juiste_invoer(1, 5)
                except ValueError:
                     value_error ()

            to_do_lijst.append( {
                "taak": taak,
                "prioriteit": prioriteit,
                "stressniveau": stressniveau
            })

            print(f'"{taak}" is toegevoegd aan de to do lijst')
            print("-" * 30)

        elif keuze == 2:
            if not to_do_lijst:
                lege_to_do_list()
            else:
                get_list()

        elif keuze == 3:
            if not to_do_lijst:
                lege_to_do_list ()
            else:
                taak_verwijderen = input("Welke taak wil je verwijderen?: ")

                for taak in to_do_lijst:
                    if taak["taak"].lower() == taak_verwijderen.lower():
                        to_do_lijst.remove(taak)
                        print(f'\nTaak "{taak_verwijderen}" is verwijderd\n'
                              f"{'-' * 30}")
                        break
                else:
                    print("Taak niet gevonden")


        elif keuze == 4:
            if not to_do_lijst:
                lege_to_do_list ()
            else:
                sort_list("prioriteit")
                get_list()


        elif keuze == 5:
            if not to_do_lijst:
                lege_to_do_list ()
            else:
                sort_list("stressniveau")
                get_list()

        elif keuze == 0:
            break

