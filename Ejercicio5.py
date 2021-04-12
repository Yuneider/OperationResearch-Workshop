import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0., 50., 0.2)
y1 = (60-(2*x))/6
y2 = [0] * len(x)
y3 = [0] * len(x)

plt.plot([],[],color='aquamarine', label='Región Solución', linewidth=5)
plt.plot([],[],color='m', label='Ecuación 1', linewidth=5)
plt.plot([],[],color='r', label='Ecuación 2', linewidth=5)
plt.plot([],[],color='g', label='Ecuación 3', linewidth=5)

plt.plot(x , y1 , 'm')
plt.plot(y2 , x , 'r')
plt.plot(x , y3 , 'g')

plt.fill_between(x,y2,y1, color='aquamarine', where=(y1>y3), interpolate=True)

plt.title('Ejercicio 5')
plt.ylabel('y')
plt.xlabel('x')
plt.legend(loc='upper right')

plt.show()