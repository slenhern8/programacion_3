class empleado:
    __conteo = 0 #variables globales
#poner __ antes de las variables para ponerlas privadas de esta clase solamente y no se pueda ver en otro lado
    def __init__(self, nombre, salario):
        self.nombre = nombre #estos son atributos
        self.salario = salario
        empleado.__conteo +=1

    def mostrar_conteo(self):
        print("Esta emoresa tiene " + str(empleado.__conteo) + " empleados")

    def mostrar_empleado(self):
        print("Nombre: " + self.nombre)
        print("Salario: " + str(self.salario))

    def calcular_salario_neto(self):
        if self.salario < 2000:
            return self.salario * 0.93
        elif self.salario > 5000:
            return self.salario * 0.85
        else:
            return self.salario

