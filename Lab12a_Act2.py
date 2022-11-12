import matplotlib.pyplot as plt
import numpy as np

######### Plot 1 ########
x = np.linspace(-2.0, 2.0, 100)   # 100 numbers from -2 to 2 - x = np.linspace(-2.0, 2.0, 100)
f1, f2 = 2.0, 6.0
plt.plot(x, (1/(4*f1))*x**2, 'b', linewidth=2)
plt.plot(x, (1/(4*f2))*x**2, 'r', linewidth=6)
plt.ylabel('y')
plt.xlabel('x')
plt.show()

# ####### Plot 2 #######
x1 = np.linspace(-4.0, 4.0, 25)
y = 2 * x1**3 + 3*x1**2 - 11*x1 - 6
plt.plot(x1, y, 'y*')
plt.ylabel('y values')
plt.xlabel('x values')
plt.show()

# ####### Plot 3 #######
x2 = np.linspace(-2 * np.pi, 2 * np.pi, 100)

plt.figure()
plt.subplot(2, 1, 1)
plt.plot(x2, np.sin(np.sin(x2)), 'r')
plt.ylabel('y sinsinx')
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(x2, np.cos(np.cos(x2)), 'g')
plt.ylabel(' y coscosx')
plt.grid()
plt.show()
