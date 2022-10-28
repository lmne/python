lengte = float(input("geef de lente van tapijt in meter: "))
breedte = float(input("geef de breedte van de tapijt in meter: "))
prijs_tapijt = float(input("geef de prijs per m2 van het tapijt: "))
prijs_plaatsing = float(input("geef de prijs van de plaatsing per m2: "))

oppervlakte = lengte * breedte
prijs_tapijt = oppervlakte * prijs_tapijt
print("prijs tapijt: " , prijs_tapijt)
prijs_plaats= oppervlakte * prijs_plaatsing
print("de prijs voor de plaatsing: ", prijs_plaats)
prijs_totaal = prijs_tapijt + prijs_plaats
print("de totale prijs is: ", prijs_totaal)