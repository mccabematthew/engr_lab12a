# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names: Jaime Reyes, Nick Foley, Alejandro Zertuche, Matthew McCabe
# Section: 538 102
# Assignment: Lab 12a, Act2
# Date: 11/14/22
# As a team, we have gone through all required sections of the
# tutorial, and each team member understands the material
import matplotlib.pyplot as plt
import numpy as np

"""---------------------------------Activity 2 (and 0)---------------------------------"""

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

# setting range and closed domain
x = np.linspace(-2 * np.pi, 2 * np.pi)
y1 = np.sin(x)
y2 = np.cos(x)

# plot with various axes scales
plt.figure()

# linear cos graph on subplot
plt.subplot(221)
plt.plot(x, y2, 'r', label='cos(x)')
plt.legend(shadow='True', loc="lower right")
plt.title('Plot of cos(x) and sin(x)')

# scale for graph, limits, grid lining, and labels
plt.yscale('linear')
plt.ylim(-1, 1)
plt.xlim(-6, 6)
plt.ylabel('y=cos(x)')
plt.grid(True)

# linear sin graph on subplot
plt.subplot(223)
plt.plot(x, y1, '.5', label='sin(x)')
plt.legend(shadow='True', loc="upper right")

# scale for graph, limits, grid lining, and labels
plt.yscale('linear')
plt.ylim(-1, 1)
plt.xlim(-6, 6)
plt.ylabel('y=cos(x)')
plt.xlabel('x')
plt.grid(True)

# Format layout for graph readiability, and show plot
plt.subplots_adjust(top=0.92, bottom=0.08, left=.15, right=1.7, hspace=0.25, wspace=0.1)
plt.show()
