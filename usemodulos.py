from tkinter import *
from tkinter import messagebox
import sympy as sp 
import numpy as np 

import moduloderi_polinc as md 
import modulografi as mg 
import moduloderi_trigo as ep

class interfaz_funciones_y_sus_derivadas:
	"""docstring for interfaz_funciones_y_sus_derivadas"""
	def __init__(self, funciones):

		"""pedimos al usuario la variable independiente de f(x)"""
		self.etiqueta_x =Label(funciones, text= 'INGRESE LA VARIABLE INDEPENDIENTE DE F(x)', fg='blue')
		self.etiqueta_x.place(x=200, y=30)
		self.entrada_x=Entry(funciones,width=5)
		self.entrada_x.config(justify='center')
		self.entrada_x.place(x=290, y=60)


		"""pedimos al usuario la funcion"""
		self.etiqueta_f=Label(funciones, text= 'INGRESE LA FUNCIÓN', fg='blue')
		self.etiqueta_f.place(x=520, y=30)
		self.entrada_f=Entry(funciones, width=30)
		self.entrada_f.config(justify='center')
		self.entrada_f.place(x=485, y=60)


		"""pedimos al usuario el inicio del dominio"""
		self.etiqueta_ini_dom=Label(funciones, text= 'INGRESE EL INICIO DEL DOMÍNIO', fg='blue')
		self.etiqueta_ini_dom.place(x=225, y=90)
		self.entrada_ini_dom=Entry(funciones, width=10)
		self.entrada_ini_dom.config(justify='center')
		self.entrada_ini_dom.place(x=275, y=120)


		"""pedimos al usuario el fin del dominio"""
		self.etiqueta_end_dom=Label(funciones, text= 'INGRESE EL FINAL DEL DOMÍNIO', fg='blue')
		self.etiqueta_end_dom.place(x=495, y=90)
		self.entrada_end_dom=Entry(funciones, width=10)
		self.entrada_end_dom.config(justify='center')
		self.entrada_end_dom.place(x=540, y=120)


#%%%%%%%%%%%%%%%%%%%%%%%%%% BOTON MAXIMOS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#
		"""creamos el boton para hallar los maximos"""
		self.Boton_maximos=Button(funciones, text='calcular puntos maximos', fg='red' ,cursor='pirate', command=self.boton_maximos)
		self.Boton_maximos.place(x=80, y=160)

		"""mostramos en pantalla los maximos de la funcion"""
		self.etiqueta_salida_maximos=Label(funciones, text='Los puntos maximos de f(x) son: ')
		self.etiqueta_salida_maximos.place(x=65, y=190)
		self.salida_maximos=Text(funciones, width=30, height=2)
		self.salida_maximos.place(x=30, y=220)


#%%%%%%%%%%%%%%%%%%%%%%%%%% BOTON MINIMOS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#
		"""creamos el boton para hallar los minimos"""
		self.Boton_minimos=Button(funciones, text='calcular puntos minimos', fg='red' ,cursor='pirate', command=self.boton_minimos)
		self.Boton_minimos.place(x=370, y=160)

		"""mostramos en pantalla los minimos de la funcion"""
		self.etiqueta_salida_minimos=Label(funciones, text='Los puntos minimos de f(x) son: ')
		self.etiqueta_salida_minimos.place(x=355, y=190)
		self.salida_minimos=Text(funciones, width=30, height=2)
		self.salida_minimos.place(x=320, y=220)


#%%%%%%%%%%%%%%%%%%%%%%%%%% BOTON PUNTOS DE INFLEXION %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#
		"""creamos el boton para hallar los puntos de inflexion"""
		self.Boton_puntos_de_inflexion=Button(funciones, text='calcular puntos de inflexion', fg='red' ,cursor='pirate', command=self.punt_inflex)
		self.Boton_puntos_de_inflexion.place(x=655, y=160)

		"""mostramos en pantalla los puntos de inflexion"""
		self.etiqueta_salida_puntos_de_inflexion=Label(funciones, text='Los puntos de inflexion de f(x) son: ')
		self.etiqueta_salida_puntos_de_inflexion.place(x=640, y=190)
		self.salida_puntos_de_inflexion=Text(funciones, width=30, height=2)
		self.salida_puntos_de_inflexion.place(x=610, y=220)


#%%%%%%%%%%%%%%%%%%%%%%%%%% BOTON INTERVALOS DE CRECIMIENTO %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#
		"""creamos el boton para hallar los intervalos de crecimiento"""
		self.Boton_interval_cre=Button(funciones, text='calcular intervalos de crecimiento', fg='red',cursor='pirate', command=self.interval_cre )
		self.Boton_interval_cre.place(x=60, y=280)

		"""mostramos en pantalla los intervalos de crecimiento"""
		self.etiqueta_salida_interval_cre=Label(funciones, text='Los intervalos de crecimiento de f(x) son: ')
		self.etiqueta_salida_interval_cre.place(x=40, y=310)
		self.salida_interval_cre=Text(funciones, width=30, height=2)
		self.salida_interval_cre.place(x=30, y=340)

#%%%%%%%%%%%%%%%%%%%%%%%%%% BOTON INTERVALOS DE DECRECIMIENTO %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#
		"""creamos el boton para hallar los intervalos de decrecimiento"""
		self.Boton_interval_cre=Button(funciones, text='calcular intervalos de decrecimiento', fg='red' ,cursor='pirate', command=self.interval_decre)
		self.Boton_interval_cre.place(x=340, y=280)

		"""mostramos en pantalla los intervalos de decrecimiento"""
		self.etiqueta_salida_interval_decre=Label(funciones, text='Los intervalos de decrecimiento de f(x) son: ')
		self.etiqueta_salida_interval_decre.place(x=325, y=310)
		self.salida_interval_decre=Text(funciones,width=30, height=2)
		self.salida_interval_decre.place(x=320, y=340)

#%%%%%%%%%%%%%%%%%%%%%%%%%% BOTON GRAFICA DE F(X) Y SUS DERIVADAS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#
		self.etiqueta_grafica=Label(funciones, text= 'Si presiona el botón "GRAFICAR", verá una ventana con')
		self.etiqueta_grafica1=Label(funciones, text= 'la gráfica de la función que ingresó y sus dos derivadas.')
		self.etiqueta_grafica.place(x=600,y=290)
		self.etiqueta_grafica1.place(x=600,y=310)

		"""creamos el boton para graficar la funcion y sus derivadas"""
		self.Boton_grafica=Button(funciones, text='GRAFICAR f(x) Y SUS DERIVADAS', fg='red' ,cursor='pirate', command=self.grafica_f)
		self.Boton_grafica.place(x=640, y=345)

#-------------comando de boton para calcular maximos-------------------------#
	def boton_maximos(self):
		try:
			f=sp.sympify(self.entrada_f.get())
			x=sp.symbols(self.entrada_x.get())

			f_num=sp.lambdify(x,md.derivada(2,f,x)[0])
			second_deri=sp.lambdify(x,md.derivada(2,f,x)[2])
			point_crit=sp.solve(md.derivada(2,f,x)[1],x)
		except:
			messagebox.showwarning('Error', 'No ha ingresado la función o la variable independiente. Intentelo nuevamente')	

		try:
			a=float(sp.sympify(self.entrada_ini_dom.get()))
			b=float(sp.sympify(self.entrada_end_dom.get()))
		except:
			messagebox.showwarning('Error', 'El domínio de su función esta incompleto, inténtelo nuevamente')

		try:	
			maximos=md.maximos(point_crit,second_deri,f_num,a,b)
			self.salida_maximos.delete('1.0',END)
			self.salida_maximos.insert(END, str(maximos))
		except:
			pass

		

#-------------comando de boton para calcular minimos-------------------------#
	def boton_minimos(self):
		try:
			f=sp.sympify(self.entrada_f.get())
			x=sp.symbols(self.entrada_x.get())

			f_num=sp.lambdify(x,md.derivada(2,f,x)[0])
			second_deri=sp.lambdify(x,md.derivada(2,f,x)[2])
			point_crit=sp.solve(md.derivada(2,f,x)[1],x)
		except:
			messagebox.showwarning('Error', 'No ha ingresado la función o la variable independiente. Intentelo nuevamente')	

		try:
			a=float(sp.sympify(self.entrada_ini_dom.get()))
			b=float(sp.sympify(self.entrada_end_dom.get()))
		except:
			messagebox.showwarning('Error', 'El domínio de su función esta incompleto, inténtelo nuevamente')

		try:	
			minimos=md.minimos(point_crit,second_deri,f_num,a,b)
			self.salida_minimos.delete('1.0',END)
			self.salida_minimos.insert(END, str(minimos))
		except:
			pass

		

#-------------comando de boton para calcular puntos de inflexion-------------------------#
	def punt_inflex(self):
		try:
			f=sp.sympify(self.entrada_f.get())
			x=sp.symbols(self.entrada_x.get())

			f_num=sp.lambdify(x,md.derivada(2,f,x)[0])
			second_deri=sp.lambdify(x,md.derivada(2,f,x)[2])
			point_inflex=sp.solve(md.derivada(2,f,x)[2],x)
		except:
			messagebox.showwarning('Error', 'No ha ingresado la función o la variable independiente. Intentelo nuevamente')	

		try:
			a=float(sp.sympify(self.entrada_ini_dom.get()))
			b=float(sp.sympify(self.entrada_end_dom.get()))
		except:
			messagebox.showwarning('Error', 'El domínio de su función esta incompleto, inténtelo nuevamente')

		try:
			puntos_inflex=md.exist_puntinflex(point_inflex,second_deri,f_num,a,b)
			self.salida_puntos_de_inflexion.delete('1.0', END )
			self.salida_puntos_de_inflexion.insert(END, str(puntos_inflex))
		except:
			pass

		


#-------------comando de boton para hallar intervalos de crecimiento-------------------------#
	def interval_cre(self):
		try:
			f=sp.sympify(self.entrada_f.get())
			x=sp.symbols(self.entrada_x.get())

			f_num=sp.lambdify(x,md.derivada(2,f,x)[0])
			first_deri=sp.lambdify(x,md.derivada(2,f,x)[1])
			point_crit=sp.solve(md.derivada(2,f,x)[1],x)
		except:
			messagebox.showwarning('Error', 'No ha ingresado la función o la variable independiente. Intentelo nuevamente')	

		try:
			a=float(sp.sympify(self.entrada_ini_dom.get()))
			b=float(sp.sympify(self.entrada_end_dom.get()))
		except:
			messagebox.showwarning('Error', 'El domínio de su función esta incompleto, inténtelo nuevamente')

		try:
			int_cre=md.intervalo_de_cre(point_crit,first_deri,f_num,a,b)
			self.salida_interval_cre.delete('1.0', END )
			self.salida_interval_cre.insert(END, str(int_cre))
		except:
			pass

		

 

#-------------comando de boton para hallar intervalos de decrecimiento-------------------------#
	def interval_decre(self):
		try:
			f=sp.sympify(self.entrada_f.get())
			x=sp.symbols(self.entrada_x.get())

			f_num=sp.lambdify(x,md.derivada(2,f,x)[0])
			first_deri=sp.lambdify(x,md.derivada(2,f,x)[1])
			point_crit=sp.solve(md.derivada(2,f,x)[1],x)
		except:
			messagebox.showwarning('Error', 'No ha ingresado la función o la variable independiente. Intentelo nuevamente')	

		try:
			a=float(sp.sympify(self.entrada_ini_dom.get()))
			b=float(sp.sympify(self.entrada_end_dom.get()))
		except:
			messagebox.showwarning('Error', 'El domínio de su función esta incompleto, inténtelo nuevamente')	

		try:
			int_decre=md.intervalo_de_decre(point_crit,first_deri,f_num,a,b)
			self.salida_interval_decre.delete('1.0', END )
			self.salida_interval_decre.insert(END, str(int_decre))
		except:
			pass





#-------------comando de boton para graficar f(x) y sus derivadas-------------------------#
	def grafica_f(self):
		try:
			f=sp.sympify(self.entrada_f.get())
			x=sp.symbols(self.entrada_x.get())

			f_num=sp.lambdify(x,md.derivada(2,f,x)[0])
			first_deri=sp.lambdify(x,md.derivada(2,f,x)[1])
			second_deri=sp.lambdify(x,md.derivada(2,f,x)[2])
		except:
			messagebox.showwarning('Error', 'No ha ingresado la función o la variable independiente. Intentelo nuevamente')	

		try:
			a=float(sp.sympify(self.entrada_ini_dom.get()))
			b=float(sp.sympify(self.entrada_end_dom.get()))
			dom=np.arange(a,b,0.01)
		except:
			messagebox.showwarning('Error', 'El domínio de su función esta incompleto, inténtelo nuevamente')

		try:
			mg.graficador(dom,f,x,f_num,first_deri,second_deri)
		except:
			pass



#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\  CLASE INTERFAZ TRIGONOMETRICAS  /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\#


class interfaz_trigonometricas_y_sus_derivadas:
	"""docstring for interfaz_funciones_y_sus_derivadas"""
	def __init__(self, funciones):

		"""pedimos al usuario la variable independiente de f(x)"""
		self.etiqueta_x =Label(funciones, text= 'INGRESE LA VARIABLE INDEPENDIENTE DE F(x)', fg='green')
		self.etiqueta_x.place(x=200, y=30)
		self.entrada_x=Entry(funciones,width=5)
		self.entrada_x.config(justify='center')
		self.entrada_x.place(x=290, y=60)


		"""pedimos al usuario la funcion"""
		self.etiqueta_f=Label(funciones, text= 'INGRESE LA FUNCIÓN', fg='green')
		self.etiqueta_f.place(x=520, y=30)
		self.entrada_f=Entry(funciones, width=30)
		self.entrada_f.config(justify='center')
		self.entrada_f.place(x=485, y=60)


		"""pedimos al usuario el inicio del dominio"""
		self.etiqueta_ini_dom=Label(funciones, text= 'INGRESE EL INICIO DEL DOMÍNIO', fg='green')
		self.etiqueta_ini_dom.place(x=225, y=90)
		self.entrada_ini_dom=Entry(funciones, width=10)
		self.entrada_ini_dom.config(justify='center')
		self.entrada_ini_dom.place(x=275, y=120)


		"""pedimos al usuario el fin del dominio"""
		self.etiqueta_end_dom=Label(funciones, text= 'INGRESE EL FINAL DEL DOMÍNIO', fg='green')
		self.etiqueta_end_dom.place(x=495, y=90)
		self.entrada_end_dom=Entry(funciones, width=10)
		self.entrada_end_dom.config(justify='center')
		self.entrada_end_dom.place(x=540, y=120)


#%%%%%%%%%%%%%%%%%%%%%%%%%% BOTON MAXIMOS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#
		"""creamos el boton para hallar los maximos"""
		self.Boton_maximos=Button(funciones, text='calcular puntos maximos', fg='blue' ,cursor='pirate', command=self.boton_maximos)
		self.Boton_maximos.place(x=80, y=160)

		"""mostramos en pantalla los maximos de la funcion"""
		self.etiqueta_salida_maximos=Label(funciones, text='Los puntos maximos de f(x) son: ')
		self.etiqueta_salida_maximos.place(x=65, y=190)
		self.salida_maximos=Text(funciones, width=30, height=3)
		self.salida_maximos.place(x=30, y=220)


#%%%%%%%%%%%%%%%%%%%%%%%%%% BOTON MINIMOS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#
		"""creamos el boton para hallar los minimos"""
		self.Boton_minimos=Button(funciones, text='calcular puntos minimos', fg='blue' ,cursor='pirate', command=self.boton_minimos)
		self.Boton_minimos.place(x=370, y=160)

		"""mostramos en pantalla los minimos de la funcion"""
		self.etiqueta_salida_minimos=Label(funciones, text='Los puntos minimos de f(x) son: ')
		self.etiqueta_salida_minimos.place(x=355, y=190)
		self.salida_minimos=Text(funciones, width=30, height=3)
		self.salida_minimos.place(x=320, y=220)


#%%%%%%%%%%%%%%%%%%%%%%%%%% BOTON PUNTOS DE INFLEXION %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#
		"""creamos el boton para hallar los puntos de inflexion"""
		self.Boton_puntos_de_inflexion=Button(funciones, text='calcular puntos de inflexion', fg='blue' ,cursor='pirate', command=self.punt_inflex)
		self.Boton_puntos_de_inflexion.place(x=655, y=160)

		"""mostramos en pantalla los puntos de inflexion"""
		self.etiqueta_salida_puntos_de_inflexion=Label(funciones, text='Los puntos de inflexion de f(x) son: ')
		self.etiqueta_salida_puntos_de_inflexion.place(x=640, y=190)
		self.salida_puntos_de_inflexion=Text(funciones, width=30, height=3)
		self.salida_puntos_de_inflexion.place(x=610, y=220)


#%%%%%%%%%%%%%%%%%%%%%%%%%% BOTON INTERVALOS DE CRECIMIENTO %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#
		"""creamos el boton para hallar los intervalos de crecimiento"""
		self.Boton_interval_cre=Button(funciones, text='calcular intervalos de crecimiento', fg='blue',cursor='pirate', command=self.interval_cre )
		self.Boton_interval_cre.place(x=60, y=280)

		"""mostramos en pantalla los intervalos de crecimiento"""
		self.etiqueta_salida_interval_cre=Label(funciones, text='Los intervalos de crecimiento de f(x) son: ')
		self.etiqueta_salida_interval_cre.place(x=40, y=310)
		self.salida_interval_cre=Text(funciones, width=30, height=3)
		self.salida_interval_cre.place(x=30, y=340)

#%%%%%%%%%%%%%%%%%%%%%%%%%% BOTON INTERVALOS DE DECRECIMIENTO %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#
		"""creamos el boton para hallar los intervalos de decrecimiento"""
		self.Boton_interval_cre=Button(funciones, text='calcular intervalos de decrecimiento', fg='blue' ,cursor='pirate', command=self.interval_decre)
		self.Boton_interval_cre.place(x=340, y=280)

		"""mostramos en pantalla los intervalos de decrecimiento"""
		self.etiqueta_salida_interval_decre=Label(funciones, text='Los intervalos de decrecimiento de f(x) son: ')
		self.etiqueta_salida_interval_decre.place(x=325, y=310)
		self.salida_interval_decre=Text(funciones,width=30, height=3)
		self.salida_interval_decre.place(x=320, y=340)

#%%%%%%%%%%%%%%%%%%%%%%%%%% BOTON GRAFICA DE F(X) Y SUS DERIVADAS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#
		self.etiqueta_grafica=Label(funciones, text= 'Si presiona el botón "GRAFICAR", verá una ventana con')
		self.etiqueta_grafica1=Label(funciones, text= 'la gráfica de la función que ingresó y sus dos derivadas.')
		self.etiqueta_grafica.place(x=600,y=290)
		self.etiqueta_grafica1.place(x=600,y=310)

		"""creamos el boton para graficar la funcion y sus derivadas"""
		self.Boton_grafica=Button(funciones, text='GRAFICAR f(x) Y SUS DERIVADAS', fg='blue' ,cursor='pirate', command=self.grafica_f)
		self.Boton_grafica.place(x=640, y=345)

#-------------comando de boton para calcular maximos-------------------------#
	def boton_maximos(self):
		try:
			f=sp.sympify(self.entrada_f.get())
			x=sp.symbols(self.entrada_x.get())

			f_num=sp.lambdify(x,ep.derivada(2,f,x)[0])
			second_deri=sp.lambdify(x,ep.derivada(2,f,x)[2])
		except:
			messagebox.showwarning('Error', 'No ha ingresado la función o la variable independiente. Intentelo nuevamente')	

		try:
			a=float(sp.sympify(self.entrada_ini_dom.get()))
			b=float(sp.sympify(self.entrada_end_dom.get()))

		except:
			messagebox.showwarning('Error', 'El domínio de su función esta incompleto, inténtelo nuevamente')

		try:
			point_crit=sp.solveset(ep.derivada(2,f,x)[1],x,domain=sp.Interval(a,b))
			maximos=ep.maximos(point_crit,second_deri,f_num,a,b)
			self.salida_maximos.delete('1.0', END )
			self.salida_maximos.insert(END, str(maximos))
		except:
			pass

		

#-------------comando de boton para calcular minimos-------------------------#
	def boton_minimos(self):
		try:
			f=sp.sympify(self.entrada_f.get())
			x=sp.symbols(self.entrada_x.get())

			f_num=sp.lambdify(x,ep.derivada(2,f,x)[0])
			second_deri=sp.lambdify(x,ep.derivada(2,f,x)[2])
		except:
			messagebox.showwarning('Error', 'No ha ingresado la función o la variable independiente. Intentelo nuevamente')	
		
		try:
			a=float(sp.sympify(self.entrada_ini_dom.get()))
			b=float(sp.sympify(self.entrada_end_dom.get()))
		except:
			messagebox.showwarning('Error', 'El domínio de su función esta incompleto, inténtelo nuevamente')

		try:	
			point_crit=sp.solveset(ep.derivada(2,f,x)[1],x,domain=sp.Interval(a,b))
			minimos=ep.minimos(point_crit,second_deri,f_num,a,b)
			self.salida_minimos.delete('1.0', END )
			self.salida_minimos.insert(END, str(minimos))
		except:
			pass

		

#-------------comando de boton para calcular puntos de inflexion-------------------------#
	def punt_inflex(self):
		try:	
			f=sp.sympify(self.entrada_f.get())
			x=sp.symbols(self.entrada_x.get())

			f_num=sp.lambdify(x,ep.derivada(2,f,x)[0])
			second_deri=sp.lambdify(x,ep.derivada(2,f,x)[2])
		except:
			messagebox.showwarning('Error', 'No ha ingresado la función o la variable independiente. Intentelo nuevamente')	

		try:
			a=float(sp.sympify(self.entrada_ini_dom.get()))
			b=float(sp.sympify(self.entrada_end_dom.get()))
		except:
			messagebox.showwarning('Error', 'El domínio de su función esta incompleto, inténtelo nuevamente')


		try:	
			point_inflex=sp.solveset(ep.derivada(2,f,x)[2],x,domain=sp.Interval(a,b))
			puntos_inflex=ep.exist_puntinflex(point_inflex,second_deri,f_num,a,b)
			self.salida_puntos_de_inflexion.delete('1.0', END )
			self.salida_puntos_de_inflexion.insert(END, str(puntos_inflex))
		except:
			pass

		


#-------------comando de boton para hallar intervalos de crecimiento-------------------------#
	def interval_cre(self):
		try:
			f=sp.sympify(self.entrada_f.get())
			x=sp.symbols(self.entrada_x.get())

			f_num=sp.lambdify(x,ep.derivada(2,f,x)[0])
			first_deri=sp.lambdify(x,ep.derivada(2,f,x)[1])
		except:
			messagebox.showwarning('Error', 'No ha ingresado la función o la variable independiente. Intentelo nuevamente')	

		try:
			a=float(sp.sympify(self.entrada_ini_dom.get()))
			b=float(sp.sympify(self.entrada_end_dom.get()))
		except:
			messagebox.showwarning('Error', 'El domínio de su función esta incompleto, inténtelo nuevamente')

		try:	
			point_crit=sp.solveset(ep.derivada(2,f,x)[1],x,domain=sp.Interval(a,b))
			int_cre=ep.intervalo_de_cre(point_crit,first_deri,f_num,a,b)
			self.salida_interval_cre.delete('1.0', END )
			self.salida_interval_cre.insert(END, str(int_cre))
		except:
			pass

		



#-------------comando de boton para hallar intervalos de decrecimiento-------------------------#
	def interval_decre(self):
		try:
			f=sp.sympify(self.entrada_f.get())
			x=sp.symbols(self.entrada_x.get())

			f_num=sp.lambdify(x,ep.derivada(2,f,x)[0])
			first_deri=sp.lambdify(x,ep.derivada(2,f,x)[1])
		except:
			messagebox.showwarning('Error', 'No ha ingresado la función o la variable independiente. Intentelo nuevamente')	
		
		try:
			a=float(sp.sympify(self.entrada_ini_dom.get()))
			b=float(sp.sympify(self.entrada_end_dom.get()))
		except:
			messagebox.showwarning('Error', 'El domínio de su función esta incompleto, inténtelo nuevamente')

		try:
			point_crit=sp.solveset(ep.derivada(2,f,x)[1],x,domain=sp.Interval(a,b))
			int_decre=ep.intervalo_de_decre(point_crit,first_deri,f_num,a,b)
			self.salida_interval_decre.delete('1.0', END )
			self.salida_interval_decre.insert(END, str(int_decre))
		except:
			pass

		



#-------------comando de boton para graficar f(x) y sus derivadas-------------------------#
	def grafica_f(self):
		try:
			f=sp.sympify(self.entrada_f.get())
			x=sp.symbols(self.entrada_x.get())

			f_num=sp.lambdify(x,ep.derivada(2,f,x)[0])
			first_deri=sp.lambdify(x,ep.derivada(2,f,x)[1])
			second_deri=sp.lambdify(x,ep.derivada(2,f,x)[2])
		except:
			messagebox.showwarning('Error', 'No ha ingresado la función o la variable independiente. Intentelo nuevamente')	

		try:
			a=float(sp.sympify(self.entrada_ini_dom.get()))
			b=float(sp.sympify(self.entrada_end_dom.get()))
			dom=np.arange(a,b,0.01)
		except:
			messagebox.showwarning('Error', 'El domínio de su función esta incompleto, inténtelo nuevamente')
		
		try:
			mg.graficador_trigonometricas(dom,f,x,f_num,first_deri,second_deri)
		except:
			pass

#=====================================SE EJECUTA EL PROGRAMA CON LAS DOS INTERFACES=====================================#

def interfaz2():
	var_chk=var.get()
	if var_chk==1:
		raiz.destroy()
		global wd
		wd=Tk()
		wd.geometry('930x600')
		wd.title("ANÁLISIS FUNCIONES TRIGONOMÉTRICAS")
		wd.resizable(0,0)

		interfaz2=Frame(wd)
		interfaz2.pack(side='bottom')
		interfaz2.config(width=930, height=520)

		label=Label(wd, text='ANÁLISIS DE FUNCIONES TRIGONOMÉTRICAS' ,font=100)
		label.place(x=300, y=10)

		label1=Label(wd, text="PARA EMPEZAR:", font=(9), fg='red')
		label2=Label(wd, text="Dé en ACEPTAR")
		label1.place(x=30,y=50)
		label2.place(x=50,y=70)

		boton_trigo=Button(wd, text='ACEPTAR', fg='red',command=interfaz4, cursor='pirate')
		boton_trigo.place(x=60, y=90)

		interfaz_trigonometricas_y_sus_derivadas(interfaz2)

		botoncierre=Button(interfaz2,text='INICIO', fg='green', cursor='pirate', command=INTERFAZ)
		botoncierre.place(x=440, y=450)

		botoncierre=Button(interfaz2,text='CERRAR', fg='green', cursor='pirate', command=wd.destroy)
		botoncierre.place(x=340, y=450)

		label4=Label(interfaz2, text='© Copyright 2020, Grupo Programación Python')
		label4.place(x=540, y=430)
		label5=Label(interfaz2, text='Proyecto Grupo 1, Interfaces Gráficas y Derivadas')
		label5.place(x=540, y=450)
		label6=Label(interfaz2, text='Maicol Vargas')
		label6.place(x=840, y=430)
		label7=Label(interfaz2, text='Alejandro Umaña')
		label7.place(x=820, y=450)
		label8=Label(interfaz2, text='Camilo Rivera')
		label8.place(x=840, y=470)
		label9=Label(interfaz2, text='La Gloriosa:')
		label9.place(x=640, y=470)
		label9=Label(interfaz2, text='UNIVERSIDAD DEL VALLE')
		label9.place(x=610, y=490)

		messagebox.showinfo('Manual de Usuario - Funciones Trigonométricas', 'BIENVENIDO' + "\n" +"\n" +'Ésta es la sección especial para funciones trigonométricas, desarrollada '+
							'con el objetivo de analizar dichas funciones de forma amena y organizada, obteniendo un resultado más que correcto, acertado ' + 
							'y estrechamente vinculado con las funciones trigonométricas. El proceso de análisis de estas funciones require también las dos '+
							'derivadas de la función en cuestion, para intentar calcular los máximos, mínimos, puntos de inflexión, e intervalos de crecimiento '+ 
							'y decrecimiento.'+"\n" +"\n" +'RECOMENDACIONES'+ "\n" +'Tenga en cuenta que:'+ "\n" +"\n" +'* lo anterior esta ligado al domínio '+ 
							'que el usuario ingresese; esto permite que el usuario decida que porción de la función desea analzar, sin embargo no puede ser '+ 
							'muy útil al momento de analizar la función en el conjunto de todos los reales.'+ "\n" +"\n" +'* En principio esta sección esta '+
							'diseñada para analizar las funciones seno, coseno, tangente y sus reespectivas inversas, sin embargo:'+ "\n" +"\n" +'  * La versión '+
							'de este programa no esta en la suficiente capacidad para interpretar y analizar las asíntotas de la función tangente.'+ "\n" +"\n" +
							'  *  La versión de este programa no esta en la suficiente capacidad para interpretar y analizar los puntos de inflexión de las reespectivas '+
							'inversas de las funciones seno y coseno.'+ "\n" +"\n" +'  * La versión de este programa no esta en la suficiente capacidad para '+
							'analizar e interpretar algunas funciones compuestas.'+ "\n" +"\n" +'  * La versión de este programa no esta en la suficiente capacidad para '+
							'graficar correctamente las funciones tangente, arcocoseno, y arcoseno.'+ "\n" +"\n" +'Pedimos disculpas por los posibles inconvenietes, '+
							'estaremos trabajando en ellos.')
		wd.mainloop()

		
		
	else:
		messagebox.showinfo('Error','No rellenó el botón, inténtelo nuevamente')

def interfaz3():
		messagebox.showinfo('información Importante', 'INFORMACIÓN IMPORTANTE'+ "\n" +"\n" +'° La multiplicación se representa con: *'+ "\n" +"\n" +
							'° La potencia se representa con: **'+ "\n" +"\n" +'° El cociente se representa con: /'+ "\n" +"\n" +'° La raíz se representa '+
							'con: sqrt(x)'+ "\n" +"\n" +'° La función exponencial se representa con: exp(x)'+ "\n" +"\n" +'° El número pi se representa con: pi')
def interfaz4():
	messagebox.showinfo('información Importante', 'INFORMACIÓN IMPORTANTE'+ "\n" +"\n" +'° La multiplicación se representa con: *'+ "\n" +"\n" +
							'° La potencia se representa con: **'+ "\n" +"\n" +'° El cociente se representa con: /'+ "\n" +"\n" +'° La raíz se representa '+
							'con: sqrt(x)'+ "\n" +"\n" +'° La función exponencial se representa con: exp(x)'+ "\n" +"\n" +'° El número pi se representa con: pi'+ "\n" +"\n" +
							'° La función seno se representa con: sin(x)'+ "\n" +"\n" +'° La función coseno se representa con: cos(x)'+ "\n" +"\n" +
							'° La función tangente se representa con: tan(x)'+ "\n" +"\n" +'° La función arcoseno se representa con: asin(x)'+ "\n" +"\n" +
							'° La función arcocoseno se representa con: acos(x)'+ "\n" +"\n" +'° La función arcotangente se representa con: atan(x)')

def INTERFAZ():
	global raiz
	try:
		wd.destroy()
	except:
		pass 
	raiz=Tk()
	raiz.geometry('930x690')
	raiz.title("ANÁLISIS DE FUNCIONES")
	raiz.resizable(0,0)

	label=Label(raiz, text='ANÁLISIS DE FUNCIONES CONTÍNUAS Y TRIGONOMÉTRICAS' ,font=100)
	label.place(x=220, y=10)

	label1=Label(raiz, text="PARA ANALIZAR FUNCIONES TRIGONOMÉTRICAS:", font=(9), fg='green') 
	label2=Label(raiz, text="rellene el botón y dé en ACEPTAR")
	label1.place(x=80,y=50)
	label2.place(x=170,y=72)

	label1=Label(raiz, text="PARA ANALIZAR FUNCIONES POLINÓMICAS:", font=(9), fg='blue')
	label2=Label(raiz, text="Dé en ACEPTAR")
	label1.place(x=500,y=50)
	label2.place(x=600,y=72)

	global var
	var=IntVar()
	chk=Checkbutton(raiz, variable=var , bd=2, fg='green' ,onvalue=1, offvalue=0)
	chk.place(x=355, y=72)

	boton_trigo=Button(raiz, text='ACEPTAR', fg='green',command=interfaz2, cursor='pirate')
	boton_trigo.place(x=230, y=92)

	boton_poli=Button(raiz, text='ACEPTAR', fg='blue',command=interfaz3, cursor='pirate')
	boton_poli.place(x=610, y=92)

	interfaz=Frame(raiz)
	interfaz.pack(side='bottom')
	interfaz.config(width=930, height=520)

	label3=Label(interfaz, text='ANÁLISIS DE FUNCIONES CONTÍNUAS', font=12)
	label3.place(x=290, y=0)

	interfaz_funciones_y_sus_derivadas(interfaz)

	botoncierre=Button(interfaz, text='CERRAR',fg='blue', command=raiz.destroy, cursor='pirate')
	botoncierre.place(x=420,y=450)

	label4=Label(interfaz, text='© Copyright 2020, Grupo Programación Python')
	label4.place(x=540, y=430)
	label5=Label(interfaz, text='Proyecto, Interfaces Gráficas y Derivadas')
	label5.place(x=540, y=450)
	label6=Label(interfaz, text='Maicol Vargas')
	label6.place(x=840, y=430)
	label9=Label(interfaz, text='La Gloriosa:')
	label9.place(x=640, y=470)
	label9=Label(interfaz, text='UNIVERSIDAD DEL VALLE')
	label9.place(x=610, y=490)

	messagebox.showinfo('Manual de Usuario - Funciones Contínuas', 'BIENVENIDO' + "\n" +"\n" +'Éste es un programa desarrollado con el objetivo de analizar funciones ' + 
						'polinómicas, constantes, identidad, exponencial, radicales, y trigonométricas a través de su primera y segunda derivada '+
						'calculando en caso de que posea, los puntos máximos y mínimos locales de dicha función, además de sus puntos de inflexión '+
						'e intervalos de crecimiento y decrecimiento; además graficar dicha función.' + "\n" +"\n" + 'RECOMENDACIONES'+ "\n"+
						'Tenga en cuenta que:'+ "\n" +"\n"+'* lo anterior esta ligado al domínio que el usuario ingresese; esto permite que el usuario '+
						'decida que porción de la función desea analzar, sin embargo no puede ser muy útil al momento de analizar la función en el '+
						'conjunto de todos los reales.'+ "\n" +"\n"+ '* El programa no cuenta con la estructura y capacidad necesaria para analizar '+
						'funciones racionlaes. '+ "\n" +"\n"+ '* El programa no cuenta con la estructura y capacidad necesaria para analizar '+
						'funciones a trozos.'+ "\n" +"\n"+ '* El programa no cuenta con la estructura y capacidad necesaria para analizar '+
						'algunas funciones compuestas.'+ "\n" +"\n"+ '* El domínio ingresado se toma como un intervalo abierto, lo que implica que se toman '+
						'todas las propiedades de un intervalo abierto y además en el caso de una función toda creciente o decreciente no se tomaran los '+
						'extremos del intervalo como puntos máximos o mínimos por defecto, de la función en cuestion.'+ "\n" +"\n"+'* Se ha elaborado una sección especial '+
						'y únicamente para funciones trigonométricas dado que estas funciones requieren de manejo un poco distinto. A dicha sección puede acceder '+
						'desde un botón en el encabezado del programa.'+ "\n" +"\n"+'* Recomendamos firmemente, no intentar analizar funciones trigonométricas fuera de su '+
						'sección especial, a decir, en la sección para funciones polinómicas, o funciones polinómicas en la sección de trigonométricas, dado que '+
						'la información que se pueda obtener podría ser no fidedigna.'+"\n" +"\n"+'AGRADECIMIENTOS'+"\n"+
						'Ante todo, damos gracias a Dios por ayudarnos y permitirnos entregar este Proyecto, damos infinitas gracias al Dr. Leon Escobar por '+
						'su labor como docente, en el aula o desde su casa; y damos infinitas gracias a la gloriosa UNIVERSIDAD DEL VALLE por la educación '+
						'de alta calidad que brinda y de la cual hacemos parte.')
	raiz.mainloop()
	
INTERFAZ()


"""
var_chk=IntVar()
chk=Checkbutton(raiz, text='Si desea analisar funciones trigonometricas de click aquí', variable=var_chk, onvalue=1, offvalue=0)
chk.place(x=70,y=70)
get_chk=var_chk.get()
interfaz=Frame(raiz)
interfaz.pack(side='bottom')
interfaz.config(width=600, height=600)
interfaz_funciones_y_sus_derivadas(interfaz)"""

"""def validar():
	if get_chk==1:
		abrirventana2()
	else:
		messagebox.showwarning('cuidado, no relleno el boton')"""

"""if get_chk==1:
	raiz=Tk()
	raiz.geometry('600x700')
	raiz.title("ANALISIS DE FUNCIONES")
	raiz.resizable(0,0)
	raiz.mainloop()
	interfaz=Frame(raiz)
	interfaz.pack(side='bottom')
	interfaz.config(width=600, height=600)
	interfaz_trigonometricas_y_sus_derivadas(interfaz)
	
	interfaz.mainloop()
raiz.mainloop()"""

		

"""x=sp.symbols(input("introduzca la variable independiente de f(x): "))
f_string=input("introduzca la funcion en terminos de la variable independiente : ")
orden=int(input("hasta que orden desea diferenciar la funcion: "))
a=float(sp.sympify(input("ingrese el numero donde desea que empiece el dominio de f(x): ")))
b=float(sp.sympify(input("ingrese el numero donde desea que termine el dominio de f(x): ")))

#(1/3)*x**3-x**2-3*x+4,-2*x**3 + (1/x**2)

dom=np.arange(a,b,0.01)
f=sp.sympify(f_string)
#f=(1/3)*x**3-x**2-3*x+4, (1/4)*x**4-4*x**2
print("f(x) y sus derivadas son: ","\n", md.derivada(orden,f,x))

f_num=sp.lambdify(x,md.derivada(2,f,x)[0])
first_deri=sp.lambdify(x,md.derivada(2,f,x)[1])
second_deri=sp.lambdify(x,md.derivada(2,f,x)[2])

#----------------CALCULAMOS LOS PUNTOS DONDE LA DERIVADA SE HACE CERO--------------#
point_crit=sp.solve(md.derivada(2,f,x)[1],x)
point_inflex=sp.solve(md.derivada(2,f,x)[2],x)
print(point_crit)
print(point_inflex)

print("SEGUN EL DOMINIO DADO, SE PRESENTA LA SIGUIENTE INFORMACION: ", "\n")
print("puntos maximos: ",md.maximos(point_crit,second_deri,f_num,a,b))
print("puntos minimos: ",md.minimos(point_crit,second_deri,f_num,a,b))
input()
#md.exist_extremos(point_crit,second_deri,f_num,a,b)
#input()
print("puntos de inflexion: ",md.exist_puntinflex(point_inflex,second_deri,f_num,a,b))
input()
print("intervalos de crecimiento: ",md.intervalo_de_cre(point_crit,first_deri,f_num,a,b))
input()
print("intervalos de decrecimiento: ",md.intervalo_de_decre(point_crit,first_deri,f_num,a,b))
input()
mg.graficador(dom,f,x,f_num,first_deri,second_deri)"""