# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    linear_model.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/10 12:22:13 by ythomas           #+#    #+#              #
#    Updated: 2020/02/10 15:13:21 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from mylinearregression import MyLR
import sys
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("./resources/are_blue_pills_magics.csv")
Xpill = np.array(data["Micrograms"]).reshape(-1,1)
Yscore = np.array(data["Score"]).reshape(-1,1)
theta1 = np.array([[89.0], [-8]])
theta2 = np.array([[89.0], [-6]])
mylm1 = MyLR(theta1)
mylm2 = MyLR(theta2)
print(Xpill)
print("========")
print(Yscore)
Y_lm1 = mylm1.predict_(Xpill)
plt.plot(Xpill, Yscore, 'g^')
y = Xpill * theta1[1] + theta1[0]
plt.plot(Xpill, y)
plt.grid(True)
plt.show()
print(mylm1.mse_(Xpill, Yscore))
print(mylm2.mse_(Xpill, Yscore))
