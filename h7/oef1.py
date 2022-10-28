#Geef 15 gehele getallen in via het toetsenbord.
#Druk het gemiddelde af weergegeven met 1 cijfer na de komma.
#Hoeveel getallen zijn er kleiner dan het gemiddelde van deze 15 getallen?
#Hoeveel procent is dit van de ingegeven getallen?

def main():
    lijst_getallen = []
    aantal_opvragen = 10
    print(f"opvragen van {aantal_opvragen} getallen")
    for x in range(0, aantal_opvragen):
        invoer_getal = int(input(f"geef hier getal {x+1} in : "))
        lijst_getallen.append(invoer_getal)
    print(f"het gemiddlde van de getallen is {gemiddelde(lijst_getallen)}")
    getallen_kleinerdangem = getal_kleiner(lijst_getallen, gemiddelde(lijst_getallen))
    print(f"aantal getallen kleiner dan gemiddeld : {getallen_kleinerdangem}")
    print(percentage(getallen_kleinerdangem, aantal_opvragen))

    print(lijst_getallen)


def gemiddelde(lijst):
    return sum(lijst) / len(lijst)

def getal_kleiner(lijst, gem):
    getallen_kleinerdan = sum(i > gem for i in lijst)
    return getallen_kleinerdan

def percentage (aantal_onder , aantal_tot):
    percent = ((aantal_onder / aantal_tot) * 100)
    return percent


if __name__ == '__main__':
    main()
