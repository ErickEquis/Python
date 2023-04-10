import Empleado

class Disenador(Empleado):

    actDiariaDise = ["Reuniones de avance","Elaboración de diseño para páginas webs","Presentación-ajustes del diseño"]

    def __init__(self, actDiariaDise):
        self.__herramientaDiseno = "Photoshop"
        self.actDiaria = actDiariaDise
    
    def getHerramientaDiseno(self):
        return self.__herramientaDiseno
    def setHerramientaDiseno(self, herramientaDiseno):
        self.__herramientaDiseno = herramientaDiseno

disenador = Disenador()
print(disenador.getHerramientaDiseno)