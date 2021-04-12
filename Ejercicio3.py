import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-2., 5., 0.2)
y = (2+x)/2

plt.plot([],[],color='aquamarine', label='Región Solución', linewidth=5)

plt.plot(x , y , 'r--')

plt.fill_between(x,y,5, color='aquamarine')

plt.title('Ejercicio 3')
plt.ylabel('y')
plt.xlabel('x')
plt.legend(loc='lower right')

plt.show()