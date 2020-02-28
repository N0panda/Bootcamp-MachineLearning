# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mylinearregression.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/07 16:36:31 by ythomas           #+#    #+#              #
#    Updated: 2020/02/25 18:21:22 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
import sys
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.linear_model import Ridge

class MR():
    def __init__(self, theta):
        if (isinstance(theta, np.ndarray)):
            self.theta = theta
        else:
            self.theta = np.array(theta)
        return

    def predict_(self, X):
        return np.dot(X, self.theta)

    def mse_elem_(self, X, Y):
        M = len(X)
        N = len(X[0])
        cost = np.zeros((M, 1))
        hypothesis = self.predict_(X)
        for i in range(M):
            cost[i] = ((hypothesis[i] - Y[i]) ** 2) / M
        return (cost)

    def mse_(self, X, Y):
        cost = np.sum(self.mse_elem_(X, Y))
        return (cost)

    def rmse_(self, X, Y):
        cost = self.mse_(X, Y)
        return (np.sqrt(cost))

    def r2score_(self, X, Y):
        M = len(X)
        N = len(X[0])
        predicted_value = np.sum(self.predict_(X) - Y) ** 2
        mean_value = np.sum(np.mean(Y) - Y) ** 2
        cost = 1 - predicted_value / mean_value
        return (cost)


    def cost_(self, X, y, lambda_):
        m = X.shape[0]
        y_pred = self.predict_(X)
        cost = np.sum(np.square(y_pred - y) / (2 * m))
        tmp_theta = self.theta
        tmp_theta[0] = 0
        reg = (lambda_ / (2 * m)) * np.sum(np.square(tmp_theta))
        return (cost + reg)

    def fit_(self, X, y, max_iter, alpha, lambda_ = 1.0):
        m = X.shape[0]
        coef = alpha / m
        new_theta = np.zeros((self.theta.shape[0], 1))
        x_zero = X.T[0]
        n = self.theta.shape[0]
        x_rest = X.T[1:n]
        self.cost = np.zeros((max_iter))
        for cycle in range(max_iter):
            y_pred = self.predict_(X)
            new_theta[0] = self.theta[0] - (coef * (np.dot(x_zero, (y_pred - y))))
            reg = (1 - ((alpha * lambda_) / m)) * self.theta[1:n]
            new_theta[1:n] = reg - (coef * (np.dot(x_rest, (y_pred - y))))
            self.theta = new_theta
            self.cost[cycle] = self.cost_(X, y, 1)
        return self.theta

    def normalequation_(self, X, Y):
        tmp = np.ones((len(X), 1))
        X = np.hstack((tmp, X))
        self.theta = np.dot(np.linalg.inv((np.dot(X.T, X))), np.dot(X.T, Y))

data = pd.read_csv("./resources/data.csv")
y = np.array(data[["y"]])
X = np.array(data[["x1", "x2"]])
tmp = np.ones((X.shape[0], 1))
X = np.hstack((tmp, X))
x3 = np.square(X[:, 2]).reshape((y.shape[0], 1))
x4 = np.power(X[:, 1], 3).reshape((y.shape[0], 1))
X = np.hstack((X, x3, x4))
theta = np.ones((X.shape[1], 1))

ridge = MR(theta)
pred = ridge.predict_(X)
ridge.fit_(X, y, 150, 0.0005, 0.5)
print(ridge.cost_(X, y, 0.5))
pred2 = ridge.predict_(X)
#test = Ridge(alpha=0.0001)
#test.fit(X,y)
#print(test.score(X,y))
#pred2 = test.predict(X)
fig = plt.figure()
ax = plt.axes(projection='3d')
t = y.reshape((2000,))
ax.scatter(X[:,1], X[:,2], pred2, c=t, cmap="viridis");
ax.set_xlabel('X1')
ax.set_ylabel('X2')
ax.set_zlabel('Y')
test=np.array([[1, 4, 1, 1**2, 4**3]])
print(ridge.predict_(test)) # test pour une valeur de x1=4 et x2=4
#plt.plot(ridge.cost)
plt.show()

