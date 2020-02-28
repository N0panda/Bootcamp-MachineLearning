# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    z-score.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/26 12:54:22 by ythomas           #+#    #+#              #
#    Updated: 2020/02/26 13:25:32 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

def zscore(x):
    m = len(x)
    x_mean = x - (np.sum(x) / m)
    st_dev = np.sqrt((1 / m) * np.sum(np.square(x_mean)))
    return x_mean / st_dev

#X = np.array([0, 15, -9, 7, 12, 3, -21])
#print(zscore(X))
#Y = np.array([2, 14, -13, 5, 12, 4, -19])
#print(zscore(Y))
