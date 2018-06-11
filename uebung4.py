# uebung4.py

import random

zahlen = []
anzahlWuerfe = int(input("Wie oft soll gewürfelt werden?"))

for i in range (0, anzahlWuerfe):
    wurf = random.randint(1,37)
    zahlen.append(wurf)
    #print(wurf, end="..." )

print ()
print("Ergebnis: ")
#print (zahlen)
for i in range(1,37):
    print(i,"er: ",zahlen.count(i))    

