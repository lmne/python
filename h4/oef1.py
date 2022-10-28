gewicht_appel = int(input("geef hier het gewicht van de appel in : "))
for x in range (1,101):
    print(x,"appel(s) = ",x*gewicht_appel,"gr.")
y=1
#di is de extra while opdracht
while y <= 100:
    print(y, "appel(s) = ", y * gewicht_appel, "gr.")
    y+= 1
