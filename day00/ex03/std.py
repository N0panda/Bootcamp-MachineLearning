# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    std.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/30 15:56:22 by ythomas           #+#    #+#              #
#    Updated: 2020/01/30 16:14:03 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from  variance import variance
import sys
from math import sqrt

def std(x):
    return sqrt(variance(x))

X = np.array([0, 15, -9, 7, 12, 3, -21])
print(std(X))
print(np.std(X))
print ("=================================")
Y = np.array([2, 14, -13, 5, 12, 4, -19])
print(std(Y))
print(np.std(Y))
