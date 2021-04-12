import matplotlib.pyplot as plt
import numpy as np

z = np.arange(0., 5/2, 0.2)
y = 5-(2*z)

plt.plot([],[],color='aquamarine', label='Región Solución', linewidth=5)

plt.stackplot(z , y , colors=['aquamarine'])
plt.plot(z , y , 'r--')

plt.title('Ejercicio 1')
plt.ylabel('y')
plt.xlabel('x')
plt.legend()

plt.show()