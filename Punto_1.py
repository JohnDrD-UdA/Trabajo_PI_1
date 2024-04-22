class Vehiculo:
    def __init__(self,ano=0,marca='',modelo='') -> None:
        self.__ano=ano
        self.__marca=marca
        self.__modelo=modelo
    def getAno(self)-> int:
       return self.__ano
    def getMarca(self)-> str:
        return self.__marca
    def getModelo(self)-> str:
        return self.__modelo
    
    def setAno(self,ano:int)-> None:
        self.__ano= ano
    def setMarca(self,marca:str)-> None:
        self.__marca=marca
    def setModelo(self, modelo:str)-> None:
        self.__modelo= modelo

    
    def detalles(self)-> None:
        return f"Marca: [{self.__marca}], Modelo: [{self.__modelo}], Año: [{self.__ano}]"

car= Vehiculo(2014,"mazda","3")

print(car.detalles())

car.setAno(2010)
car.setMarca("Honda")
car.setModelo("xp")

print(car.detalles())