# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    pred.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/03 16:01:25 by ythomas           #+#    #+#              #
#    Updated: 2020/02/09 17:42:44 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
import sys

# X = (M, N) 5-1
# theta = (N + 1, 1) 2-1

# result = (M, 1) 5-1

def predict_(theta, x):
    m = len(x)
    n = len(x[0])
    result = np.zeros((m, 1))
    for i in range(m):
        result[i] = theta[0]
        for j in range(n):
            result[i] += theta[j + 1] * x[i][j]
    return result

#X1 = np.array([[0.], [1.], [2.], [3.], [4.]])
#theta1 = np.array([[2.], [4.]])
#print(predict_(theta1, X1))
##print("===========================")
#X2 = np.array([[1], [2], [3], [5], [8]])
#theta2 = np.array([[2.]])
#print(predict_(theta2, X2))
##print("===========================")
#X3 = np.array([[0.2, 2., 20.], [0.4, 4., 40.], [0.6, 6., 60.], [0.8, 8.,
#80.]])
#theta3 = np.array([[0.05], [1.], [1.], [1.]])
#print(predict_(theta3, X3))
