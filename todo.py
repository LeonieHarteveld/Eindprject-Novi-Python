from operator import itemgetter
from algemene_functies import vraag_menu_keuze
from menus import print_todo_menu

to_do_lijst = []

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
            print("-" * 50)

        elif keuze == 2:
            if not to_do_lijst:
                print("Je to-do lijst is leeg")
            else:
                for taak in to_do_lijst:
                    print(
                        f"Taak : {taak["taak"]}\n"
                        f"Prioriteit: {taak["prioriteit"]}\n"
                        f"Stressniveau: {taak["stressniveau"]}\n"
                        f"{'-' * 50}"
                    )

        elif keuze == 3:
            if not to_do_lijst:
                print("Je to-do lijst is leeg")
            else:
                taak_verwijderen = input("Welke taak wil je verwijderen?: ")

                for taak in to_do_lijst:
                    if taak["taak"].lower() == taak_verwijderen.lower():
                        to_do_lijst.remove(taak)
                        print(f'Taak "{taak_verwijderen}" is verwijderd')
                        break
                else:
                    print("Taak niet gevonden")


        elif keuze == 4:
            if not to_do_lijst:
                print("Je to-do lijst is leeg")
            else:
                to_do_lijst.sort(key=itemgetter("prioriteit"), reverse=True)

                for taak in to_do_lijst:
                    print(
                        f"Taak : {taak["taak"]}\n"
                        f"Prioriteit: {taak["prioriteit"]}\n"
                        f"Stressniveau: {taak["stressniveau"]}\n"
                        f"{'-' * 50}"

                    )

        elif keuze == 5:
            if not to_do_lijst:
                print("Je to-do lijst is leeg")
            else:
                to_do_lijst.sort(key=itemgetter("stressniveau"), reverse=True)

                for taak in to_do_lijst:
                    print(
                        f"Taak : {taak["taak"]}\n"
                        f"Prioriteit: {taak["prioriteit"]}\n"
                        f"Stressniveau: {taak["stressniveau"]}\n"
                        f"{'-' * 50}"

                    )

        elif keuze == 6:
            break