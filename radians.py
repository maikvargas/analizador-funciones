import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

from basic_units import radians, acos, asin , atan ,sin , cos

x = [val*radians for val in np.arange(-4*sp.pi,4*sp.pi, 0.01)]

#fig, axs = plt.subplots(2)

#plt.plot(x, cos(x), xunits=radians)
plt.plot(x, sin(x), xunits=radians)
plt.title("GRAFICO DE UNA FUNCION Y SUS DERIVADAS :) ")
plt.legend()
plt.grid()

plt.show()
  