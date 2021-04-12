import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0., 150., 0.2)
y1 = (-2*x)+180
y2 = (-x+160)/2
y3 = -x+100
y4 = [0] * len(x)
y5 = [0] * len(x)

plt.plot([],[],color='aquamarine', label='Región Solución', linewidth=5)
plt.plot([],[],color='m', label='Ecuación 1', linewidth=5)
plt.plot([],[],color='r', label='Ecuación 2', linewidth=5)
plt.plot([],[],color='g', label='Ecuación 3', linewidth=5)
plt.plot([],[],color='orange', label='Ecuación 4', linewidth=5)
plt.plot([],[],color='y', label='Ecuación 5', linewidth=5)

plt.plot(x , y1 , 'm')
plt.plot(x , y2 , 'r')
plt.plot(x , y3 , 'g')
plt.plot(x , y4 , 'orange')
plt.plot(y5 , x , 'y')
plt.plot(40 , 60 , color='k' , marker='o')
plt.plot(0 , 0 , color='k' , marker='o')
plt.plot(90 , 0 , color='k' , marker='o')
plt.plot(80 , 20 , color='k' , marker='o')
plt.plot(0 , 80 , color='k' , marker='o')

plt.fill_between(x,y4,y3, color='aquamarine', interpolate=True)
plt.fill_between(x,y2,y3, color='w', interpolate=True)
plt.fill_between(x,y1,y3, color='w', interpolate=True)

plt.title('Ejercicio 6')
plt.ylabel('y')
plt.xlabel('x')

plt.text(40,60,'(40,60)',fontsize=10)
plt.text(0,0,'(0,0)',fontsize=10)
plt.text(90,0,'(90,0)',fontsize=10)
plt.text(80,20,'(80,20)',fontsize=10)
plt.text(0,80,'(0,80)',fontsize=10)
plt.text(20,-100,'MAX P(40,60)=520',fontsize=15)

plt.legend(loc='upper right')

plt.show()