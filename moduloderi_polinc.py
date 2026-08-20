import sympy as sp 
import numpy as np 

#----------------------calculamos las n derivadas que se desee--------------------#

def derivada(g,k,x):
	"""creamos una lista vacia, donde se agrega la funcion y las n derivadas
	que se haya deseado calcular, por lo que al final esta funcion,
	devuelve como valor un arreglo o lista de funciones constantes, continuas
	o polinomiales"""
	derivadas=[]
	i=0
	while i <=g:
		deri=sp.diff(k,x,i)
		i=i+1
		derivadas.append(deri)
	return derivadas
#----------------------calculamos los puntos maximos locales--------------------#

def maximos(k,q,w,a,b):
	"""calculamos los maximos de la funcion que ingreso el usuario, a partir de los ceros de la 
	primera derivada de la funcion de este"""
	lista_max=[]
	if k==[]:
		no_exist="f(x) no tiene extremos"
		return no_exist
	else:
		for i in k:
			"""con try: nos aseguramos que la funcion ingresada por el usuario
			no tenga en su primer derivada, raices complejas"""
			try:
				c=float(i)
				if a<=c and c<=b:
					second_deri_eval=q(c)
					if second_deri_eval<0:
						lista_max.append([c,float(w(c))])
					else:
						pass
				else:
					pass
			except:
				pass
	if lista_max==[]:
		no_exist="f(x) no tiene maximos"
		lista_max.append(no_exist)
	else:
		pass
	return lista_max

#-------------------calculamos los puntos minimos locales-------------------#

def minimos(k,q,w,a,b):
	lista_min=[]
	if k==[]:
		no_exist="f(x) no tiene extremos"
		return no_exist
	else:
		for i in k:
			try:
				c=float(i)
				if a<=c and c<=b:
					second_deri_eval=q(c)
					if second_deri_eval >0:
						lista_min.append([c,float(w(c))])
					else:
						pass
				else:
					pass
			except:
				pass
	if lista_min==[]:
		no_exist="f(x) no tiene minimos"
		lista_min.append(no_exist)
	else:
		pass
	return lista_min

#-----------------calculamos los puntos de inflexion---------------------#

def exist_puntinflex(k,q,w,a,b):
	
	lista_inflex=[]
	if k==[]:
		no_exist="f(x) no tiene puntos de inflexion"
		return no_exist
	else:
		for i in k:
			try:
				c=float(i)
				if a <= c and c <=b:
					if ( q(c-0.1) <0 and q(c+0.1) >0 ) or ( q(c-0.1) >0 and q(c+0.1) <0 ):
						lista_inflex.append([c,float(w(c))])
					else:
						pass
				else:
					pass 
			except:
				pass
	if lista_inflex==[]:
		no_exist="f(x) no tiene puntos de inflexion"
		lista_inflex.append(no_exist)
	else:
		pass
	return lista_inflex

#====================HALLAMOS LOS INTERVALOS DE CRECIMIENTO Y DECRECECIMIENTO DE LA FUNCION=================#
#-------------intervalos de crecimiento-------------------------------#
def intervalo_de_cre(k,q,w,a,b):
	crece=[]
	decrece=[]
	if k ==[]:
		if w(a)==w(b):
			const="f(x) es constante"
			return const
		elif w(a)<w(b):
			crece.append((a,b))
		else:
			decrece.append((a,b))
	else:
		inter_cre=[a,b]
		for l in k:
			try:
				c=float(l)				
				if a<=c and c<=b:
					inter_cre.append(c)
				for i in range(1,len(inter_cre)):
					for j in range(0,len(inter_cre)-1):
						if inter_cre[j] > inter_cre[j+1]:
							elemento=inter_cre[j]
							inter_cre[j]=inter_cre[j+1]
							inter_cre[j+1]=elemento

			except:
				pass
		i=0
		while i < len(inter_cre)-1:
			inter_vari=np.arange(float(inter_cre[i])+0.1, float(inter_cre[i+1])-0.1)
			crece_decrece=q(inter_vari)
			result=all(l<0 for l in crece_decrece)
			if result:
				decrece.append((inter_cre[i],inter_cre[i+1]))
			
			else:
				crece.append((inter_cre[i],inter_cre[i+1]))
			i+=1
	if crece==[]:
		no_exist="f(x) no tiene intervalos de crecimiento"
		return no_exist
	else:
		return crece
#-----------------intervalos de decrecimiento------------------------------------#
def intervalo_de_decre(k,q,w,a,b):
	crece=[]
	decrece=[]
	if k ==[]:
		if w(a)==w(b):
			const="f(x) es constante"
			return const
		elif w(a)>w(b):
			decrece.append((a,b))
		else:
			crece.append((a,b))
	else:
		inter_cre=[a,b]
		for l in k:
			try:
				c=float(l)				
				if a<=c and c<=b:
					inter_cre.append(c)
				for i in range(1,len(inter_cre)):
					for j in range(0,len(inter_cre)-1):
						if inter_cre[j] > inter_cre[j+1]:
							elemento=inter_cre[j]
							inter_cre[j]=inter_cre[j+1]
							inter_cre[j+1]=elemento
			except:
				pass
		i=0
		while i < len(inter_cre)-1:
			inter_vari=np.arange(float(inter_cre[i])+0.1, float(inter_cre[i+1])-0.1)
			crece_decrece=q(inter_vari)
			result=all(l<0 for l in crece_decrece)
			if result:
				decrece.append((inter_cre[i],inter_cre[i+1]))

			else:
				crece.append((inter_cre[i],inter_cre[i+1]))
				
			i+=1
	if decrece==[]:
		no_exist="f(x) no tiene intervalos de decrecimiento"
		return no_exist
	else:
		return decrece 










	
