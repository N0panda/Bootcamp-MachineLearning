# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    normal_equation_model.py                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/11 13:14:51 by ythomas           #+#    #+#              #
#    Updated: 2020/02/11 16:12:49 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
import sys
import matplotlib.pyplot as plt
import pandas as pd
from mylinearregression import MyLR

data = pd.read_csv("./resources/spacecraft_data.csv")
X = np.array(data[["Age", "Thrust_power", "Terameters"]])
Y = np.array(data[["Sell_price"]])
theta = np.array([[1.], [1.], [1.], [1.]])
mylr_ne = MyLR(theta)
mylr_lgd = MyLR(theta)

Y_pred = mylr_ne.predict_(X)

############### Gradient descente ############
print("Basic cost = " + str(mylr_lgd.mse_(X, Y)))
mylr_lgd.fit_(X,Y, alpha = 5e-5, n_cycle = 10000)
print("Cost after gradient descente = " + str(mylr_lgd.mse_(X, Y)))
print("Theta after gradient descente = " + str(mylr_lgd.theta))
Y_grad = mylr_lgd.predict_(X)
##############################################

#print()

############# Normale Equation ###############
mylr_ne.normalequation_(X,Y)
print("Cost after Normale equation = " + str(mylr_ne.mse_(X, Y)))
print("Theta after normale equation = " + str(mylr_ne.theta))
Y_ne = mylr_ne.predict_(X)
##############################################


plt.plot(X.T[0], Y, 'co:')
plt.plot(X.T[0], Y_grad, 'g.')
plt.plot(X.T[0], Y_ne, 'y.')
plt.grid('True')
plt.xlabel("x1 : age")
plt.ylabel("Y : Selling price")
plt.show()
