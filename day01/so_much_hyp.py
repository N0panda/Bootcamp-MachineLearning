# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    so_much_hyp.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/12 13:18:07 by ythomas           #+#    #+#              #
#    Updated: 2020/02/12 15:10:23 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
import matplotlib.pyplot as plt
from mylinearregression import MyLR
import pandas as pd

data = pd.read_csv("./resources/saturn_asteroids.csv")
X = np.array(data[['x1','x2']])
X2 = np.array(data[['x1**2','x2**2']])
Y = np.array(data[['y']])
hypo1 = MyLR([1., 1.])
hypo2 = MyLR([1., 1.])
print(hypo1.predict_(X))
print(hypo2.predict_(X2))
#hypo1.fit_(X[:,0], Y, alpha = 1e-4, n_cycle = 1e5)
#hypo2.fit_(X[:,1], Y, alpha = 1e-4, n_cycle = 1e5)
#hypo1.rmse_(X[:,0],Y)
#hypo2.rmse_(X[:,0],Y)
