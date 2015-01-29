class Estacionamiento(object):
	def __init__(self, capacidad):
		self.reservaciones = []
		self.capacidad = capacidad

	def reservar(self, hInicio, hFinal):
		numSolapados = 0
		for i in self.reservaciones :
			if i[0] > hInicio:
				break
			numSolapados = numSolapados - i[1]
		if numSolapados < self.capacidad:
			self.agregarInicioEnOrden(hInicio)
			self.agregarFinalEnOrden(hFinal)
			return True
		else:
			return False

	def agregarInicioEnOrden(self, hInicio):
		i = 0
		hInicioEsMayor = True
		largoLista = len(self.reservaciones)
		while (i < largoLista) & hInicioEsMayor:
			if self.reservaciones[i][0] <= hInicio:
				i = i + 1
			else:
				hInicioEsMayor = False
		if i == largoLista:
			self.reservaciones.append((hInicio, -1))
		else:
			self.reservaciones.insert(i, (hInicio, -1))
	
	def agregarFinalEnOrden(self, hFinal):
		i = 0
		hFinalEsMayor = True
		largoLista = len(self.reservaciones)
		while (i < largoLista) & hFinalEsMayor:
			if self.reservaciones[i][0] < hFinal:
				i = i + 1
			else:
				hFinalEsMayor = False
		if i == largoLista:
			self.reservaciones.append((hFinal, +1))
		else:
			self.reservaciones.insert(i, (hFinal, +1))
