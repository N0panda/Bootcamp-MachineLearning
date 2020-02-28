# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    sigmoid.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/12 17:26:06 by ythomas           #+#    #+#              #
#    Updated: 2020/02/13 17:43:02 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import math
import numpy as np

def sigmoid_(x):
    if isinstance(x, list):
        result = []
        for i in range(len(x)):
            result.append(1 / (1 + math.exp(-x[i])))
    elif isinstance(x, np.ndarray):
        result = []
        for i in range(len(x)):
            result.append(1 / (1 + math.exp(-x[i])))
    else :
        result = 1 / (1 + math.exp(-x))
    return result

#x = -4
#print(sigmoid_(x))
#x= 2
#print(sigmoid_(x))
#x = [-4, 2, 0]
#print(sigmoid_(x))
