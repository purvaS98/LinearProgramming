import matplotlib.pyplot as plt
import numpy as np

# Pure ILP constraints: 2x + 3y <= 10, x, y are integers
x = np.arange(0, 6)
y = np.arange(0, 4)

X, Y = np.meshgrid(x, y)
Z = 2*X + 3*Y

plt.figure(figsize=(8, 6))
plt.contourf(X, Y, Z, levels=[-1, 10], colors=('skyblue', 'white'))
plt.xlabel('x')
plt.ylabel('y')
plt.title('Feasible Region for Pure ILP')
plt.grid(True)
plt.show()
