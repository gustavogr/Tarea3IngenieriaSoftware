import unittest
from classEstacionamiento import *

class TestReservar(unittest.TestCase):
	def testExisteFuncion(self):
		# Agregado por incremento TDD sin frontera.
		e = Estacionamiento(10)
		e.reservar(700, 800)

	def testReservaEstacionamientoVacio(self):
		# Agregado por incremento TDD con frontera.
		e = Estacionamiento(10)
		assert e.reservar(800, 1000)

	def testReservaHorarioLleno(self):
		# Agregado por incremento TDD con frontera.
		e = Estacionamiento(10)
		for i in range(10):
			e.reservar(800, 900)
		assert not e.reservar(800, 900) 

	def testReservarHorarioNoVacio(self):
		# Agregado por incremento TDD sin frontera.
		e = Estacionamiento(10)
		for i in range(9):
			e.reservar(800, 900)
		assert e.reservar(800, 900)

	def testReservarConOtroHorarioLleno(self):
		# Agregado por incremento TDD con frontera.
		e = Estacionamiento(10)
		for i in range(10):
			e.reservar(800, 900)
		assert e.reservar(1500, 1700)

	def testReservarHorarioFinalLleno(self):
		# Agregado por incremento TDD con frontera.
		e = Estacionamiento(10)
		for i in range(10):
			e.reservar(800,1000)
		assert not e.reservar(700,900)

	def testReservarHoraInicialMenorALimiteInferior(self):
		# Agregado por incremento TDD con frontera.
		e = Estacionamiento(10)
		self.assertRaises(ValueError, e.reservar, 500, 800)

	def testReservarHoraFinalMayorALimiteSuperior(self):
		# Agregado por incremento TDD con frontera.
		e = Estacionamiento(10)
		self.assertRaises(ValueError, e.reservar, 1500, 1900)

	def testReservarHoraInicialMayorAHoraFinal(self):
		# Agregado por incremento TDD sin frontera.
		e = Estacionamiento(10)
		self.assertRaises(ValueError, e.reservar, 1400, 800)

	def testReservarHoraInicialConMinutos(self):
		# Agregado por incremento TDD sin frontera.
		e = Estacionamiento(10)
		self.assertRaises(ValueError, e.reservar, 1425, 1500)

	def testReservarHorarioFinalConMinutos(self):
		# Agregado por incremento TDD sin frontera.
		e = Estacionamiento(10)
		self.assertRaises(ValueError, e.reservar, 1400, 1525)
		
if __name__ == "__main__":
    unittest.main()