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

# setting range and open domain
x = np.linspace(-2 * np.pi, 2 * np.pi)
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
plt.ylim(-1, 1)
plt.xlim(-6, 6)
plt.ylabel('y=cos(x)')
plt.grid(True)

# linear sin graph
plt.subplot(223)
plt.plot(x, y1, '.5', label='sin(x)')
plt.yscale('linear')
plt.legend(shadow='True', loc="upper right")
plt.ylim(-1, 1)
plt.xlim(-6, 6)
plt.ylabel('y=cos(x)')
plt.xlabel('x')
plt.grid(True)


# Format layout for graph readiability, and show plot
plt.subplots_adjust(top=0.92, bottom=0.08, left=.15, right=1.7, hspace=0.25, wspace=0.1)
plt.show()

# x = np.linspace(-1, 1, 5000)
# y = x**2
# plt.xlabel("x axis")
# plt.ylabel("y axis")
# plt.plot(x, y, lw=2.0)
# a = 5
# b = 6
# print(x)
# plt.show()

# Selects the last entry in a 4x4 subplot g

# figure creation and numerical data plot
# fig, ax = plt.subplots()
# ax.plot([5, 7, 9, 11], [25, 49, 81, 121], l)
#
# # graph labels, (linear) scale values for both , and legend
# ax.set_title('Potential Profit Line Graph')
# ax.set_xlabel('Days Until Graduation')
# ax.set_ylabel('Potential $')
# plt.xscale('linear')
# plt.yscale('linear')
# plt.legend(['Potential $ Per Day'])
#
#
# plt.show()
