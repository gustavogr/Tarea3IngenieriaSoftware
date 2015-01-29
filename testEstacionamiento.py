import unittest
from classEstacionamiento import *

class TestReservar(unittest.TestCase):
	def testExisteFuncion(self):
		e = Estacionamiento(10)
		e.reservar(700, 800)

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

	def testReservarConOtroHorarioLleno(self):
		e = Estacionamiento(10)
		for i in range(10):
			e.reservar(800, 900)
		assert e.reservar(1500, 1700)

	def testReservarHorarioFinalLleno(self):
		e = Estacionamiento(10)
		for i in range(10):
			e.reservar(800,1000)
		assert not e.reservar(700,900)

	def testReservarHoraInicialInvalida(self):
		e = Estacionamiento(10)
		self.assertRaises(ValueError, e.reservar, 500, 800)

	def testReservarHoraFinalInvalida(self):
		e = Estacionamiento(10)
		self.assertRaises(ValueError, e.reservar, 1500, 1900)

if __name__ == "__main__":
    unittest.main()