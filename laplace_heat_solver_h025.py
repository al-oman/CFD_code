#Laplace Equation Fourier Series Plotter (h=0.25)

import numpy as np
import matplotlib.pyplot as plt

def series_sum(x, y, sum_lim):
    S = 0
    for n in range(1, sum_lim+1):
        S = S+ (2*(-2*np.cos(np.pi*n)+2)*np.sin(n*np.pi*x)*np.sinh(np.pi*n*y))/(np.pi**3 * n**3 * np.sinh(2*np.pi*n))
    return S

x = np.linspace(0, 1, 5)
y = np.linspace(0, 2, 9)

#generate coordinate grid
X, Y = np.meshgrid(x, y)

#generate temperature grid, iterate sum 100 times
T = series_sum(X, Y, 100)

plt.pcolormesh(X, Y, T, shading='auto')
plt.colorbar(label='Temperatue')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Temperature as Calculated by Fourier Series')

for i in range(len(x)):
    for j in range(len(y)):
        plt.text(x[i], y[j], f'{T[j, i]:.2f}', ha='center', va='center')

plt.show()
