import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0., 5., 0.2)
y1 = 3-(2*x)
y2 = [1/2] * len(x)
y3 = x

plt.plot([],[],color='aquamarine', label='Región Solución', linewidth=5)
plt.plot([],[],color='m', label='Ecuación 1', linewidth=5)
plt.plot([],[],color='r', label='Ecuación 2', linewidth=5)
plt.plot([],[],color='g', label='Ecuación 3', linewidth=5)

plt.plot(x , y1 , 'm--')
plt.plot(x , y2 , 'r--')
plt.plot(x , y3 , 'g')

plt.fill_between(x,y3,y2, color='aquamarine', where=(y3>y1), interpolate=True)

plt.title('Ejercicio 4')
plt.ylabel('y')
plt.xlabel('x')
plt.legend(loc='lower left')

plt.show()