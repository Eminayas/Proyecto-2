class Lista:
    def __init__(self,tamanio):
        self.lista = []
        self.longitud=0
        self.size= tamanio
        
        
    def append(self, dato): #agregar datos a la lista
        if self.longitud < self.size:
           self.lista += [dato]
           self.longitud += 1
        else:
            print("Lista esta llena")
            
    def obtener(self,pos): #obtener datos de la lista        
        if pos < 0 or pos >= self.longitud:
            return None
        else: 
            valor = self.lista[pos]
            # listAux = self.lista[0:pos] + self.lista[pos+1]
            
            listAux = self.lista[0:pos]
            for indice in range(pos,self.longitud-1):
                listAux = listAux +  [self.lista[indice+1]]
            self.longitud -= 1
            self.lista = listAux 
            return valor  
            

    def mostrar (self,orden): # muestra la lista ingresada de forma des-asc dependiendo de las condiciones del usuario
        if orden.lower() == "asc":
            for pos in range(self.longitud):
                print("[{}]".format(self.lista[pos]))
        else:
            for pos in range(self.longitud-1,-1,-1):
                print("[{}]".format(self.lista[pos]))  
                
                      
    def buscar(self,dato):  
        if self.longitud > 0 and self.longitud <= self.size:
            for pos, ele in enumerate(self.lista):
                if dato == ele:
                    return pos
            else:
                return None
        else:
            print("La lista no tiene valores")
            return None
        
        
    def insertar(self,dato):
        
        if self.buscar(dato) != None:
            print("No se puede agregar el valor porque ya existe en la Lista")
        else:
            self.append(dato)
    
    
    
    def eliminar(self, dato):
        e = self.buscar(dato)
        
        if e == None:
            print("El numero a elminar no existe en la Lista")
        else:
            self.obtener(e)
            
            
   
       
       
# lista = Lista(4)
# lista.append(3)
# lista.append(4)
# lista.append(2)
# lista.append(8)
# lista.append(9)
# # print(lista.obtener(7))
# # print(lista.obtener(1))
# lista.mostrar("des")