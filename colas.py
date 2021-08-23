class Colas:
        def __init__(self,tamanio):
            self.__lista = []
            self.__tope = 0
            self.size = tamanio
            
        def empty(self):
            return self.__tope == 0 # metodo automatico
            # if self.__tope == 0:
            #     return True
            # else:
            #     return False
            
        def push(self,dato):
            if self.__tope < self.size:
                self.__lista = self.__lista + [dato] 
                self.__tope += 1
            else:
                print("La lista esta llena")
                
        def pop(self):
            if self.empty():
                return None
            else:
                self.__lista = self.__lista[1:]
                self.__tope -= 1
            print()    
            
        def show(self):
            for top in range(0,self.__tope):   
                print("[{}]".format(self.__lista[top]))
                
        def longitud(self):
            return self.__tope