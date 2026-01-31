import sys
from operator import itemgetter
import requests
from algemene_functies import vraag_menu_keuze
from menus import print_hoofdmenu
from motivatie import keuze_motivatie_menu
from grappen import keuze_grap_menu
from todo import keuze_to_do_list

from api_keys import API_KEY_API_NINJAS, API_NINJAS_BASE_URL



def main():
    while True:
        print_hoofdmenu()
        keuze = vraag_menu_keuze("Selecteer je optie (1 - 4): ", 1, 4)

        if keuze == 1:
            resultaat = keuze_motivatie_menu()
            if resultaat == "Hoofdmenu":
                continue

        elif keuze == 2:
            keuze_grap_menu()
        elif keuze == 3:
            keuze_to_do_list()
        elif keuze == 4:
            print("Tot Ziens! 👋")
            break

main()
