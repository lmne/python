
def main():
    text_variabele1 = input("geef hier je eerste variabele in :")
    text_variabele2 = input("geef hier je tweede variabele in :")
    print(controle_eerste_variabelen(text_variabele1))
   # controle_tweede_variabelen(text_variabele2)




def controle_eerste_variabelen(variabele_1):
    lengte_string = len(variabele_1)
    if lengte_string < 4:
        variabele_1 += "*"
    else:
        variabele_1 = variabele_1[0, 3]
        variabele_1.upper()
        return variabele_1


#def controle_tweede_variabelen(variabele_2):


if __name__ == '__main__':
    main()

