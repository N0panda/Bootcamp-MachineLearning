# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    sum.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/29 18:30:14 by ythomas           #+#    #+#              #
#    Updated: 2020/01/30 13:57:13 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

def sum_(x, f):
    result = 0.0
    for value in x:
        result = result + f(value)
    return result

array = np.array([0, 15, -9, 7, 12, 3, -21])
print(sum_(array, lambda x: x))
print(sum_(array, lambda x: x**2))
