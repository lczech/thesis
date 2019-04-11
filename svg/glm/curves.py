#!/usr/bin/python

import seaborn as sns; sns.set()
import matplotlib.pyplot as plt

#fmri = sns.load_dataset("fmri")
#ax = sns.lineplot(x="timepoint", y="signal", data=fmri)

#sns.plot( sin(x) )

import numpy as np
import matplotlib.pyplot as plt

ax = plt.subplot(111)

t = np.arange(-8.0, 8.0, 0.01)
#s = np.cos(2*np.pi*t)
#s = np.log(t/(1-t))
s = np.exp(t) / (1+np.exp(t))

line, = plt.plot(t, s, lw=2)

plt.xlim(-8.0,8.0)
plt.ylim(-0.1,1.1)
plt.show()
