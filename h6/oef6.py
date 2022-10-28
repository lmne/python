def main ():
    hoogte_poort = int(input("geef hier de hoogte van de poort in tussen 2 en 6.5m in : "))
    if 2<= hoogte_poort >=6.5:
        print("de waarde is correct")
    else:
        print("de waarde valt niet tussen de gegeven waardes")
    breedte_poort = int(input("geef hier de breedte van de poort in tussen 2 en 8m in : "))
    if 2 <= breedte_poort >= 8:
        print("de waarde is correct")
    else:
     print("de waarde valt niet tussen de gegeven waardes")
    oppervlakte = oppervlakte_poort(hoogte_poort, breedte_poort)
    gewicht = gewicht_poort(oppervlakte)
    genereren_offerte_nummer(totale_prijs(oppervlakte,  bepalen_motortype(gewicht)))

    print(oppervlakte, gewicht)




def oppervlakte_poort(lengte,breedte):
    opervlakte = lengte*breedte
    return opervlakte

def gewicht_poort (oppervlakte):
    gewicht = oppervlakte * 11
    return gewicht

def bepalen_motortype (gewicht_ijzer):
    if gewicht_ijzer < 150:
        return 120
    elif gewicht_ijzer >= 150 <= 300:
        return 220.5
    else:
        return 250.5

def totale_prijs (opper_vlakte, prijs_motor):
    prijs_totaal = opper_vlakte * 113.5 + prijs_motor
    return prijs_totaal

def genereren_offerte_nummer(prijs_totaal):
    naam_verkoper = input("geef hier de naam van de verkoper in : ")
    naam_verkoper.upper()
    offerte_nummer_nogd = f"2022_{naam_verkoper}_{prijs_totaal}"
    offerte_nummer_Af = offerte_nummer_nogd[::-1]
    print(f"{prijs_totaal} is {offerte_nummer_Af.upper()}")



if __name__ == '__main__':
    main()