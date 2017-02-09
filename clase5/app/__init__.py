from app.empleado import empleado
# de app archibo empleado se importa  la clase empleado
import time #se importo para usar la funcion time.spleep abajo
from app.Ejecutivo import Ejecutivo

if __name__ == "__main__":
    e1 = empleado("Juan", 2500)
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