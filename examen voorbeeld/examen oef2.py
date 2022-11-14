import random


def main():
    aantal_getallen = int(input("geef het aantal getallen in : "))
    lijst = [0] * aantal_getallen
    veelvoud = int(input("geef het veelvoud in : "))
    for i in range(aantal_getallen):
        randomgetal = random.randint(0,101)*veelvoud
        if randomgetal >= 0 and randomgetal >= 100:
            lijst[i] = randomgetal
        else:
            i = i - 1
    print(lijst)


if __name__ == '__main__':
    main()
