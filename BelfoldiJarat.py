from Jarat import Jarat

class BelfoldiJarat(Jarat):
    
    def jarathozzaadas(self, legitarsasagneve, indulas):
        try:
            f = open("BelföldiJáratok.txt", "x")  #Létrehozza a BelföldiJáratok.txt file-t
        except:
            f = open("BelföldiJáratok.txt", "a")  #Megnyitja a BelföldiJáratok.txt file-t append módba 
        f.write(legitarsasagneve + " " + self.jaratszam + " belföldi járat " + indulas + " " + self.celallomas + " "+ self.jegyar + "\n") #Hozzáadja a járatot a txt-hez majd lezárja a megynyitást
        f.close()