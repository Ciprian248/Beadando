class Jegyek():

    def __init__(self):
        pass

    def jaratEllenorzes(self,jarat,idopont):
        egyezik = False
        letezik = False
        try:
            ev = int(idopont[0:4])                                                                                          #Átkonvertálja int típusba az év,hónap és napokat ha tudja
            ho = int(idopont[5:6])
            nap = int(idopont[8:9])
            
            if(type(ev) is int and type(ho) is int and type(nap) is int and idopont[4] =="." and idopont[7] =="." and len(idopont) == 10):  #Ellenőrzi, hogy a dátum jól van-e megadva
                
                try:
                    f = open("BelföldiJáratok.txt", "r")                                                                              #Megnézi, hogy létezik-e ilyen járatszámú járat
                    x = f.readlines()
                    for i in range(len(x)):
                        if (x[i].split()[1] == jarat):
                            letezik = True
                    f.close()

                    f = open("NemzetköziJáratok.txt", "r")
                    x = f.readlines()
                    for i in range(len(x)):
                        if (x[i].split()[1] == jarat):
                            letezik = True
                    f.close()
                except:
                    pass
        
                if(letezik):
            
                    try:
                        f = open("Foglalások.txt", "r")                                       #Megnyitja a Foglalások.txt file-t és ellenőrzi, hogy van-e ilyen foglalás
                        x = f.readlines()
                        for i in range(len(x)):
                            if (x[i].split()[1] == jarat and x[i].split()[2] == idopont):
                                egyezik = True
                    except:
                        pass
                else:
                    print("Nem található ilyen járat!")
        
            
            else:
                print("Nem pontot használtál a dátumformátumnál vagy nem megfelelő a formátum! (éééé.hh.nn)")
            return letezik,egyezik
        except:
            print("Nem megfelelő karaktereket használtál a dátumnál, vagy nem jó a formátum! (éééé.hh.nn)")
            return letezik,egyezik

        


    def jegyFoglalas(self,name,jaratszam,idopont):
       
        check = self.jaratEllenorzes(jaratszam,idopont)
        if(check[0] and not(check[1])):
            try:
                f = open("Foglalások.txt", "x")                          #Létrehozza a Foglalások.txt file-t
            except:
                f = open("Foglalások.txt", "a")                          #Megnyitja a Foglalások.txt file-t append módba 
            f.write(name + " " + jaratszam + " " + idopont + "\n")       #Hozzáadja a foglalást a txt-hez 
            f.close()
        elif(check[0] and check[1]):
            print("Sajnos ez a járat már megtelt, próbálj másikat vagy másik időpontban!")
        

    def foglalasLemondas(self,name,jaratszam,idopont):
       
        check = self.jaratEllenorzes(jaratszam,idopont)                                                       #Ellenőrzi, hogy létzezik-e a foglalás
        if(check[0] and check[1]):
            f = open("Foglalások.txt", "r")
            y = f.readlines()
            f.close()
            f = open("Foglalások.txt", "w")
            for i in range(len(y)-1):
                if (y[i].split()[1] == jaratszam and y[i].split()[2] == idopont and y[i].split()[0] == name): #Eggyezőséget keres a lemondani kívánt foglalás és az aktív foglalások között
                    del y[i]                                                                                  #Törli a megfelelő sort 
            for line in y:
                f.write(line)                                                                                 #Visszaírja a txt-be az eredményt
            f.close()
            print("Sikeresen lemondtad a foglalást!")

    def foglalasokListazasa(self):
       
        try:
            f = open("Foglalások.txt", "r")                            #Megnyitja a foglalások file-t
            y = f.readlines()
            print("Foglalások: \n")
            for line in y:                                             #Végigmegy rajta és sorról sorra kiírja
                print(line)
        except:
            print("Nem található foglalás!")                           #Ha nincs létrehozva a foglalások.txt akkor tájékoztatjuk a felhasználót
        
    