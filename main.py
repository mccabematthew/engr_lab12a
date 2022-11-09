# As a team, we have gone through all required sections of the
# tutorial, and each team member understands the material
import numpy as np
#import matplotlib as mpl
import matplotlib.pyplot as plt

# numpy matrices and operations to combine and transpose
A = np.arange(12).reshape(3, 4)
B = np.arange(8).reshape(4, 2)
C = np.arange(6).reshape(2, 3)
F = np.arange(3).reshape(3, 1)
D = A@B@C
# numpy operation to take half of sqrt and apply to linear system equation
E = np.sqrt(D) / 2
X = F / E
# print(np.linalg.solve(A, B))

print(A, '\n')
print(B, '\n')
print(C, '\n')
print(F, '\n')
print(np.transpose(D), '\n')
print(X)

fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])

ax.set_title('Degradation of Man')
ax.set_ylabel('Women')
ax.set_ylabel('Money')
