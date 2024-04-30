#temperature generator/plotter as calculated numerically for h=0.25
import numpy as np
import matplotlib.pyplot as plt

#generate matrix with variables representing each point in grid (14 instead of 5*9 = 45 variables because of symmetries and boundary conditions)

A = np.zeros((14, 14))

#set diagonal to -4
for i in range(0, 14):
    for j in range(0, 14):
        if i == j:
            A[i, j] = -4

for i in range(0, 14):
    for j in range(0, 14):
        if j == i-2:
            A[i, j] = 1

for i in range(0, 14):
    for j in range(0, 14):
        if j == i-1 and (i+1)%2 ==0:
            A[i,j] = 2

for i in range(0, 14):
    for j in range(0, 14):
        if j == i+2:
            A[i,j] = 1

for i in range(0, 14):
    for j in range(0, 14):
        if j== i+1 and (j+1)%2==0:
            A[i,j] = 1

b = np.zeros(14)

b[12] = -.1875
b[13] = -.25
#get solution column vector
y = np.linalg.solve(A, b)

#reshape col vec to be put in matrix representing x, y coordinates
Y = y.reshape(7, 2)

#create matrix representing x, y, coords
T = np.zeros((9, 5))

#set boundary condition on top of grid
for j in range(0,5):
    T[8,j] = 0.25*j*(1-(0.25*j))

#insert solution of A&b into temp grid
for i in range(1,8):
    for j in range(1, 3):
        T[i,j] = Y[i-1, j-1]

#reflect values about x=0.5 (symmetry BC)
for i in range(1,8):
    T[i, 3] = T[i, 1]


x = np.linspace(0, 1, 5)
y = np.linspace(0, 2, 9)
X, Y = np.meshgrid(x, y)

plt.pcolormesh(X, Y, T, shading='auto')
plt.colorbar(label='Temperatue')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Temperature as Calculated Numerically')

for i in range(len(x)):
    for j in range(len(y)):
        plt.text(x[i], y[j], f'{T[j, i]:.2f}', ha='center', va='center')

plt.show()



print(T)
