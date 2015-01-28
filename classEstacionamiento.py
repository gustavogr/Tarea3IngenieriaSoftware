class Estacionamiento(object):
	def __init__(self, capacidad):
		self.reservaciones = []
		self.capacidad = capacidad

	def reservar(self, hInicio, hFinal):
		if len(self.reservaciones) < self.capacidad:
			self.reservaciones.append((hInicio,hFinal))
			return True
		else:
			return False
