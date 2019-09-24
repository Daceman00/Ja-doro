#Program unosi recenicu i, koristeci regularni izraz, ispisuje rijeci(niz znakova odvojenih razmakom) koje u sebi sadrze neki znak koji
#nije dio engleskog alfabeta

import re
recenica = input("Unesi recenicu")
rez = re.findall("[A-Za-z]*[šćßžŁ]+[A-Za-z]*", recenica)
print(rez)
