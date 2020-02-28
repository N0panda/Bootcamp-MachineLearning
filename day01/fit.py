# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    fit.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/06 15:53:40 by ythomas           #+#    #+#              #
#    Updated: 2020/02/09 17:53:07 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
import sys
from pred import predict_
from cost_function import cost_
from cost_function import cost_elem_
from dot import dot

def fit_(theta, X, Y, alpha, n_cycle):
    M = len(X)
    N = len(X[0])
    new_theta = np.zeros((N + 1, 1))
    coef = alpha / M
    for cycle in range(n_cycle):
        err_pred = predict_(theta, X) - Y
        new_theta[0] = theta[0] - (sum(err_pred) * coef)
        for feat in range(N):
            tmp_theta =  np.sum(dot(err_pred, X.T[feat])) * coef
            new_theta[feat + 1] = theta[feat + 1] - tmp_theta
        theta = new_theta
    return new_theta

#X1 = np.array([[0.], [1.], [2.], [3.], [4.]])
#Y1 = np.array([[2.], [6.], [10.], [14.], [18.]])
#theta1 = np.array([[1.], [1.]])
#print("cost before = " + str(cost_(theta1, X1, Y1)))
#theta1 = fit_(theta1, X1, Y1, 0.01, 1000)
#print(theta1)
#print("")
#print(predict_(theta1, X1))
#print("cost after = " + str(cost_(theta1, X1, Y1)))
#print("=========================================================")
#X2 = np.array([[0.2, 2., 20.], [0.4, 4., 40.], [0.6, 6., 60.], [0.8, 8.,
#80.]])
#Y2 = np.array([[19.6], [-2.8], [-25.2], [-47.6]])
#theta2 = np.array([[42.], [1.], [1.], [1.]])
#print("cost before = " + str(cost_(theta2, X2, Y2)))
#theta2 = fit_(theta2, X2, Y2, 0.0005, 42000)
#print(theta2)
#print("")
#print(predict_(theta2, X2))
#print("cost after = " + str(cost_(theta2, X2, Y2)))
