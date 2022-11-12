# As a team, we have gone through all required sections of the
# tutorial, and each team member understands the material

"""--------------------------------------Activity 1--------------------------------------"""
import numpy as np
# import matplotlib as mpl
import matplotlib.pyplot as plt

# numpy matrices for use in combination, transposition, and multiplication calc of the 3
A = np.arange(12).reshape(3, 4)
B = np.arange(8).reshape(4, 2)
C = np.arange(6).reshape(2, 3)
F = np.arange(3).reshape(3, 1)
D = A@B@C

# numpy mathematical and linear algebraic functions for linear system solution
E = np.divide(np.sqrt(D), 2)
X = np.linalg.solve(E, F)

# inline formatted print statements
print('A = ', A, '\n')
print('B = ', B, '\n')
print('C = ', C, '\n')
print('D = ', D, '\n')
print('D^T = ', np.transpose(D), '\n')
print('E = ', E, '\n')
print('X = ', X, '\n')

"""--------------------------------------Activity 2--------------------------------------"""
# As a team, we have gone through all required sections of the
# tutorial, and each team member understands the material
''''''
'''
||Part 1||
'''

x = np.linspace(-2.0, 2.0, 100)   # 100 numbers from -2 to 2 - x = np.linspace(-2.0, 2.0, 100)
f1, f2 = 2.0, 6.0
plt.plot(x, (1/(4*f1))*x**2, 'b', linewidth=2)
plt.plot(x, (1/(4*f2))*x**2, 'r', linewidth=6)
plt.ylabel('y')
plt.xlabel('x')
plt.show()

'''
||Part 2||
'''

x1 = np.linspace(-4.0, 4.0, 25)
y = 2 * x1**3 + 3*x1**2 - 11*x1 - 6
plt.plot(x1, y, 'y*')
plt.ylabel('y values')
plt.xlabel('x values')
plt.show()

'''
||Part 3||
'''

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


# setting range and open domain
x = np.arange(0, 3 * np.pi, .1)
y1 = np.sin(x)
y2 = np.cos(x)

# plot with various axes scales
plt.figure()

# linear cos graph
plt.subplot(221)
plt.plot(x, y2, 'r', label='cos(x)')
plt.yscale('linear')
plt.legend(shadow='True', loc="lower right")
plt.title('Plot of cos(x) and sin(x)')
plt.ylabel('y=cos(x)')
plt.grid(True)

# linear sin graph
plt.subplot(223)
plt.plot(x, y1, label='sin(x)')
plt.yscale('linear')
plt.legend(shadow='True', loc="upper right")
plt.ylabel('y=cos(x)')
plt.grid(True)


# Format layout for graph readiability, and show plot
plt.subplots_adjust(top=0.92, bottom=0.08, left=.15, right=1.7, hspace=0.25, wspace=0.1)
plt.show()
