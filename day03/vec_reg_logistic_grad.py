# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vec_reg_logistic_grad.py                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/24 17:47:48 by ythomas           #+#    #+#              #
#    Updated: 2020/02/24 18:09:17 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np


def sigmoid_(x):
    return(1 / (1 + np.exp(-x)))

def predict_(X, theta):
    return sigmoid_(np.dot(X, theta))

def vec_reg_logistic_grad(X, y, theta, lambda_):
    y = y.reshape((y.shape[0], 1))
    m = X.shape[0]
    theta = theta.reshape((theta.shape[0], 1))
    y_pred = predict_(X, theta)
    result = np.zeros((theta.shape))
    result = (np.dot(X.T, y_pred - y) / m) + (lambda_ / m) * theta
    result[0] = (np.dot(X.T[0], y_pred - y) / m)
    return result

X = np.array([
         [ -6, -7, -9],
        [ 13, -2, 14],
        [ -7, 14, -1],
        [ -8, -4, 6],
        [ -5, -9, 6],
        [ 1, -5, 11],
        [ 9, -11, 8]])
Y = np.array([1,0,1,1,1,0,0])
Z = np.array([1.2,0.5,-0.32])
print(vec_reg_logistic_grad(X, Y, Z, 1))
print(vec_reg_logistic_grad(X, Y, Z, 0.5))
print(vec_reg_logistic_grad(X, Y, Z, 0.0))
