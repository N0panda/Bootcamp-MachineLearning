# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mean.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/30 13:59:43 by ythomas           #+#    #+#              #
#    Updated: 2020/01/30 15:38:20 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
import sys

def mean(x):
    result = 0.0
    i = 0.0
    if x.size == 0: print("error"); sys.exit();
    for value in x:
        result += value
        i+=1
    return (result / i)
