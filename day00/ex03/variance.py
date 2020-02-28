# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    variance.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/30 14:52:59 by ythomas           #+#    #+#              #
#    Updated: 2020/01/30 16:08:44 by ythomas          ###   ########.fr        #
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
