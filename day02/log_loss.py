# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    log_loss.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/13 11:53:08 by ythomas           #+#    #+#              #
#    Updated: 2020/02/13 14:27:12 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import math
from sigmoid import sigmoid_

def log_loss_(y_true, y_pred, m, eps=1e-15):
    result = 0.0
    if isinstance(y_true, list) == 0: 
        y_tr = []; y_tr.append(y_true)
        y_pr = []; y_pr.append(y_pred)
    else :
        y_tr = y_true
        y_pr = y_pred
    for i in range(m):
        result += (y_tr[i] * math.log(y_pr[i] + eps) + (1 - y_tr[i]) * math.log(1 - y_pr[i] + eps))
    return (-1 * result / m)

# Test n.1
#x= 4
#y_true = 1
#theta = 0.5
#y_pred = sigmoid_(x * theta)
#m = 1
#print(log_loss_(y_true, y_pred, m))

## Test n.2
#x = [1, 2, 3, 4]
#y_true = 0
#theta = [-1.5, 2.3, 1.4, 0.7]
#x_dot_theta = sum([a*b for a, b in zip(x, theta)])
#y_pred = sigmoid_(x_dot_theta)
#m= 1
#print(log_loss_(y_true, y_pred, m))
#  Test n.3
#x_new = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
#y_true = [1, 0, 1]
#theta = [-1.5, 2.3, 1.4, 0.7]
#x_dot_theta = []
#for i in range(len(x_new)):
#    my_sum = 0
#    for j in range(len(x_new[i])):
#        my_sum += x_new[i][j] * theta[j]
#    x_dot_theta.append(my_sum)
#y_pred = sigmoid_(x_dot_theta)
#m = len(y_true)
#print(log_loss_(y_true, y_pred, m))
