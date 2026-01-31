import sys

# Algemene functies

def vraag_menu_keuze(vraag: str, min_keuze: int, max_keuze: int):
    """ Vraagt de input en vangt error's op

    params: vraag(str): De keuze die de gebruiker kan maken in het menu
            min_keuze(int): Minimal keuze
            max_keuze(int): Maximale keuze

    Returns: keuze
    """
    while True:
        try:
            keuze = int(input(vraag))
            if min_keuze <= keuze <= max_keuze:
                return keuze
            print(f"Kies een getal tussen {min_keuze} en {max_keuze}: \n")
        except ValueError:
            print(f"Voer een geldig getal in ({min_keuze} - {max_keuze}): ", file=sys.stderr)