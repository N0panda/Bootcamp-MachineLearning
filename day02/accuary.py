# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    accuary.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/19 13:58:19 by ythomas           #+#    #+#              #
#    Updated: 2020/02/19 17:06:10 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from sklearn.metrics import accuracy_score

def accuracy_score_(y_true, y_pred):
    accuracy = 0.0
    size = len(y_true)
    for i in range(size):
        if y_true[i] == y_pred[i]: accuracy += 1.0
    return (accuracy / size)


# Test n.1
#y_pred = np.array([1, 1, 0, 1, 0, 0, 1, 1])
#y_true = np.array([1, 0, 0, 1, 0, 1, 0, 0])
#print(accuracy_score_(y_true, y_pred))
#print(accuracy_score(y_true, y_pred))
# Test n.2
#y_pred = np.array(['norminet', 'dog', 'norminet', 'norminet', 'dog', 'dog',
#'dog', 'dog'])
#y_true = np.array(['dog', 'dog', 'norminet', 'norminet', 'dog', 'norminet',
#'dog', 'norminet'])
#print(accuracy_score_(y_true, y_pred))
#print(accuracy_score(y_true, y_pred))
