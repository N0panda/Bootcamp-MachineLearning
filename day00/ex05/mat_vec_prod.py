# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mat_vec_prod.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/30 16:50:45 by ythomas           #+#    #+#              #
#    Updated: 2020/01/30 18:52:48 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import numpy as np
from dot import dot

def mat_vec_prod(x, y):
    size = x.shape[0]
    result = np.zeros((size, 1))
    for i in range(size):
        result[i] = dot(x[i], y)
    return result

W = np.array([
    [ -8, 8, -6, 14, 14, -9, -4],
    [ 2, -11, -2, -11, 14, -2, 14],
    [-13, -2, -5, 3, -8, -4, 13],
    [ 2, 13, -14, -15, -14, -15, 13],
    [ 2, -1, 12, 3, -7, -3, -6]])
X = np.array([0, 15, -9, 7, 12, 3, -21]).reshape((7,1))
Y = np.array([2, 14, -13, 5, 12, 4, -19]).reshape((7,1))
print(mat_vec_prod(W, X))
print(W.dot(X))
print("==============================")
print(mat_vec_prod(W, Y))
print(W.dot(Y))
