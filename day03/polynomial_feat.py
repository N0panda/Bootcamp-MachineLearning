# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    polynomial_feat.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/26 15:14:27 by ythomas           #+#    #+#              #
#    Updated: 2020/02/26 15:26:09 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

def polynomialFeatures(x, degree=2, interaction_only= False, include_bias=True):
    None

X = np.array([[0, 1], [2, 3], [4, 5]])
polynomialFeatures(X)
polynomialFeatures(X, 3)
polynomialFeatures(X, 3, interaction_only=True, include_bias=False)
