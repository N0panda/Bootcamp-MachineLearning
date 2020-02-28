# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    confusion_matrix.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/20 18:11:32 by ythomas           #+#    #+#              #
#    Updated: 2020/02/21 12:36:38 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from sklearn.metrics import confusion_matrix
import sklearn.metrics as met
from precision import precision_score_


def confusion_matrix_(y_true, y_pred, labels=None):
    a = np.unique(y_true)
    b = np.unique(y_pred)
    if len(a) > len(b): size = len(a)
    else: size = len(b)
    c_matrix = np.zeros((size, size))
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                c_matrix[i][j] = precision_score_(y_true, y_pred, a[i])
    return c_matrix


y_pred = np.array(['norminet', 'dog', 'norminet', 'norminet', 'dog',
'bird'])
y_true = np.array(['dog', 'dog', 'norminet', 'norminet', 'dog', 'norminet'])
print(confusion_matrix_(y_true, y_pred))
print(confusion_matrix(y_true, y_pred))
# [[0 0 0]
# [0 2 1]
# [1 0 2]]

# [[0 0 0]
# [0 2 1]
# [1 0 2]]
print(confusion_matrix_(y_true, y_pred, labels=['dog', 'norminet']))
print(confusion_matrix(y_true, y_pred, labels=['dog', 'norminet']))
# [[2 1]
# [0 2]]

# [[2 1]
# [0 2]]
