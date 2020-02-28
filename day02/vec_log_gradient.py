# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vec_log_gradient.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/15 12:59:38 by ythomas           #+#    #+#              #
#    Updated: 2020/02/15 14:16:03 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from sigmoid import sigmoid_

def vec_log_gradient_(x, y_true, y_pred):
    n = x.shape[0]
    new_theta = []
    if isinstance(y_pred, float) or isinstance(y_pred, int):
        m = 1;
        y_pred = np.array([y_pred])
        y_true = np.array([y_true])
    else : m = len(y_pred)
    tmp_x = x.T
    for i in range(n):
        value = np.dot((y_pred - y_true), tmp_x[i])
        new_theta.append(value)
    return np.asarray(new_theta)

# Test n.1
#x = np.array([1, 4.2]) # x[0] represent the intercept
#y_true = 1
#theta = np.array([0.5, -0.5])
#y_pred = sigmoid_(np.dot(x, theta))
#print(vec_log_gradient_(x, y_pred, y_true))
# [0.83201839 3.49447722]
# Test n.2
#x = np.array([1, -0.5, 2.3, -1.5, 3.2]) # x[0] represent the intercept
#y_true = 0
#theta = np.array([0.5, -0.5, 1.2, -1.2, 2.3])
#y_pred = sigmoid_(np.dot(x, theta))
#print(vec_log_gradient_(x, y_true, y_pred))
# Test n.3
#x_new = np.arange(2, 14).reshape((3, 4))
#x_new = np.insert(x_new, 0, 1, axis=1)
# first column of x_new are now intercept values initialized to 1
#y_true = np.array([1, 0, 1])
#theta = np.array([0.5, -0.5, 1.2, -1.2, 2.3])
#y_pred = sigmoid_(np.dot(x_new, theta))
#print(vec_log_gradient_(x_new, y_true, y_pred))
