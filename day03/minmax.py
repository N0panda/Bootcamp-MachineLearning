# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    minmax.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/26 13:28:23 by ythomas           #+#    #+#              #
#    Updated: 2020/02/26 13:38:37 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

def minmax(x):
    top = x - np.min(x)
    bot = np.max(x) - np.min(x)
    return (top / bot)

#X = np.array([0, 15, -9, 7, 12, 3, -21])
#print(minmax(X))
#Y = np.array([2, 14, -13, 5, 12, 4, -19])
#print(minmax(Y))
