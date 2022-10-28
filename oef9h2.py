bedrag = int(input("geef hier het bedrag in in cent : "))
aantal_2euro = bedrag//200
rest = bedrag % 200
print("2euro munten",aantal_2euro)
print("rest",rest)
aantal_1euro = rest //100
print("1euro munten",aantal_1euro)
rest%=100
print("rest",rest)
#...... dit herhalen
