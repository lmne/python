"""""
Er worden via het toetsenbord 10 getallen ingelezen. Schrijf een programma dat de positieve getallen toevoegt in een
list met de naam positieve_getallen en de strikt negatieve getallen toevoegt in een list met de naam negatieve_getallen.
Druk de lengte en de waarden van beide lists af.
Bepaal het kleinste getal van de list negatieve_getallen
"""""

def main():
    lijst_pos = []
    lijst_neg = []
    for x in range(1,11):
        getal_invoer = int(input(f"geef hier getal {x} in :"))
        if getal_invoer <0:
            lijst_neg.append(getal_invoer)
        else:
            lijst_pos.append(getal_invoer)
    print(lijst_neg)
    print(len(lijst_neg))
    print(f"kleinste getal in de lijst is : {min(lijst_neg)}")
    print(lijst_pos)
    print(len(lijst_pos))

if __name__ == '__main__':
    main()

