#Creëer een list met 500 elementen waarbij de elementen willekeurige gehele getallen
#zijn tussen 0 en 10000 (beiden inclusief).
#Als er minder dan de helft (250 elementen) van de getallen groter zijn dan 5000, dan tel je alle elementen van de list die groter zijn dan 5000 op en druk het resultaat van deze optelling af.
#Als er 250 of meer getallen groter zijn dan 5000, dan tel je alle elementen van de list die groter zijn dan 8000 op en drukt dit resultaat af.
import random
def main():
    array_lijst = random.sample(range(0, 10000), 500)
    print(array_lijst)
    print( optellen(array_lijst))

def optellen (lijst):
    optelling = 0
    getallen_kleinerdan = sum(i > 5000 for i in lijst)
    if getallen_kleinerdan < 250:
        for i in lijst:
            if i < 5000:
                optelling = optelling + i
        print("kleiner dan 250")
    else:
        for i in lijst:
            if i > 8000:
                optelling = optelling + i
        print("groter dan 250")
    return optelling


if __name__ == '__main__':
    main()
