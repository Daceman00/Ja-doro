kapacitet = (12,8,5)
x = kapacitet[0]
y = kapacitet[1]
z = kapacitet[2]
rjecnik = {}
lista = []
def sve_kombinacije(komb):
  a = komb[0]
  b = komb[1]
  c = komb[2]

  if(a==6 and b==6):
      lista.append(komb)
      return True
    
  if((a,b,c) in rjecnik):
      return False

  rjecnik[(a,b,c)] = 1

  if(a>0):
      if(a+b<=y):
          if( sve_kombinacije((0,a+b,c)) ):
              lista.append(komb)
              return True
      else:
          if( sve_kombinacije((a-(y-b), y, c)) ):
              lista.append(komb)
              return True
      if(a+c<=z):
          if( sve_kombinacije((0,b,a+c)) ):
              lista.append(komb)
              return True
      else:
          if( sve_kombinacije((a-(z-c), b, z)) ):
              lista.append(komb)
              return True
            
  if(b>0):
      if(a+b<=x):
          if( sve_kombinacije((a+b, 0, c)) ):
              lista.append(komb)
              return True
      else:
          if( sve_kombinacije((x, b-(x-a), c)) ):
              lista.append(komb)
              return True
      if(b+c<=z):
          if( sve_kombinacije((a, 0, b+c)) ):
              lista.append(komb)
              return True
      else:
          if( sve_kombinacije((a, b-(z-c), z)) ):
              lista.append(komb)
              return True

  if(c>0):
      if(a+c<=x):
          if( sve_kombinacije((a+c, b, 0)) ):
              lista.append(komb)
              return True
      else:
          if( sve_kombiinacije((x, b, c-(x-a))) ):
              lista.append(komb)
              return True
      if(b+c<=y):
          if( sve_kombinacije((a, b+c, 0)) ):
              lista.append(komb)
              return True
      else:
          if( sve_kombinacije((a, y, c-(y-b))) ):
              lista.append(komb)
              return True

  return False

pocetna_komb = (12,0,0)
print("Pocetak ...")
sve_kombinacije(pocetna_komb)
lista.reverse()
for i in lista:
  print(i)
