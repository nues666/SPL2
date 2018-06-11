zahl1 = input("Bitte Zahl 1 eingeben: ") 
zahl2 = input("Bitte Zahl 2 eingeben: ") 
zahl3 = input("Bitte Zahl 3 eingeben: ") 

if(zahl1 < zahl2 <zahl3 ):
    print(zahl1, zahl2, zahl3)

if(zahl1 < zahl2 <zahl2 ):
    print(zahl1, zahl2, zahl3)

if(zahl2 < zahl1 <zahl3 ):
    print(zahl2, zahl1, zahl3)

if(zahl2 < zahl3 <zahl1 ):
    print(zahl2, zahl3, zahl1)

if(zahl3 < zahl2 <zahl1 ):
    print(zahl3, zahl2, zahl1)

if(zahl3 < zahl1 <zahl2 ):
    print(zahl3, zahl1, zahl2)
