""""
Schrijf een programma om de verkiezingsresultaten van de verkiezing “student van het
jaar” te verwerken. Er zijn 4 kandidaten waarop men kan stemmen. Via het toetsenbord
wordt de keuze van een aantal personen ingegeven. De keuze is de code van de student
waarvoor men stemt. De invoer stopt wanneer voor de keuze de waarde 0 wordt
ingegeven.
+ code 1: An Janssen + code 2: Bart Vriends + code 3: Andries Michels + code 4: Inge Kaas
Druk per kandidaat de naam, het aantal personen dat voor deze kandidaat gestemd heeft
en het procentueel aandeel van de gekregen stemmen in het totaal aantal uitgebrachte
stemmen af. Het procentueel aandeel wordt weergegeven met 1 cijfer na de komma.
"""

def main():
    stem_an = 0
    stem_bart = 0
    stem_andries = 0
    stem_inge = 0
    while True:
        code = int(input("geef hier de code in : "))
        if code == 0:
            break
        elif code == 1 :
            print("gekozen voor an")
            stem_an = stem_an + 1
        elif code == 2:
            print("gekozen voor bart")
            stem_bart = stem_bart + 1
        elif code == 3:
            print("gekozen voor andries")
            stem_andries = stem_andries + 1
        elif code == 4:
            print("gekozen voor inge")
            stem_inge = stem_inge + 1
    print(f"stemmen an = {stem_an}")
    print(f"stemmen bart = {stem_bart}")
    print(f"stemmen andries = {stem_andries}")
    print(f"stemmen inge = {stem_inge}")


if __name__ == '__main__':
    main()