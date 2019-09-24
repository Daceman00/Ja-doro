# A.2
# Napravi program koji unosi tekst i zatim, korištenjem n-torki i rjeènika 
# ispisuje sve znakove koji se ponavljaju bar 3 puta, sortirane silazno po 
# broju ponavljanja

tekst = str(input("Unesi tekst:"))
rjecnik = {}

for i in tekst:
    rjecnik[i] = rjecnik.get(i, 0) + 1
print(rjecnik)

ponavljanja = []
for r in rjecnik:
    ponavljanja.append ((rjecnik[r], r))
print(ponavljanja)

ponavljanja.sort()
print(ponavljanja)

print("Znakovi koji se ponavljaju bar 3 puta")
for p in ponavljanja:
    if p[0] >= 3:
        print(p[1])
        
    


    

    

