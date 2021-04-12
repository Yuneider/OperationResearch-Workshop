import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0., 5., 0.2)
y = [5] * len(x)

plt.plot([],[],color='aquamarine', label='Región Solución', linewidth=5)

plt.stackplot(x , y , colors=['aquamarine'])
plt.plot(x , y , 'c')


plt.title('Ejercicio 2')
plt.ylabel('y')
plt.xlabel('x')
plt.legend(loc='lower right')

plt.show()