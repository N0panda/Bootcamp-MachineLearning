# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    sygmoid_.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/24 14:21:25 by ythomas           #+#    #+#              #
#    Updated: 2020/02/24 14:52:18 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

def sigmoid_(value):
    return 1 / (1 + np.exp(-value))

def pred_(X, theta):
    theta = theta.reshape((theta.shape[0], 1))
    h = sigmoid_(np.dot(X, theta))
    return h
