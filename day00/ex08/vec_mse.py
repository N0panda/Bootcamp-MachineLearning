# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vec_mse.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/31 15:32:43 by ythomas           #+#    #+#              #
#    Updated: 2020/01/31 15:49:46 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import numpy as np
from dot import dot

def vec_mse(y, y_hat):
    return dot(y_hat - y, y_hat - y) / len(y)

X = np.array([0, 15, -9, 7, 12, 3, -21])
Y = np.array([2, 14, -13, 5, 12, 4, -19])
print(vec_mse(X, Y))
print(vec_mse(X, X))
