# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    reg.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/24 12:42:45 by ythomas           #+#    #+#              #
#    Updated: 2020/02/24 12:51:56 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

def regularization(theta, lambda_):
    theta = np.asarray(theta)
    reg = lambda_ * sum(np.square(theta))
    return reg

X = np.array([0, 15, -9, 7, 12, 3, -21])
print(regularization(X, 0.3))
print(regularization(X, 0.01))
print(regularization(X, 0))
