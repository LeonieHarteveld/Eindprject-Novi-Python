from operator import itemgetter
from algemene_functies import vraag_menu_keuze
from menus import print_todo_menu

to_do_lijst = []

def get_list ():
    for taak in to_do_lijst:
        print(
            f"Taak : {taak["taak"]}\n"
            f"Prioriteit: {taak["prioriteit"]}\n"
            f"Stressniveau: {taak["stressniveau"]}\n"
            f"{'-' * 30}"

        )

def sort_list (soort:str):
    to_do_lijst.sort(key=itemgetter(soort), reverse=True)


def keuze_to_do_list ():
    while True:
        print_todo_menu()
        keuze = vraag_menu_keuze("Selecteer je optie: (0 - 5): ", 0,5)

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
            print("-" * 30)

        elif keuze == 2:
            if not to_do_lijst:
                print("Je to-do lijst is leeg")
            else:
                get_list()

        elif keuze == 3:
            if not to_do_lijst:
                print("Je to-do lijst is leeg")
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
                print("Je to-do lijst is leeg")
            else:
                sort_list("prioriteit")
                get_list()


        elif keuze == 5:
            if not to_do_lijst:
                print("Je to-do lijst is leeg")
            else:
                sort_list("stressniveau")
                get_list()

        elif keuze == 0:
            break


