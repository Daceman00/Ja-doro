# Napravi program koji za uneseni broj n, koristenjem rekurzivne funkcije, racuna sumu svih neparnih pozitivnih brojeva manjih ili
#jednakih n

def main():
  broj = int(input("Unesi prirodni broj:"))
  print("Suma = " + str(izracunajsumuneparnih(broj)))
def izracunajsumuneparnih(n):
  if n != 0:
    if n % 2 == 1:
      return n + izracunajsumuneparnih(n - 1)
    else:
      return izracunajsumuneparnih(n - 1)
  else:
    return n
if _ _name_ _ == "_ _main_ _":
  main()