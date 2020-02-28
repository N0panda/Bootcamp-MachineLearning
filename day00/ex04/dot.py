# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    dot.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/30 16:14:45 by ythomas           #+#    #+#              #
#    Updated: 2020/01/30 16:49:04 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import numpy as np

def dot(x, y):
    result = 0.0
    for i in range(x.size): result += x[i] * y[i]
    return result

X = np.array([0, 15, -9, 7, 12, 3, -21])
Y = np.array([2, 14, -13, 5, 12, 4, -19])
print(dot(X, Y))
print(np.dot(X, Y))
print ("=============================")
print(dot(X, X))
print(np.dot(X, X))
print ("=============================")
print(dot(Y, Y))
print(np.dot(Y, Y))
