# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    linear_mse.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/31 15:50:33 by ythomas           #+#    #+#              #
#    Updated: 2020/01/31 17:09:05 by ythomas          ###   ########.fr        #
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
