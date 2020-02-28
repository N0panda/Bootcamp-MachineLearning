# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    cost_function.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/05 15:31:36 by ythomas           #+#    #+#              #
#    Updated: 2020/02/10 12:51:31 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
import sys
from pred import predict_

#calculate 0.5*M*(y_pred - y) ** 2
def cost_elem_(theta, X, Y):
    m = len(X)
    n = len(X[0])
    J_elem = np.zeros((m, 1))
    for i in range(m):
        J_elem[i] = ((predict_(theta, X)[i] - Y[i]) ** 2) / (2 * m)
    return J_elem

def cost_(theta, X, Y):
    J_value = np.sum(cost_elem_(theta, X, Y))
    return J_value

#X1 = np.array([[0.], [1.], [2.], [3.], [4.]])
#theta1 = np.array([[2.], [4.]])
#Y1 = np.array([[2.], [7.], [12.], [17.], [22.]])
#print("Cost for each elements " + "\n" + str(cost_elem_(theta1, X1, Y1)))
#print("Cost  = " + str(cost_(theta1, X1, Y1)))
#print("=======================================================")
#X2 = np.array([[0.2, 2., 20.], [0.4, 4., 40.], [0.6, 6., 60.], [0.8, 8.,
#80.]])
#theta2 = np.array([[0.05], [1.], [1.], [1.]])
#Y2 = np.array([[19.], [42.], [67.], [93.]])
#print("Cost for each elements " + "\n" + str(cost_elem_(theta2, X2, Y2)))
#print("Cost  = " + str(cost_(theta2, X2, Y2)))
