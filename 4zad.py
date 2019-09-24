#Napravi program koji za uneseni niz brojeva, koristenjem rekurzivne funkcije, provjerava radi li se o Fibonaccijevom nizu, te vraca 
#logicku (true/false) vrijednost (Fibanccijev niz: 1,1,2,3,5,8,...,F(1)=F(2)=1,f(n)=F(n-1)+F(n-2))

def F(n):
  if n==1:
    return 1
  elif n==2:
    return 1
  else:
    return F(n-1) + F(n-2)
n=26
if F(n):
  return 1
else:
  return 0