import numpy as np
from matplotlib import pyplot as plt

# Exercise 1.1:  Simple separable data set
X = np.array([[2, 3, 9, 12],
              [5, 2, 6, 5]])
Y = np.array([[1, 0, 1, 0]])

X_pos1 = np.array([[2, 9],
                  [5, 6]])

X_neg1 = np.array([[3, 12],
                  [2, 5]])

figure1 = plt.figure(1)
plt.scatter(X_pos1[0], X_pos1[1], marker='+', c='green', s=200, linewidths=2)
plt.scatter(X_neg1[0], X_neg1[1], marker='x', c='red', s=100, linewidths=2)

plt.xlabel('x1 feature')
plt.ylabel('x2 feature')
plt.grid()
plt.show()

# Exercise 1.2: NOT-XOR
# 1.2A)
X = np.array([[0, 1, 0, 1],
              [0, 1, 1, 0]])
Y = np.array([[1, 1, 0, 0]])

X_pos2 = np.array([[0, 1],
                  [0, 1]])

X_neg2 = np.array([[0, 1],
                  [1, 0]])

figure2 = plt.figure(2)
plt.scatter(X_pos2[0], X_pos2[1], marker='+', c='green', s=200, linewidths=2)
plt.scatter(X_neg2[0], X_neg2[1], marker='x', c='red', s=100, linewidths=2)
plt.xlabel('x1 feature')
plt.ylabel('x2 feature')
plt.grid()
plt.show()


