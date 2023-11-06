import matplotlib.pyplot as plt
import numpy as np

# Mixed ILP constraints: 2x + y <= 10, 0 <= x <= 5, y is integer
x = np.arange(0, 6)
y = np.arange(0, 12)

X, Y = np.meshgrid(x, y)
Z = 2*X + Y

plt.figure(figsize=(8, 6))
plt.contourf(X, Y, Z, levels=[-1, 10], colors=('skyblue', 'white'))
plt.xlabel('x')
plt.ylabel('y')
plt.title('Feasible Region for Mixed ILP')
plt.grid(True)
plt.show()
