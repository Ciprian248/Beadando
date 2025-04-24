from Jarat import Jarat

class NemzetkoziJarat(Jarat):
    
    def jarathozzaadas(self, legitarsasagneve, indulas):
        try:
            f = open("NemzetköziJáratok.txt", "x")  #Létrehozza a NemzetköziJáratok.txt file-t
        except:
            f = open("NemzetköziJáratok.txt", "a")  #Megnyitja a NemzetköziJáratok.txt file-t append módba 
        f.write(legitarsasagneve + " " + self.jaratszam + " nemzetközi járat " + indulas + " " + self.celallomas + " " + self.jegyar + "\n") #Hozzáadja a járatot a txt-hez majd lezárja a megynyitást
        f.close()