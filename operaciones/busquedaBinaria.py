# clase que permite realizar la busqueda binaria
class ArregloBinario:

	#se declara la variable con la cual se interactua 
	def __init__(self, datos):
		self.datos = datos

	# metodo para agregar la informacino de datos
	def agregarInformacion(self, datos):
		self.datos = datos

	# metodo que realiza la busqueda binaria 
	def busquedaBinaria(self, elementoBuscar):
		inferior = 0  # inferior es la primera posicion de la lista
		superior = len(self.datos) - 1 # superior es la ultima posicion de la lista
		medio = int((inferior + superior + 1) / 2) # medio es la pocision central de la lista
		ubicacion = -1 # se encargara de devolver la ubicacion que se busca 
		elemento = elementoBuscar # es el elemnto a buscar

		while ((inferior <= superior) and (ubicacion == -1)): # se realiza las condiciones para la iteracion
			if( elementoBuscar == self.datos[medio]):  # si el elemento se encuentra en medio
				ubicacion = medio; # la ubicaci�n es el elemento medio actual

			elif ( elementoBuscar < self.datos[medio]): # el elemento medio es demasiado alto
				superior = medio - 1 # elimina la mitad superior 

			else: # el elemento medio es demasiado bajo
				inferior = medio + 1 # elimina la mitad inferior

			medio = int((inferior + superior + 1) / 2) #  recalcula el elemento medio

		return ubicacion # devuelve la ubicaci�n de la clave de b�squeda

	

