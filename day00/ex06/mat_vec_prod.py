# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mat_vec_prod.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/30 16:50:45 by ythomas           #+#    #+#              #
#    Updated: 2020/01/31 13:46:05 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import numpy as np
from dot import dot

def mat_vec_prod(x, y):
    size = x.shape[0]
    result = np.zeros((size, 1))
    for i in range(size):
        result[i] = dot(x[i], y)
    return result
