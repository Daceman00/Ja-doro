op = 0
brojac = 0

while True:
    op = input("Unesi zeljenu operaciju 1,2 i 3:")

    if op == 1:
        r = input("Unesi radijus:")
        opseg = (r*r*3.14)
        print("Povrsina kruga je:", opseg)
        brojac += 1
    
    elif op == 2:
        s = input("Unesi stranicu:")
        vis_trokuta = 3/2*s
        print("Visina jednakostranicnog trokuta:", vis_trokuta )
        brojac += 1

    elif op == 3:
        a = input("Unesi duljinu 1. stranice:")
        b = input("Unesi duljinu 2. stranice:")
        obujam = a*b*2
        print("Obujam prostora:", obujam)
        brojac += 1
    elif op == 0:
        break
    
import datetime
x = datetime.datetime.now()
print(x)
print("Broj pokusaja", brojac)
        
    
    



    



    
