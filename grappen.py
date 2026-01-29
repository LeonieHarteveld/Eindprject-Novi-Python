from algemene_functies import vraag_menu_keuze
from menus import print_grap_menu

def keuze_grap_menu():

    while True:
        print_grap_menu()
        keuze = vraag_menu_keuze("Selecteer je optie (1 - 3): ", 1, 3)

        if keuze == 1:
            pass

        elif keuze == 2:
            pass

        elif keuze == 3:
            break
