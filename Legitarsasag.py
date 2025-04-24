from BelfoldiJarat import BelfoldiJarat
from NemzetkoziJarat import NemzetkoziJarat

class Legitarsasag():
    
    def __init__(self, legitarsasagneve):
        self.legitarsasagneve = legitarsasagneve               # Légitársaság neve
    
    def jaratHozzaadas(self, jaratszam, honnan, hova, jegyar):
        
        if (honnan.split()[0] == hova.split()[0]):             #Megvizsgálja ,hogy belföldi-e a járat      
           
            belfoldi = BelfoldiJarat(jaratszam,hova,jegyar)
            if (belfoldi.letezojarat("BelföldiJáratok")):
                print ("létező járat")                         #Ha már létezik a járat, tájékoztatja a felhasználót
            else:
                belfoldi.jarathozzaadas(self.legitarsasagneve, honnan) #Hozáadja az új járatot
            
        else:
             
            nemzetkozi = NemzetkoziJarat(jaratszam,hova,jegyar)
            if (nemzetkozi.letezojarat("NemzetköziJáratok")):
                print ("létező járat")
            else:
                nemzetkozi.jarathozzaadas(self.legitarsasagneve, honnan)
           

       