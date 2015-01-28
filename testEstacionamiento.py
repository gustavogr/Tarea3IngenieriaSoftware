import unittest
from classEstacionamiento import *

class TestReservar(unittest.TestCase):
	def testExisteFuncion(self):
		e = Estacionamiento(10)
		e.reservar(0, 0)

	def testReservaEstacionamientoVacio(self):
		e = Estacionamiento(10)
		assert e.reservar(800, 1000)

	def testReservaHorarioLleno(self):
		e = Estacionamiento(10)
		for i in range(10):
			e.reservar(800, 900)
		assert not e.reservar(800, 900)

	def testReservarHorarioNoVacio(self):
		e = Estacionamiento(10)
		for i in range(9):
			e.reservar(800, 900)
		assert e.reservar(800, 900)


if __name__ == "__main__":
    unittest.main()