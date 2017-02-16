class circunferencia:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.1416*self.radio*self.radio

    def calcular_diametro(self):
        return self.radio*2
