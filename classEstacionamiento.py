class Estacionamiento(object):
	def __init__(self, capacidad):
		self.reservaciones = []
		self.capacidad = capacidad

	def reservar(self, hInicio, hFinal):
		if (type(hInicio) is not int) or (type(hFinal) is not int):
			raise TypeError('Las horas deben ser enteros.')
		if (hInicio < 600):
			raise ValueError('Hora de inicio de la reservacion invalida.')
		if (hFinal > 1800):
			raise ValueError('Hora final de la reservacion invalida.')
		if (hFinal < hInicio):
			raise ValueError('La hora de inicio es mayor que la hora final.')
		if (hInicio%100 != 0):
			raise ValueError('La hora inicial de la reservacion contempla minutos.')
		if (hFinal%100 != 0):
			raise ValueError('La hora final de la reservacion contempla minutos.')
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
