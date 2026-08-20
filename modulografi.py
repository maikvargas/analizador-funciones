from matplotlib import pyplot as plt 
import numpy as np
import moduloderi_polinc as md
from basic_units import *

#_________________funcion graficador para funciones polinomicas, exponenciales, identidad, y constante_____________________#

def graficador(d,k,z,*x):
	v=["f(x)=","f'(x)=","f''(x)="]
	h=md.derivada(2,k,z)
	j=0
	for i in x:
		leyenda=v[j] + str(h[j])
		puntosde_f=np.ones(len(d))*i(d)
		
		plt.plot(d, puntosde_f, label=leyenda)
		j+=1
	plt.title("GRAFICA DE f(x) Y SUS DERIVADAS")
	plt.legend()
	plt.grid()
	plt.show()


#_________________funcion graficador para funciones trigonometricas y sus inversas__________________________________________#

def graficador_trigonometricas(d,k,z,*x):
	v=["f(x)=","f'(x)=","f''(x)="]
	h=md.derivada(2,k,z)
	j=0
	for i in x:
		leyenda=v[j] + str(h[j])
		x = [val*radians for val in d]
		plt.plot(x, i(d), xunits=radians, label=leyenda)
		#plt.plot(d,puntosde_f, label=leyenda)
		j+=1
	plt.title("GRAFICA DE FUNCIONES TRIGONOMETRICAS Y SUS DERIVADAS")
	plt.legend()
	plt.grid()
	plt.show()
