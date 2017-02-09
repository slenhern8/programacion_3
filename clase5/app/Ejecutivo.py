from app.empleado import empleado

class Ejecutivo(empleado):
    def mandar(self):
        print("Traeme un cafe!")

    def calcular_salario_neto(self): #overWrite
        return self.salario * 0.98 #se sobre escribe el metodo que ya existe en empleado
        #en empleado sigue normal pero cuando un ejecutivo lo llame saldra este

    def mostrar_empleado(self, saludo):
        print("nombre: {}  {}".format(saludo, self.nombre))
        print("Salario:" + str(self.salario))

