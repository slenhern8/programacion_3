'''
Modulo de pruebas del modulo 'funciones.py'
'''
import unittest
from app.funciones import evalua_ganardor, IA

''' Usamos este array para las pruebas 
como ya habiamos mencionado la posicion 0 no se esta usando por eso la "a" 
los numeros indican a las funciones posiciones vacias en el cuadro'''
p = ['a', 'x', 'x', 'x', 4, 5, 6, '0', '0', 9]

class test_proyecto(unittest.TestCase):
    def test_evalua(self):
        '''
        Prueba que "x" gano la partida ya que en las posiciones 1, 2 y 3 :param p: tiene "x"
        '''
        self.assertEquals(evalua_ganardor(p), 'x')

    def test_IA(self):
        '''
        Prueba de donde va a jugar la computadora ya que en las posiciones 7 y 8 :param p: tiene "0" por lo que
        la computadora jugara en la posicion "9" automaticamente para ganar
        '''
        self.assertEquals(IA(p), 9)