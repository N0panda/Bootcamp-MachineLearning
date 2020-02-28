# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mat_mat_prod.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/30 18:53:46 by ythomas           #+#    #+#              #
#    Updated: 2020/01/31 14:50:32 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import numpy as np
from dot import dot

def mat_mat_prod(x, y):
    result = np.zeros((x.shape[0], y.shape[1]))
    for i in range(len(x)):
        for j in range(len(y[0])):
            for k in range(len(y)):
                result[i][j] += x[i][k] * y[k][j]
    return (result)

W = np.array([
    [ -8, 8, -6, 14, 14, -9, -4],
    [ 2, -11, -2, -11, 14, -2, 14],
    [-13, -2, -5, 3, -8, -4, 13],
    [ 2, 13, -14, -15, -14, -15, 13],
    [ 2, -1, 12, 3, -7, -3, -6]])
Z = np.array([
    [ -6, -1, -8, 7, -8],
        [ 7, 4, 0, -10, -10],
        [ 7, -13, 2, 2, -11],
        [ 3, 14, 7, 7, -4],
        [ -1, -3, -8, -4, -14],
        [ 9, -14, 9, 12, -7],
        [ -9, -4, -10, -3, 6]])
print(mat_mat_prod(W, Z))
print(W.dot(Z))
print(mat_mat_prod(Z,W))
print(Z.dot(W))
