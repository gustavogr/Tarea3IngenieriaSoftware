class Estacionamiento(object):
	def __init__(self):
		self.reservaciones = []

	def reservar(self, hInicio, hFinal):
		if len(self.reservaciones) == 0:
			self.reservaciones.append((hInicio,hFinal))
			return True
		else :
			return False
