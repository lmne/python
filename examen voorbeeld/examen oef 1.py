""""
Schrijf een programma voor onderstaande opgave:
Op basis van een weersvoorspelling wordt beslist of een klas van het derde leerjaar op
tweedaagse gaat, op daguitstap gaat of helemaal niet op uitstap vertrekt.
De temperatuur (gehele getallen) en hoeveelheid neerslag (overvloed - veel – matig – geen)
worden ingelezen van het toetsenbord.
Opm: Je mag ervan uitgaan dat de gebruikers van je programma geen verkeerde invoer
ingeven, je moet dus geen invoercontrole uitvoeren.
Er zijn 7 dagen nodig (niet meer) om een voorspelling te maken.
Maar de invoer stopt ook wanneer voor regen “overvloed” ingegeven wordt.
Dan wordt er helemaal niet op uitstap vertrokken (dit is dus de voorwaarde om niet op uitstap
te vertrekken).
De voorwaarden om op tweedaagse te gaan zijn:
* de laagste temperatuur is minimaal 15 graden
* de laagste temperatuur moet groter zijn dan 20% van de gemiddelde temperatuur
* geen enkele dag mag voor regen “veel” ingegeven zijn
Als output willen we een overzicht van de dagen met daarbij de ingegeven temperatuur en
hoeveelheid neerslag.
Alsook de conclusie van welke uitstap er gemaakt wordt.
"""
def main():
    GROOTTE = 7
    matrix = []
    counter = 1
    for i in range(GROOTTE):
        matrix.append(GROOTTE * [''])

    matrix[0][0] = 'dag'
    matrix[0][1] = 'temperatuur'
    matrix[0][2] = 'neerslag'

    while counter < 7:
        invoer_regen = input("geef hier de regen in : ")
        if invoer_regen == 'overvloed':
            break
        else:
            matrix[counter][2] = invoer_regen
            matrix[counter][1] = input("geef hier de temperatuur in")
            matrix[counter][0] = str(counter)
            counter = counter + 1
    if laagste_temperatuur(matrix) == int(0):
        print_matrix(matrix)
        print("we gaan niet")
    else:
        print_matrix(matrix)
        print("we gaan wel")


def print_matrix(array):
    for i in range(7):
        for j in range(7):
            print(array[i][j], end=" ")
        print()

def laagste_temperatuur(array):
    lijst_temp = []
    for x in range(7):
        lijst_temp[x] = int(array[x][1])
    laagste_waarde = min(array)
    if laagste_waarde < 15:
        return 0
    gemiddelde = ((sum(array)/7)/100)
    for y in range(7):
        if lijst_temp[y] < (gemiddelde*20):
            return 0
    aantal_veel = array.count('veel')
    if aantal_veel > 0:
        return 0






if __name__ == '__main__':
    main()

