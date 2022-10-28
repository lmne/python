try:
    getal_invoer = int(input("geef hier een getal in tussen 1 en 100 : "))
    if getal_invoer <100 & getal_invoer>1:
        print("u heeft een geldig getal in gegeven !")
    else:
        print("het getal dat u heeft in gegeven is niet tussen 1 en 100")

except:
    print("het was geen geldig karakter!!")