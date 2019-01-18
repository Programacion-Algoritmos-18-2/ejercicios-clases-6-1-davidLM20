# se importa toda la informacion de los paquetes
from archivos.leerArchivo import *
from operaciones.busquedaBinaria import *

m = MiArchivo() # se declara un objeto para la lectura del archivo

lista = m.obtener_informacion() # se crea una variable que contendra la informacion del objeto m
lista = [l.split(",") for l in lista] # se usa el split para separar la cadena por (,)

lista_2 = [] # se crea una nueva lista vacia 
for d in lista: # se recorre cada linea de la lista 
	for n in d: # se vuelve a iterar dato por dato
		lista_2.append(int(n)) # se agrega a la nueva lista

lista_2.sort() # se usa la funcion sort para ordenar la nueva lista
print("La lista ordenada es:\n",lista_2) # se imprime un encabezado junto con la lista
busqueda = 	ArregloBinario(lista_2) # se declara un nuevo objeto 
llave = 3 # es la clave a buscar 
pocision = busqueda.busquedaBinaria(llave) # se declara una nueva variable que llamara al metodo busqueda binaria
print("La pocision es:\n", pocision) # se imprime la pocision