#!/usr/bin/python3

from sklearn.datasets import make_regression
from matplotlib import pyplot
import math
import random
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


num=100

# generate regression dataset
#x, y = make_regression(n_samples=num, n_features=1, noise=10)
#mn=min(x)
#mx=max(x)
#x = (x-mn)/(mx-mn)*90.0
#y = y/10

# plot regression dataset
#pyplot.scatter(x,y)
#sns.regplot(x=x, y=y)
#pyplot.show()

x = np.asarray([random.uniform(0.0, 90.0) for i in range(num)])
y = np.asarray([random.gauss(0.0, 12.0) for i in range(num)])
#y = np.asarray([random.uniform(-20.0, 20.0) for i in range(num)])

plt.figure( 1 )
ax = sns.regplot(x=x, y=y)
plt.ylim(-40, 40)
ax.set(xlabel='Latitude', ylabel='Balance')
plt.savefig( "balance_bad.svg", format='svg')

r = np.asarray([random.gauss(0.0, 3.0) for i in range(num)])
y = -(x - 45.0)/45.0*30.0 + r

plt.figure( 2 )
ax = sns.regplot(x=x, y=y)
plt.ylim(-40, 40)
ax.set(xlabel='Latitude', ylabel='Balance')
plt.savefig( "balance_good.svg", format='svg')
