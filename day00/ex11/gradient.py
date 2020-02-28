# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    gradient.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/31 17:00:26 by ythomas           #+#    #+#              #
#    Updated: 2020/01/31 17:27:59 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
import sys
from dot import dot

def gradient(x, y, theta):
    result = np.zeros((len(x[0]), 1))
    for i in range(len(x[0])):
        result[i] += dot((dot(theta, x[i]) - y[i]), x[i])
    

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
gradient(X, Y, Z)
W = np.array([0,0,0])
gradient(X, Y, W)
gradient(X, X.dot(Z), Z)
