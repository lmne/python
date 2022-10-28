lijst_temp = []
for x in range(1,11):
    lijst_temp.append(int( input(f"geef hier de temp in van dag {x} : ")))
for x in range(len(lijst_temp)):
    print (lijst_temp[x])
gemiddelde_temp = sum(lijst_temp)/10
print("de hoogste temperatuur van deze 10 dagen is : ",max(lijst_temp))
print(f"de gemiddelde temperatuur is {gemiddelde_temp}")
