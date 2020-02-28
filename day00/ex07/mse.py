# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mse.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/31 14:51:03 by ythomas           #+#    #+#              #
#    Updated: 2020/01/31 15:31:30 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import numpy as np
from mean import mean

def mse(y, y_hat):
    return mean((y_hat - y)**2)


X = np.array([0, 15, -9, 7, 12, 3, -21])
Y = np.array([2, 14, -13, 5, 12, 4, -19])
print(mse(X, Y))
print(mse(X, X))
