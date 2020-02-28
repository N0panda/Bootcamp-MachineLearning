# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mylinearregression.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/07 16:36:31 by ythomas           #+#    #+#              #
#    Updated: 2020/02/12 14:53:03 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
import sys
from dot import dot

class MyLR():
    def __init__(self, theta):
        if (isinstance(theta, np.ndarray)):
            self.theta = theta
        else:
            self.theta = np.array(theta)
        return

    def predict_(self, X):
        M = len(X)
        N = len(X[0])
        hypothesis = np.zeros((M, 1))
        for i in range(M):
            hypothesis[i] = self.theta[0]
            for j in range(N):
                hypothesis[i] += self.theta[j + 1] * X[i][j]
        return hypothesis

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


    def cost_elem_(self, X, Y):
        M = len(X)
        N = len(X[0])
        cost = np.zeros((M, 1))
        hypothesis = self.predict_(X)
        for i in range(M):
            cost[i] = ((hypothesis[i] - Y[i]) ** 2) / (2 * M)
        return (cost)

    def cost_(self, X, Y):
        cost = np.sum(self.cost_elem_(X, Y))
        return (cost)

    def fit_(self, X, Y, alpha, n_cycle):
        M = len(X)
        N = len(X[0])
        coef = alpha / M
        new_theta = np.zeros((N + 1, 1))
        for cycle in range(n_cycle):
            err_pred = self.predict_(X) - Y
            new_theta[0] = self.theta[0] - (np.sum(err_pred) * coef)
            for feature in range(N):
                tmp_theta = np.sum(dot(err_pred, X.T[feature])) * coef
                new_theta[feature + 1] = self.theta[feature + 1] - tmp_theta
            self.theta = new_theta

    def normalequation_(self, X, Y):
        tmp = np.ones((len(X), 1))
        X = np.hstack((tmp, X))
        self.theta = np.dot(np.linalg.inv((np.dot(X.T, X))), np.dot(X.T, Y))

#X = np.array([[1., 1., 2., 3.], [5., 8., 13., 21.], [34., 55., 89.,
#144.]])
#Y = np.array([[23.], [48.], [218.]])
#mylr = MyLR([[1.], [1.], [1.], [1.], [1]])
#print(mylr.predict_(X))
#print("=============")
#print(mylr.cost_elem_(X, Y))
#print("=============")
#print(mylr.cost_(X,Y))
#print("=============")
#mylr.fit_(X, Y, alpha = 1.6e-04, n_cycle=200000)
#print("=============")
#print(mylr.predict_(X))
#print("=============")
#print(mylr.cost_elem_(X,Y))
#print("=============")
#print(mylr.cost_(X,Y))
