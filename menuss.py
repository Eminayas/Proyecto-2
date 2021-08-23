import os
class Menu:
    def __init__(self,titu,opci):
        self.titulo=titu
        self.opciones=opci
        
    def menu(self):
        print(self.titulo)
        for opcion in self.opciones:
            print(opcion)
        opc = input("Elija opcion[1....{}]: ".format(len(self.opciones)))
        return opc