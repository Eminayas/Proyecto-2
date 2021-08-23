import os
from menuss import Menu
from lista import Lista
from pilas import Pila
from colas import Colas


opc = ""
while opc != "4":
    os.system("cls")
    men = Menu("Menú Principal",["1)Listas","2)Pilas","3)Colas","4)Salir"])
    opc = men.menu()
    
    if opc == "1":
        opc3 =""
        n = int(input("Ingrese el tamaño de la lista: "))
        lista = Lista(n)
        os.system("cls")
        while opc3 != "7":
            os.system("cls") 
            men3 = Menu("Menú Tratamiento de Listas",["1)Append","2)Mostrar","3)Obtener","4)Busca", "5) Insertar", "6)Eliminar", "7)Salir"])
            opc3 = men3.menu()
            
            if opc3 == "1":
                os.system("cls")
                list =[]
                x = str(input("Ingrese un valor: "))
                lista.append(x)
                input("Presione una tecla para continuar")
                
            elif opc3 == "2":
                os.system("cls")
                a = str(input("Ingrese la manera en que quiere presentar la lista: ")) 
                lista.mostrar(a)

                input("Presione una tecla para continuar")
                
            elif opc3 == "3":
                os.system("cls")
                o = int(input("Ingrese la posicion que se va obtener de la Lista: "))
                print("El valor que se obtenido fue: {}".format(lista.obtener(o))) 
            

                input("Presione una tecla para continuar")
                
            elif opc3 == "4":
                os.system("cls")
                c = str(input("Ingrese el valor a buscar que va a buscar en la Lista: "))
                lista.buscar(c)
                if lista.buscar(c) !=None:
                    print ("El dato es {} y esta en la posicion {}".format(c,lista.buscar(c)))
                else:
                    print("El valor no existe en la Lista")         
                    
                input("Presione una tecla para continuar") 
               
            elif opc3 == "5":
                os.system("cls")
                p = str(input("Ingrese el valor que va insertar en la Lista: "))
                lista.insertar(p)
                
                input("Presione una tecla para continuar")
                
            elif opc3 == "6":
                os.system("cls")
                i = str(input("Ingrese el valor que va eliminar en la Lista: "))
                lista.eliminar(i)
                
                input("Presione una tecla para continuar")    
                
                
                     
                
    if opc == "2":
        opc3 =""
        n = int(input("Ingrese el tamaño de la pila: "))
        pila = Pila(n)
        os.system("cls")
        while opc3 != "6":
            os.system("cls") 
            men3 = Menu("Menú de pilas",["1)Push","2)Pop","3)Show","4)Empty","5)Longitud", "6)Salir"])
            opc3 = men3.menu()
            if opc3 == "1":
                os.system("cls")
                d = int(input("Ingrese un numero en la pila:"))
                pila.push(d)
                input("Presione una tecla para continuar")
             
            elif opc3 == "2":
                os.system("cls")
                pila.pop()

                input("Presione una tecla para continuar")
                
            elif opc3 == "3":
                os.system("cls")
                pila.show()
                input("Presione una tecla para continuar")
                
            elif opc3 == "4":
                os.system("cls")
                pila.empty()
                input("Presione una tecla para continuar")       
                                        
            elif opc3 == "5":
                os.system("cls")
                print("La longitud de los elementos ingresados en la pilas son: {}".format(pila.longitud()))
                input("Presione una tecla para continuar")

                
    if opc == "3":
        opc3 =""
        n = int(input("Ingrese el tamaño de la cola: "))
        cola = Colas(n)
        os.system("cls")
        while opc3 != "6":
            os.system("cls") 
            men3 = Menu("Menú de Colas",["1)Push","2)Pop","3)Show","4)Empty","5)Longitud", "6)Salir"])
            opc3 = men3.menu()
            if opc3 == "1":
                os.system("cls")
                d = int(input("Ingrese un numero en la cola: "))
                cola.push(d)
                input("Presione una tecla para continuar")
             
            elif opc3 == "2":
                os.system("cls")
                cola.pop()

                input("Presione una tecla para continuar")
                
            elif opc3 == "3":
                os.system("cls")
                cola.show()
                input("Presione una tecla para continuar")
                
            elif opc3 == "4":
                os.system("cls")
                cola.empty()
                input("Presione una tecla para continuar")       
                                        
            elif opc3 == "5":
                os.system("cls")
                print("La longitud de los elementos ingresados en la cola son: {}".format(cola.longitud()))
                input("Presione una tecla para continuar")
            
            elif opc3 == "4":
                print("Gracias por usar el sistema")
                input("Presione una tecla para continuar")
                   
    else:
        print("Opción no valida")
        input("Presione una tecla para continuar")    
                
                
                
print("Muchas gracias por su visita, vuelva cuando quiera")                