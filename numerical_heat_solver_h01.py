#temperature generator/plotter as calculated numerically for h=0.1
import numpy as np
import matplotlib.pyplot as plt

A = np.zeros((95, 95))

#set diagonal to -4
for i in range(0, 95):
    for j in range(0, 95):
        if i == j:
            A[i, j] = -4

for i in range(0, 95):
    for j in range(0, 95):
        if j == i-1 and i%5 != 0 and (i+1)%5 != 0:
            A[i,j] = 1
        elif j ==i-1 and (i+1)%5 == 0:
            A[i,j] = 2

for i in range(0, 95):
    for j in range(0, 95):
        if j == i-5:
            A[i,j] = 1

for i in range(0, 95):
    for j in range(0, 95):
        if j == i+1 and (i+1)%5 != 0:
            A[i,j] = 1

for i in range(0, 95):
    for j in range(0, 95):
        if j == i+5:
            A[i,j] = 1

b = np.zeros(95)

b[90] = -.09
b[91] = -.16
b[92] = -.21
b[93] = -.24
b[94] = -.25

y = np.linalg.solve(A, b)
Y = y.reshape(19, 5)

#create coord. grid
T = np.zeros((21, 11))

#add BC on y=2
for j in range(0,11):
    T[20,j] = 0.1*j*(1-(0.1*j))

#add solution from Ay=b
for i in range(1,20):
    for j in range(1, 6):
        T[i,j] = Y[i-1, j-1]

#add BC of reflection about x = 0.5
for i in range(1,20):
    for j in range(1, 6):
        T[i, j+5] = T[i, 5-j]

x = np.linspace(0, 1, 11)
y = np.linspace(0, 2, 21)
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

np.set_printoptions(threshold=np.inf)
print(T)



