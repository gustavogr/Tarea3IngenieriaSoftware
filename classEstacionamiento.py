class Estacionamiento(object):
	def __init__(self, capacidad):
		self.reservaciones = []
		self.capacidad = capacidad

	def reservar(self, hInicio, hFinal):
		numSolapados = 0
		for i in self.reservaciones :
			if i[0] >= hFinal :
				break
			numSolapados -= i[1]
			if i[0] >= hInicio  and numSolapados == self.capacidad:
				return False
		self.reservaciones.append((hInicio,-1))
		self.reservaciones.append((hFinal,1))
		self.reservaciones = sorted(self.reservaciones, key=lambda x: (x[0],-x[1]))
		return True	
