# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    veg_log_loss.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/13 17:05:33 by ythomas           #+#    #+#              #
#    Updated: 2020/02/15 12:58:19 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import math
from sigmoid import sigmoid_
import numpy as np

def vec_log_loss_(y_true, y_pred, m, eps=1e-15):
    if m == 1:
        y_true = np.array([y_true])
        y_pred = np.array([y_pred])
    else :
        y_true = np.asarray(y_true)
        y_pred = np.asarray(y_pred)
    cost = 0.0;
    for i in range(m):
        cost += np.dot(y_true[i], math.log(y_pred[i]) + eps) + np.dot((1 - y_true[i]), (math.log(1 - y_pred[i]) + eps))
    return ((cost * -1) / m)

#
# Test n.1
#x= 4
#y_true = 1
#theta = 0.5
#y_pred = sigmoid_(x * theta)
#m = 1
#length of y_true is 1
#print(vec_log_loss_(y_true, y_pred, m))
# Test n.2
#x = np.array([1, 2, 3, 4])
#y_true = 0
#theta = np.array([-1.5, 2.3, 1.4, 0.7])
#y_pred = sigmoid_(np.dot(x, theta))
#m= 1
#print(vec_log_loss_(y_true, y_pred, m))
# Test n.3
#x_new = np.arange(1, 13).reshape((3, 4))
#y_true = np.array([1, 0, 1])
#theta = np.array([[-1.5], [2.3], [1.4], [0.7]])
#y_pred = sigmoid_(np.dot(x_new, theta))
#m = len(y_true)
#print(vec_log_loss_(y_true, y_pred, m))
# 7.233346147374828
