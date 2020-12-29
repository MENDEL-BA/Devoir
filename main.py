from random import randint
nombre_aleatoire=randint(0,50)


while True :
        try:
            nom=input("Donner votre nom:\t")
            while(nom.isspace()):
               nom=input("Donner votre nom:\t")
            break
        except:
            print("Veuillez entrer un nombre !")


while True:
        try:
            numero=int(input("Entrer une valeur coprise entre 0 et 50:\t"))
            break
        except:
            print("Veuillez entrer un nombre !")



while 0<numero>50:
        try:
            numero=int(input("vous devez saisir une valeur comprise entre 0 et 50:\t"))
            if 0<numero>50 :
              continue;
        except:
            print("Veuillez entrer un nombre !")

while True:
        try:
            miser=int(input("Entrer votre mise :\t"))
            break
        except:
            print("Veuillez entrer un nombre !")

print("======== Resultat =========")

if numero == nombre_aleatoire :
  print(f"MR. {nom} vous avez gagner le double de votre mise  {numero*2}")

elif (numero%2==0 and nombre_aleatoire % 2 == 0 ) or (numero % 2 != 0 and nombre_aleatoire % 2 != 0 ):
   print(f"MR. {nom} vous avez gagner la moitié de votre mise {numero/2}")

else :
  print(f"MR. {nom} vous n'avez pas gagner")

print(f"le nombre aleatoire est \t{nombre_aleatoire}")
print(f"========END Resultat=========")