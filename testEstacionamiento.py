import unittest
from classEstacionamiento import *

class TestReservar(unittest.TestCase):
	def testExisteFuncion(self):
		e = Estacionamiento()
		e.reservar(0,0)

	def testRealizarReservaEstacionamientoVacio(self):
		e = Estacionamiento()
		e.reservar(800, 1000)





if __name__ == "__main__":
    unittest.main()