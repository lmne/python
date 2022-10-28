""""
Maak een programma om het juiste sterrenbeeld van meerdere personen af te drukken.
Geef de naam, de voornaam en de geboortedatum van de persoon in. De geboortedatum geef
je in in het formaat dd/mm/yyyy (bijv. 15/05/1999).
De invoer stopt wanneer voor de naam een “/” wordt ingegeven.
De sterrenbeelden zijn (in volgorde van de maanden van het jaar): waterman, vissen, ram,
stier, tweelingen, kreeft, leeuw, maagd, weegschaal, schorpioen, boogschutter, steenbok.
We gaan er van uit dat telkens de 21ste van de maand een nieuw sterrenbeeld begint. Dus
wie jarig is tussen 21 januari en 20 februari is een waterman, wie jarig is tussen 21
februari en 20 maart heeft als sterrenbeeld vissen, …
Het bepalen van het juiste sterrenbeeld moet met een functie gebeuren.
Voor elke persoon moet de eerste letter van de voornaam gevolgd door een punt gevolgd
door de achternaam (dit alles in hoofdletters) afgedrukt worden. Het afdrukken van de naam van een persoon dient te gebeuren in een functie.
Bv.: Hans Andersen geboren op 3/2 geeft: H. ANDERSEN waterman
"""
def main():
    opvragengeg()



def opvragengeg():
    y = 0
    arr = [[] * 2] * y
    while True:
        invoer = input("geef hier de voor en achter naam in (vb lamine guisse) : ")
        if invoer != '/':
            arr[0][y] = invoer
            arr[1][y] = input("geef hier de geboortedatum in  (vb 15/05/1999) : ")
            y = y+1
        else:
            print(arr)
            break



if __name__ == '__main__':
    main()
