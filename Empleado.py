class Empleado:
    
    """
    Constructor: __init__ indica que es un constructor
    'self' = this en Java. Debe ir en cada metodo de la clase
    '__atributo' encapsula el atributo
    """
    def __init__(self, nombre, apellidos, edad, actDiaria, codigoEmp):
            self.__nombre = nombre
            self.__apellidos = apellidos
            self.__edad = edad
            self.__actDiaria = actDiaria
            self.__codigoEmp = codigoEmp

    def getNombre(self):
          return self.__nombre
    def setNombre(self, nombre):
          self.__nombre = nombre
    
    def getApellido(self):
          return self.__apellidos
    def setApellidos(self, apellidos):
          self.__apellidos = apellidos
    
    def getEdad(self):
          return self.__edad
    def setEdad(self, edad):
          self.__edad = edad

    def getActDiaria(self):
          return self.__actDiaria
    def setActDiaria(self, actDiaria):
          self.__actDiaria = actDiaria
    
    def getCodigoEmp(self):
          return self.__codigoEmp
    def setCodigoEmp(self, codigoEmp):
          self.__codigoEmp = codigoEmp
    
empleado = Empleado("Erick", "Santillan", 28, "Ninguna")
print(empleado.getNombre())
empleado.setNombre("Terry")
print(empleado.getNombre())