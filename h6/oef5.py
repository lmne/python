def main():
    aantal_volwassenen = int(input("geef hier het aantal volwassennen in : "))
    aantal_kinderen = int(input("geef hier het aantal kinderen in : "))
    hotel_codes = []
    while True:
        hotel_code = input("geef hier de hotel code in vb : (HI1234****): ")
        if hotel_code[0] != '/':
            hotel_codes.append(hotel_code)
            print("de waarde is ingegeven!")
        elif hotel_code[0] == '/':
            print("het invoeren is gestop \n")
            verwerken_waardens(hotel_codes, aantal_volwassenen, aantal_kinderen)
            break


def verwerken_waardens(list,volwassenen,kinderen):
    for x in range(len(list)):
        aantal_sterren = list.count('*')
        prijs_kinderen = 0
        prijs_volwassenen = 0
        prijs = 48
        if aantal_sterren >= 4:
            prijs = 60
        elif aantal_sterren == 3:
            prijs = 56
        if aantal_sterren <= 2:
            if controle_hotel(list[x]) == 60:


            elif controle_hotel(list[x]) == 70:
                prijs_volwassenen = volwassenen * 70
                prijs_kinderen = kinderen * 35
                print(f"{list[x]} {prijs_volwassenen} {prijs_kinderen} {prijs_volwassenen + prijs_kinderen}")

            elif controle_hotel(list[x]) == 0:
                prijs_volwassenen = volwassenen * 45
                prijs_kinderen = kinderen * 27.5
                print(f"{list[x]} {prijs_volwassenen} {prijs_kinderen} {prijs_volwassenen + prijs_kinderen}")

        elif aantal_sterren == 4:
            if controle_hotel(list[x]) == 60:
                prijs_volwassenen = volwassenen * 60
                prijs_kinderen = kinderen * 30
                print(f"{list[x]} {prijs_volwassenen} {prijs_kinderen} {prijs_volwassenen + prijs_kinderen}")

            elif controle_hotel(list[x]) == 70:
                prijs_volwassenen = volwassenen * 70
                prijs_kinderen = kinderen * 35
                print(f"{list[x]} {prijs_volwassenen} {prijs_kinderen} {prijs_volwassenen + prijs_kinderen}")

            elif controle_hotel(list[x]) == 0:
                prijs_volwassenen = volwassenen * 56
                prijs_kinderen = kinderen * 28
                print(f"{list[x]} {prijs_volwassenen} {prijs_kinderen} {prijs_volwassenen + prijs_kinderen}")

            if aantal_sterren <= 5:

                if controle_hotel(list[x]) == 70:
                    prijs_volwassenen = volwassenen * 70
                    prijs_kinderen = kinderen * 35
                    print(f"{list[x]} {prijs_volwassenen} {prijs_kinderen} {prijs_volwassenen + prijs_kinderen}")

                elif controle_hotel(list[x]) == 0 or 60:
                    prijs_volwassenen = volwassenen * 60
                    prijs_kinderen = kinderen * 30
                    print(f"{list[x]} {prijs_volwassenen} {prijs_kinderen} {prijs_volwassenen + prijs_kinderen}")


def controle_hotel (variabel):
    if (variabel[0:2]) == 'BR':
        return 60
    elif (variabel[0:2]) == 'AN':
        return 60
    elif (variabel[0:2]) == 'HI':
        return 70
    else:
        return 0


if __name__ == '__main__':
    main()

