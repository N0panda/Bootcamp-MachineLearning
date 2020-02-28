# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    log_gradient.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/13 14:30:16 by ythomas           #+#    #+#              #
#    Updated: 2020/02/13 16:24:37 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from sigmoid import sigmoid_
import math

def log_gradient_(x, y_true, y_pred):
    gradient = []
    if any(isinstance(var, list) for var in x) == False:
        x = [x]
    if isinstance(y_true, list) == 0:
        y_tr = []; y_tr.append(y_true)
        y_true = y_tr
        y_pr = []; y_pr.append(y_pred)
        y_pred = y_pr
    for i in range(len(x[0])):
        result = 0.0
        for j in range(len(x)):
            result += (y_pred[j] - y_true[j]) * x[j][i]
        gradient.append(result)
    return (gradient)

# Test n.1
#x = [1, 4.2] # 1 represent the intercept
#y_true = 1
#theta = [0.5, -0.5]
#x_dot_theta = sum([a*b for a, b in zip(x, theta)])
#y_pred = sigmoid_(x_dot_theta)
#print(log_gradient_(x, y_pred, y_true))
# Test n.2
#x = [1, -0.5, 2.3, -1.5, 3.2]
#y_true = 0
#theta = [0.5, -0.5, 1.2, -1.2, 2.3]
#x_dot_theta = sum([a*b for a, b in zip(x, theta)])
#y_pred = sigmoid_(x_dot_theta)
#print(log_gradient_(x, y_true, y_pred))
# Test n.3
#x_new = [[1, 2, 3, 4, 5], [1, 6, 7, 8, 9], [1, 10, 11, 12, 13]]
#first column of x_new are intercept values initialized to 1
#y_true = [1, 0, 1]
#theta = [0.5, -0.5, 1.2, -1.2, 2.3]
#x_new_dot_theta = []
#for i in range(len(x_new)):
#    my_sum = 0
#    for j in range(len(x_new[i])):
#        my_sum += x_new[i][j] * theta[j]
#    x_new_dot_theta.append(my_sum)
#y_pred = sigmoid_(x_new_dot_theta)
#print(log_gradient_(x_new, y_true, y_pred))
