# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vec_reg.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/24 12:52:37 by ythomas           #+#    #+#              #
#    Updated: 2020/02/24 14:57:08 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

def vec_reg(theta, lambda_):
    reg = lambda_ * np.dot(theta.T, theta)
    return reg


#X = np.array([0, 15, -9, 7, 12, 3, -21])
#print(vectorized_regularization(X, 0.3))
#print(vectorized_regularization(X, 0.01))
#print(vectorized_regularization(X, 0))
