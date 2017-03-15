"""
Ese es el modulo para saludar
"""

class Hola(object):
    """
    Esta es la clase Hola para encapsular un saludo
    """

    def __init__(self, nombre):
        """
        Este es el constructor

        Crea una instancia de la :class: 'Hola'

        :param nombre: nombre para el saludo
        :type nombre: str
        """
        self.nombre = nombre

    def saludar(self):
        """
        este es el motodo para saludar

        """
        print("Hola %s", self.nombre)