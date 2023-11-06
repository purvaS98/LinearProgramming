import matplotlib.pyplot as plt
import numpy as np

# Binary ILP constraints: x + y <= 1, x, y are binary variables
x = np.array([0, 1])
y = np.array([0, 1])

X, Y = np.meshgrid(x, y)
Z = X + Y

plt.figure(figsize=(6, 6))
plt.contourf(X, Y, Z, levels=[-1, 1], colors=('skyblue', 'white'))
plt.xlabel('x')
plt.ylabel('y')
plt.title('Feasible Region for Binary ILP')
plt.grid(True)
plt.show()
