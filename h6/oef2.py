def main():
    print("zin omdraaien oefening")
    zin = input("geef hier een zin in die omgedraaid moet worden : ")
    zinomdraaien(zin)
    print(zinomdraaien(zin))

def zinomdraaien(zin) :
    nieuwe_zin = zin [::-1]
    return nieuwe_zin


if __name__ == '__main__':
    main()

