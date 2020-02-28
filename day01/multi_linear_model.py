# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    multi_linear_model.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/10 15:13:57 by ythomas           #+#    #+#              #
#    Updated: 2020/02/11 13:53:01 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
import sys
import matplotlib.pyplot as plt
import pandas as pd
from mylinearregression import MyLR

data = pd.read_csv("./resources/spacecraft_data.csv")
Xage = np.array(data["Age"]).reshape(-1,1)
Xthrust = np.array(data["Thrust_power"]).reshape(-1,1)
Xtera = np.array(data["Terameters"]).reshape(-1,1)

#theta = np.array([[1.], [1.], [1.], [1.]])
Yprice = np.array(data[["Sell_price"]])
#Y = Yprice
#X = np.array(data[["Age", "Thrust_power", "Terameters"]])
#mylr = MyLR(theta)
#print(mylr.mse_(X, Y))
#plt.subplot(121)
#plt.xlabel('x1 : age')
#plt.ylabel('y : price')
#plt.plot(X.T[0], Y, '.r')
#X_pred = mylr.predict_(X)
#plt.plot(X.T[0], X_pred, '.k')
#plt.grid('True')


#plt.subplot(122)
#plt.xlabel('x1 : age')
#plt.ylabel('y : price')
#plt.plot(X.T[0], Y, '.r')
#mylr.fit_(X, Y, alpha = 9e-5, n_cycle = 10000)
#print(mylr.mse_(X, Y))
#X_pred = mylr.predict_(X)
#plt.plot(X.T[0], X_pred, '.k')
#plt.grid('True')
#plt.show()

#print(mylr.theta)

theta_age = np.array([[1000.0], [-1.0]])
theta_thrust = np.array([[0.], [-1.0]])
theta_tera = np.array([[800.0], [-1.0]])

Xage2 = np.hstack((Xage, np.full((Xage.shape[0], 1), 1)))
mylr_age = MyLR(theta_age)
mylr_thrust = MyLR(theta_thrust)
mylr_tera = MyLR(theta_tera)

plt.subplot(231)
plt.ylabel('y : sell price')
plt.xlabel('x1 : age')
plt.plot(Xage, Yprice, 'bo')
pred_age = mylr_age.predict_(Xage)
plt.plot(Xage, pred_age, 'm.')
plt.grid('True')

plt.subplot(232)
plt.ylabel('y : sell price')
plt.xlabel('x2 : Thrust Power')
plt.plot(Xthrust, Yprice, 'go')
pred_thrust = mylr_thrust.predict_(Xthrust)
plt.plot(Xthrust, pred_thrust, 'r.')
plt.grid('True')

plt.subplot(233)
plt.ylabel('y : sell price')
plt.xlabel('x3 : Terameters')
plt.plot(Xtera, Yprice, 'yo')
pred_tera = mylr_tera.predict_(Xtera)
plt.plot(Xtera, pred_tera, 'k.')
plt.grid('True')

plt.subplot(234)
plt.ylabel('y : sell price')
plt.xlabel('x1 : age')
plt.plot(Xage, Yprice, 'bo')
mylr_age.fit_(Xage, Yprice, alpha = 2.5e-5, n_cycle = 1000)
pred_age = mylr_age.predict_(Xage)
plt.plot(Xage, pred_age, 'm.')
plt.grid('True')

plt.subplot(235)
plt.ylabel('y : sell price')
plt.xlabel('x2 : Thrust Power')
plt.plot(Xthrust, Yprice, 'go')
mylr_thrust.fit_(Xthrust, Yprice, alpha = 2.5e-5, n_cycle = 1000)
pred_thrust = mylr_thrust.predict_(Xthrust)
plt.plot(Xthrust, pred_thrust, 'r.')
plt.grid('True')

plt.subplot(236)
plt.ylabel('y : sell price')
plt.xlabel('x2 : Terameters')
plt.plot(Xtera, Yprice, 'yo')
mylr_tera.fit_(Xtera, Yprice, alpha = 2.5e-5, n_cycle = 1000)
pred_tera = mylr_tera.predict_(Xtera)
plt.plot(Xtera, pred_tera, 'k.')
plt.grid('True')

plt.show()
