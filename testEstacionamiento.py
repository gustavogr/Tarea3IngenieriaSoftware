import unittest
from classEstacionamiento import *

class TestReservar(unittest.TestCase):
	def testExisteFuncion(self):
		e = Estacionamiento()
		e.reservar(0,0)

	def testRealizarReservaEstacionamientoVacio(self):
		e = Estacionamiento()
		e.reservar(800, 1000)

	def testRealizarReservaEstacionamientoLleno(self):
		e = Estacionamiento()
		for i in range(10):
			e.reservar(800,900)
		assert not e.reservar(800,900)



if __name__ == "__main__":
    unittest.main()