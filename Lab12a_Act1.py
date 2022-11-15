# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names: Jaime Reyes, Nick Foley, Alejandro Zertuche, Matthew McCabe
# Section: 538 102
# Assignment: Lab 12a, Act1
# Date: 11/14/22
# As a team, we have gone through all required sections of the
# tutorial, and each team member understands the material

"""--------------------------------------Activity 1 (and 0)--------------------------------------"""
import numpy as np

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
