#Program unosi recenicui, koristeci regularni izraz, ispisuje one rijeci(niz velikih i malih slova) koje pocinju i zavrsava


import re
def main():
  recenica = input("Unesi recenicu: ")
  rijeci = re.sub("[^\w]" , " " , recenica).split()
  print(rijecisasamoglasnicima(rijeci))
def rijecsasamoglasnikom(rijec):
  rijec = rijec.lower()
  if re.match(r"\b[aeiou] (\w*[aeiou])?\b" , rijec) and len(rijec) >= 3:
    return True
  else:
    return False
def rijecisasamoglasnicima(rijeci):
  niz = []
  for rijec in rijeci:
    if(rijecsasamoglasnikom(rijec)):
      niz.append(rijec)
  return niz
if _ _ name _ _ == "_ _ main _ _":
  main()