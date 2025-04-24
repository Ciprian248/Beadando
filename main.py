from Legitarsasag import Legitarsasag
from JegyFoglalas import Jegyek

while True:
            print("1. Járat hozzáadása")                     #Főmenüben lévő opciók kiírása (a Járat hozzáadása admin lehetőség de nem rejtettem el, hogy könnyebb legyen a tesztelés)
            print("2. Jegy foglalása")
            print("3. Foglalás lemondása")
            print("4. Foglalások listázása")
            print("5. Járatok listázása")
            print("6. Kilépés")

            choice = input("Válasz a fenti menüpontok közül: ")

            if choice == "1":
                legitarsasag = Legitarsasag(input("Add meg a légitársaság nevét:"))                   #A választás után ahol kell a szükséges adatok bekérése a felhasználótól
                legitarsasag.jaratHozzaadas(input("Add meg a járatszámot:"),input("Add meg az indulási helyet(Ország Város formátumba):"),input("Add meg a célállomást(Ország Város formátumba):"),input("Add meg a jegyárat:"))
            
            elif choice == "2":
                foglalas = Jegyek()
                foglalas.jegyFoglalas(input("A jegy foglaláshoz előbb add meg a nevedet:"),input("Add meg a járatszámot:"), input("Utazás időpontja(éééé.hh.nn):"))

            elif choice == "3":
                foglalas = Jegyek()
                foglalas.foglalasLemondas(input("A foglalás lemondáshoz előbb add meg a nevedet:"),input("Add meg a járatszámot:"), input("Utazás időpontja(éééé.hh.nn):"))

            elif choice == "4":
                foglalas = Jegyek()
                foglalas.foglalasokListazasa()

            elif choice == "5":
                try:
                    f = open("BelföldiJáratok.txt", "r")                       #Megnyitja a BelföldiJáratok file-t
                    y = f.readlines()
                    print("Belföldi járatok: \n")
                    for line in y:                                             #Végigmegy rajta és sorról sorra kiírja
                        print(line)
                    f.close()

                    f = open("NemzetköziJáratok.txt", "r")                     #Megnyitja a NemzetköziJáratok file-t
                    y = f.readlines()
                    print("Nemzetközi járatok: \n")
                    for line in y:                                             #Végigmegy rajta és sorról sorra kiírja
                        print(line)
                    f.close()
                except:
                    print("Nem található járat!")

            elif choice == "6":
                break