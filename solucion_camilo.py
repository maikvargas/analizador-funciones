import numpy as np
import sympy as sp 
import ensayo_interfaz as ep

x=sp.symbols(input("introduzca la variable independiente de f(x): "))
f=sp.sympify(input("introduzca la funcion en terminos de la variable independiente : "))
orden=int(input("hasta que orden desea diferenciar la funcion: "))
a=float(sp.sympify(input("ingrese el numero donde desea que empiece el dominio de f(x): ")))
b=float(sp.sympify(input("ingrese el numero donde desea que termine el dominio de f(x): ")))

#(1/3)*x**3-x**2-3*x+4,-2*x**3 + (1/x**2)
e=[a,b]
print(len(e))
dom=np.arange(a,b,0.01)
#f=(1/3)*x**3-x**2-3*x+4, (1/4)*x**4-4*x**2
print("f(x) y sus derivadas son: ","\n", ep.derivada(orden,f,x))

f_num=sp.lambdify(x,ep.derivada(2,f,x)[0])
first_deri=sp.lambdify(x,ep.derivada(2,f,x)[1])
second_deri=sp.lambdify(x,ep.derivada(2,f,x)[2])

#----------------CALCULAMOS LOS PUNTOS DONDE LA DERIVADA SE HACE CERO--------------#
point_crit=sp.solveset(ep.derivada(2,f,x)[1],x, domain=sp.Interval(a,b))
point_inflex=sp.solveset(ep.derivada(2,f,x)[2],x, domain=sp.Interval(a,b))
print(point_crit)
print(point_inflex)

print("SEGUN EL DOMINIO DADO, SE PRESENTA LA SIGUIENTE INFORMACION: ", "\n")

print("maximos: ",ep.maximos(point_crit,second_deri,f_num,a,b) )
print("minimos:", ep.minimos(point_crit,second_deri,f_num,a,b), "\n" )

print("puntos de inflexion:", ep.exist_puntinflex(point_inflex,second_deri,f_num,a,b), "\n")

print("intervalos de crecimiento:", ep.intervalo_de_cre(point_crit,first_deri,f_num,a,b) ,"\n")
print("intervalos de decrecimiento:", ep.intervalo_de_decre(point_crit,first_deri,f_num,a,b) )

#print("puntos maximos: ",md.maximos(point_crit,second_deri,f_num,a,b))
#print("puntos minimos: ",md.minimos(point_crit,second_deri,f_num,a,b))
#input()
#md.exist_extremos(point_crit,second_deri,f_num,a,b)
#input()
#print("puntos de inflexion: ",md.exist_puntinflex(point_inflex,second_deri,f_num,a,b))
#input()
#print("intervalos de crecimiento: ",md.intervalo_de_cre(point_crit,first_deri,f_num,a,b))
#input()
#print("intervalos de decrecimiento: ",md.intervalo_de_decre(point_crit,first_deri,f_num,a,b))
#input()
#mg.graficador(dom,f,x,f_num,first_deri,second_deri)




"""x=sp.symbols(input("introduzca la variable independiente de f(x): "))
f_string=input("introduzca la funcion en terminos de la variable independiente : ")
orden=int(input("hasta que orden desea diferenciar la funcion: "))
a=sp.sympify(input("ingrese el numero donde desea que empiece el dominio de f(x): "))
b=sp.sympify(input("ingrese el numero donde desea que termine el dominio de f(x): "))


dom=np.arange(a,b,0.01)
f=sp.sympify(f_string)
#f=(1/3)*x**3-x**2-3*x+4, (1/4)*x**4-4*x**2
print("f(x) y sus derivadas son: ","\n", md.derivada(orden,f,x), "\n")
   
f_num=sp.lambdify(x,md.derivada(2,f,x)[0])
first_deri=sp.lambdify(x,md.derivada(2,f,x)[1])
second_deri=sp.lambdify(x,md.derivada(2,f,x)[2])

#----------------CALCULAMOS LOS PUNTOS DONDE LA DERIVADA SE HACE CERO--------------#
#point_crit=sp.solveset(ei.derivada(2,f,x)[1],x,domain=sp.Interval(a,b))
#point_inflex=sp.solveset(ei.derivada(2,f,x)[2],x,domain=sp.Interval(a,b))

point_crit=sp.solve(md.derivada(2,f,x)[1],x)
point_inflex=sp.solve(md.derivada(2,f,x)[2],x)


print("raices de la primera derivada de la funcion que ud ingreso:", "\n",point_crit, "\n")
print("raices de la segunda derivada de la funcion que ud ingreso: ", "\n",point_inflex)

r=second_deri(point_crit)
t=second_deri(point_inflex)
print(r, "\n" )
print(t, "\n" )


input()
# , -2x**3 + 1/x**2
raiz=[]
for i in point_crit: 
	raiz.append(first_deri(i))     
print("primera derivada evaluada en las raices:", "\n",raiz, "\n")

raiz2=[]
for i in  point_inflex:
	raiz2.append(first_deri(i))     
print("primera derivada evaluada en las raices: ", "\n",raiz2)"""

"""print("SEGUN EL DOMINIO DADO, SE PRESENTA LA SIGUIENTE INFORMACION: ", "\n")
print("puntos maximos: ",md.maximos(point_crit,second_deri,f_num,a,b))"""