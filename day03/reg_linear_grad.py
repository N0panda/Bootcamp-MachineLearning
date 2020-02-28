# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    reg_linear_grad.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/24 15:37:39 by ythomas           #+#    #+#              #
#    Updated: 2020/02/24 16:16:16 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

def predict_(X, theta):
    return np.dot(X, theta)


def reg_linear_grad(X, y, theta, lambda_):
    m = X.shape[0]
    n = X.shape[1]
    y = y.reshape((y.shape[0], 1))
    theta = theta.reshape((theta.shape[0], 1))
    y_pred = predict_(X, theta)
    result = np.zeros((n, 1))
    for i in range(m):
        for j in range(n):
            result[j] += ((y_pred[i] - y[i]) * X[i][j]) + (lambda_ * theta[j]/m)
    return result / m


X = np.array([
         [ -6, -7, -9],
        [ 13, -2, 14],
        [ -7, 14, -1],
        [ -8, -4, 6],
        [ -5, -9, 6],
        [ 1, -5, 11],
        [ 9, -11, 8]])
Y = np.array([2, 14, -13, 5, 12, 4, -19])
Z = np.array([3,10.5,-6])
print(reg_linear_grad(X, Y, Z, 1))
print(reg_linear_grad(X, Y, Z, 0.5))
print(reg_linear_grad(X, Y, Z, 0.0))
