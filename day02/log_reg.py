# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    log_reg.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/15 14:19:38 by ythomas           #+#    #+#              #
#    Updated: 2020/02/19 18:02:29 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt

class LLR:
    def __init__(self, alpha, max_iter, verbose=False, learning_rate='constant'):
        self.alpha = alpha
        self.max_iter = max_iter
        self.verbose = verbose
        self.learning_rate = learning_rate # can be 'constant' or 'invscaling'
        self.thetas = []

    def fit(self, x_train, y_train):
        m = x_train.shape[0]
        n = x_train.shape[1]
        tmp_x = x_train.T
        y_train = np.asarray(y_train)
        y_train = y_train.reshape((m, 1))
        self.theta = np.ones((n, 1))
        for cycle in range(self.max_iter):
            y_pred = self.predict_(x_train)
            tmp_theta = np.zeros((n, 1))
            for i in range(n):
                tmp_theta[i] = self.theta[i] - (sum(np.dot(tmp_x[i].reshape((1, m)), (y_pred - y_train))) * self.alpha)
            self.theta = tmp_theta
            if cycle % 50 == 0: self.score(x_train, y_train)
        self.score(x_train, y_train)

    def predict_(self, x_train):
        m = x_train.shape[0]
        n = x_train.shape[1]
        result = np.zeros((m, 1))
        value = np.dot(x_train, self.theta)
        for i in range(m):
            result[i] = (1 / (1 + math.exp(-1 * value[i])))
        return result

    def score(self, x_train, y_train):
        eps = 1e-15
        pred = self.predict_(x_train)
        m = x_train.shape[0]
        cost = (-1/m) * (np.dot(y_train.T, (np.log(pred + eps))) + np.dot((1 - y_train).T, np.log(1 - pred + eps)))
        print("*****" + str(cost) + "*****")

df_train = pd.read_csv('./resources/train_dataset_clean.csv', delimiter=',', header=None, index_col=False)
x_train, y_train = np.array(df_train.iloc[:, 1:82]), df_train.iloc[:, 0]
df_test = pd.read_csv('./resources/test_dataset_clean.csv', delimiter=',', header=None, index_col=False)
x_test, y_test = np.array(df_train.iloc[:, 1:82]), np.array(df_train.iloc[:, 0])
model = LLR(alpha=0.0001, max_iter=1, verbose=True,learning_rate='constant')
model.fit(x_train, y_train)
model.score(x_test, y_test)
pre = model.predict_(x_train)
plt.plot(y_test, pre,'y.')
plt.show()
