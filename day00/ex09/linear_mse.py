# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    linear_mse.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/31 15:50:33 by ythomas           #+#    #+#              #
#    Updated: 2020/01/31 16:32:52 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import numpy as np
from dot import dot
from mean import mean

def linear_mse(x, y, theta):
    result = 0.0
    for i in range(len(x)):
        result += (dot(theta, x[i]) - y[i])**2
    return (result / len(x))


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
print(linear_mse(X, Y, Z))
W = np.array([0,0,0])
print(linear_mse(X, Y, W))
