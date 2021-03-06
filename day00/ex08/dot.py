# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    dot.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/30 16:14:45 by ythomas           #+#    #+#              #
#    Updated: 2020/01/31 15:47:25 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import numpy as np

def dot(x, y):
    result = 0.0
    for i in range(x.size): result += x[i] * y[i]
    return result
