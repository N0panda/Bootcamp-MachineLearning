# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    reg_mse.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/24 12:56:48 by ythomas           #+#    #+#              #
#    Updated: 2020/02/24 15:37:00 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from sygmoid_ import pred_
from vec_reg import vec_reg

def predict_(X, theta):
    pred = np.dot(X, theta.reshape((theta.shape[0], 1)))
    return pred

def reg_mse(X, y, theta, lambda_):  
    y_pred = predict_(X, theta)
    y = y.reshape((y.shape[0], 1))
    err = np.dot((y_pred - y).T, (y_pred - y)) + vec_reg(theta, lambda_)
    return float(err / X.shape[0])

X = np.array([
         [ -6, -7, -9],
        [ 13, -2, 14],
        [ -7, 14, -1],
        [ -8, -4, 6],
        [ -5, -9, 6],
        [ 1, -5, 11],
        [ 9, -11, 8]])
Y = np.array([2, 14, -13, 5, 12, 4, -19])
Z = np.array([3,0.5,-6])
print(reg_mse(X, Y, Z, 0))
print(reg_mse(X, Y, Z, 0.1))
print(reg_mse(X, Y, Z, 0.5))
