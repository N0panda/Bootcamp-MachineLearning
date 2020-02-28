# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recall.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/20 15:48:26 by ythomas           #+#    #+#              #
#    Updated: 2020/02/20 17:18:27 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from sklearn.metrics import recall_score

def recall_score_(y_true, y_pred, pos_label=1):
    label = pos_label
    size = len(y_true)
    value = 0
    good = 0
    for i in range(size):
        if y_true[i] == label:
            value += 1
            if label == y_pred[i]: good +=1
    return good / value

# Test n.1
y_pred = np.array([1, 1, 0, 1, 0, 0, 1, 1])
y_true = np.array([1, 0, 0, 1, 0, 1, 0, 0])
print(recall_score_(y_true, y_pred))
print(recall_score(y_true, y_pred))
# 0.6666666666666666
# 0.6666666666666666
# Test n.2
y_pred = np.array(['norminet', 'dog', 'norminet', 'norminet', 'dog', 'dog',
'dog', 'dog'])
y_true = np.array(['dog', 'dog', 'norminet', 'norminet', 'dog', 'norminet',
'dog', 'norminet'])
print(recall_score_(y_true, y_pred, pos_label='dog'))
print(recall_score(y_true, y_pred, pos_label='dog'))
# 0.75
# 0.75
# Test n.3
print(recall_score_(y_true, y_pred, pos_label='norminet'))
print(recall_score(y_true, y_pred, pos_label='norminet'))
# 0.5
# 0.5
