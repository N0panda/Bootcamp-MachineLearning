# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    f1_score.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/20 17:43:46 by ythomas           #+#    #+#              #
#    Updated: 2020/02/20 18:08:06 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from sklearn.metrics import f1_score

def f1_score_(y_true, y_pred, pos_label=1):
    size = len(y_true)
    label = pos_label
    preci_match = 0
    preci_total = 0
    recall_total = 0
    recall_match = 0
    for i in range(size):
        if y_pred[i] == label:
            preci_total += 1
            if y_true[i] == label: preci_match += 1
        if y_true[i] == label:
            recall_total +=1
            if y_pred[i] == label: recall_match += 1
    precision = preci_match / preci_total
    recall = recall_match / recall_total
    f_score = 2 * (precision * recall) / (precision + recall)
    return f_score

# Test n.1
y_pred = np.array([1, 1, 0, 1, 0, 0, 1, 1])
y_true = np.array([1, 0, 0, 1, 0, 1, 0, 0])
print(f1_score_(y_true, y_pred))
print(f1_score(y_true, y_pred))
# 0.5 # 0.5
# Test n.2
y_pred = np.array(['norminet', 'dog', 'norminet', 'norminet', 'dog', 'dog',
'dog', 'dog'])
y_true = np.array(['dog', 'dog', 'norminet', 'norminet', 'dog', 'norminet',
'dog', 'norminet'])
print(f1_score_(y_true, y_pred, pos_label='dog'))
print(f1_score(y_true, y_pred, pos_label='dog'))
# 0.6666666666666665
# 0.6666666666666665
# Test n.3
print(f1_score_(y_true, y_pred, pos_label='norminet'))
print(f1_score(y_true, y_pred, pos_label='norminet'))
# 0.5714285714285715
# 0.5714285714285715
