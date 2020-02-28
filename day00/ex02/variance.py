# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    variance.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/30 14:52:59 by ythomas           #+#    #+#              #
#    Updated: 2020/01/30 15:53:15 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from mean import mean
import sys

def variance(x):
    result = 0.0
    m = 0.0
    if x.size == 0: print("error"); sys.exit()
    for value in x:
            result += (value - mean(x))**2
            m+=1
    return result / m

array = np.array([0, 15, -9, 7, 12, 3, -21])
print(variance(array))
print(np.var(array))
print("==================")
print(variance(array / 2))
print(np.var(array / 2))
