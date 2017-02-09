from app.empleado import empleado
# de app archibo empleado se importa  la clase empleado
import time #se importo para usar la funcion time.spleep abajo
from app.Ejecutivo import Ejecutivo

if __name__ == "__main__":
    # ESTE CODIGO SE VA A ADAPTAR PARA UNA PRACTICA ''' para saber como estaba originalmente
    '''e1 = empleado("Juan", 2500)
    e2 = empleado("Maria", 4250)
    #print("Empleados Totales: " + str(empleado.conteo)) #aqui se llama a la variable
    #la linea de arriba se vuelve imposible al volver privada la variable
    e1.mostrar_conteo()  #y aqui se llama el metodo

    print("Infomacion de Empleados")
    e1.mostrar_empleado()
    e2.mostrar_empleado()

    ex1 = Ejecutivo("Petra", 15000)
    ex1.mostrar_empleado("Sra.")
    ex1.mostrar_conteo() #con esto vemos que a pesar de que conteo esta en empleado ejecu lo eredo y tambien sumo
    ex1.mandar()
    ex1_salario_neto = ex1.calcular_salario_neto()
    print("El Sr(a). {} tiene salario neto de $ {:.2f}".format(ex1.nombre, ex1_salario_neto))
    #las {} son para imprimir al estilo de C ,  {:.2} ajusta los decimales a 2 , el primer {} que esta solo acepta lo que sea
    e2_salario_neto = e2.calcular_salario_neto()
    print("El Sr(a). {} tiene salario neto de $ {:.2f}".format(e2.nombre, e2_salario_neto))

    #time.sleep(10) #sirve para hacer que el programa se detenga por (segundos) se puso para que el error de abajo saliera
    #del e2 #con esto se borra
    #e2.mostrar_empleado() #solo se esta usando para ejemplo que se borro y manda error
    '''
    #INICIO PRACTICA
    empleados = []
    ejecutivos = []

    flag = True
    while flag:
        try:
            print("\nMENU\n 1. Agregar Empleado\n 2. Ver Empleado\n 3. Salir")
            op = int(input())
            if op == 3:
                flag = False
            elif op == 2:
                print("Los empleados son: ")
                a = empleados.count()
                for i in range(a):
                    print(a)      # AQUI ******************************************************************FALTA
            elif op == 1:
                flag2 = True
                while flag2:
                    try:
                        print("\nTipo a agregar?\n 1. Ejecutivo\n 2. Empleado\n 3. Atras")
                        op = int(input())
                        if op == 3:
                            flag2 = False
                        elif op == 2:
                            print("Nombre de empleado:")
                            nom = input()
                            print("Salario de empleado:")
                            sal = float(input())
                            emp = empleado(nom , sal)
                            empleados.append(emp)
                        elif op == 1:
                            print("Nombre de ejecutivo:")
                            nom = input()
                            print("Salario de ejecutivo:")
                            sal = float(input())
                            emp = empleado(nom, sal)
                            ejecutivos.append(emp)
                        else:
                            print("Esa opcion no existe")
                    except ValueError:
                        print("No introdujo un numero")
                    except:
                        print("Error")
            else:
                print("Esa opcion no existe")
        except ValueError:
            print("No introdujo un numero")
        except:
            print("Error")
