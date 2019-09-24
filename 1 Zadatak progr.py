#Napravi program koji unosi rijeci sve dok se dva puta zaredom ne unese ista rijec i formira rjecnik ciji su kljucevi prva slova
#unesenih rijeci a vrijednosti broj rijeci koje pocinju s tim slovom. Nakon toga ispisi string sastavljen od kljuceva rjecnika cija 
#je vrijednost veca od 2

def main():
  rijeci = []
  zadnja_rijec = " "
  ponovljena = False
  while ponovljena != True:
    rijec = input("Unesi rijec:")
    rijeci.append(rijec)
    if rijec == zadnja_rijec:
      ponovljena = True
    else:
      zadnja_rijec = rijec
  rjecnik = formiraj_rjecnik(rijeci) 
  string = ""
  for k, v in rjecnik.items():
    if v >= 2:
      string += " " + k
  print(string)
def brojrijecisapocetnimslovom(slovo, niz):
  counter = 0
  for rijec in niz:
    if rijec[0] == slovo:
      counter = counter + 1
  return counter
def formirajrjecnik(rijeci):
  novi_rjecnik = {}
  for rijec in rijeci:
    novi_rjecnik[rijec[0]] = brojrijecisapocetnimslovom(rijec[0], rijeci)
  return novi_rjecnik
if _ _name_ _ == "_ _main_ _":
  main()