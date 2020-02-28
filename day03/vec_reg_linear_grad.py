# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vec_reg_linear_grad.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/24 16:16:48 by ythomas           #+#    #+#              #
#    Updated: 2020/02/26 17:19:34 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from timeflux.core.node import Node


def predict_(X, theta):
    return np.dot(X, theta)

def vec_reg_linear_grad(X, y, theta, lambda_):
    y = y.reshape((y.shape[0], 1))
    m = X.shape[0]
    theta = theta.reshape((theta.shape[0], 1))
    y_pred = predict_(X, theta)
    result = np.zeros((theta.shape[0], 1))
    result = (np.dot(X.T, (y_pred - y)) / m) + sum(lambda_ * theta) / m
    result[0] = np.dot(X.T[0], (y_pred - y)) / m
    print(result)

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
vec_reg_linear_grad(X, Y, Z, 1)
vec_reg_linear_grad(X, Y, Z, 0.5)
vec_reg_linear_grad(X, Y, Z, 0.0)
