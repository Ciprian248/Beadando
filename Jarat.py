from abc import ABC, abstractmethod


class Jarat(ABC):
    def __init__(self, jaratszam, celallomas, jegyar):
        self.jaratszam = jaratszam        # Járatszám
        self.celallomas = celallomas      # Célállomás
        self.jegyar = jegyar              # Jegyár

 

    @abstractmethod                       #Absztrakt metódus
    def jarathozzaadas(self):
        pass

    def letezojarat(self, filename):      #Megvizsgálja hogy létezik-e a járat, ha igen akkor a visszatérési értéke TRUE
        try:
            f = open(filename + ".txt", "r")
            x = f.readlines()
            for i in range(len(x)):
                if (x[i].split()[1] == self.jaratszam):
                    return True
                else:
                    return False
            f.close()
        except:
            return False

