#A.1
# Napravi program koji unosi tekst i zatim, korištanjem rjeènika, ispisuje
# one znakove koji su se ponovili više od  4 puta, i to onliko puta koliko 
# su se ponovili
tekst = str(input("Unesi tekst"))
rjecnik = {}

for i in tekst:
    rjecnik[i] = rjecnik.get(i, 0) + 1
print(rjecnik)

print("Znakovi koji su se pojavili vise od 4 puta")    
for r in rjecnik:
    if rjecnik[r] > 4:
        for i in range(rjecnik[r]):
            print(r)
           
        
      
        
        
            
             
        
