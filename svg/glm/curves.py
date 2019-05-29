#!/usr/bin/python

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import pandas as pd
import statsmodels.api as sm
import seaborn as sns
import os

#fmri = sns.load_dataset("fmri")
#ax = sns.lineplot(x="timepoint", y="signal", data=fmri)

#sns.plot( sin(x) )

log_data = pd.read_csv( "logistic_regression.csv", sep="," )
# Predictor,Response

def plot_logistic():
	ax = plt.subplot(111)

	t = np.arange(-8.0, 8.0, 0.01)
	#s = np.cos(2*np.pi*t)
	#s = np.log(t/(1-t))
	s = np.exp(t) / (1+np.exp(t))

	line, = plt.plot(t, s, lw=2)

	plt.xlim(-8.0,8.0)
	plt.ylim(-0.1,1.1)
	plt.show()

def plot_dots():

	x=log_data["Predictor"]
	y=log_data["Response"]
	min_x = x.min()
	max_x = x.max()
	
	# Plot the data points on top
	plt_data = sns.scatterplot( x=log_data["Predictor"], y=log_data["Response"], marker="o", color="k", label="Data", zorder=3 )
	
	# Plot a horizontal line representing the null model
	mean = log_data["Response"].mean()
	plt_null = sns.lineplot( x=[ min_x, max_x ], y=[ mean, mean ], marker="", color="C1", label="Null Model", zorder=0 )
	
	# Plot the saturated model that reaches every data point
	plt_sat = sns.lineplot( x=log_data["Predictor"], y=log_data["Response"], marker="", color="C0", label="Saturated Model", zorder=2 )
	
	# Fit a GLM to the data
	model = sm.GLM(endog=log_data["Response"], exog=log_data["Predictor"], family=sm.families.Binomial())
	fit = model.fit()
	#print(fit.summary())
	#print("params", fit.params["Predictor"])
	#print("tvalues", fit.tvalues["Predictor"])
	#sns.lineplot( x=log_data["Predictor"], y=fit.fittedvalues, marker="o", color="C1", label="Test" )
	
	# Get the params of the logistic function
	b1=fit.params["Predictor"]
	b0=fit.tvalues["Predictor"]
	#print( "min_x", min_x, "max_x", max_x, "b1", b1, "b0", b0 )
	
	# Plot the GLM fit
	t = np.arange(min_x, max_x, 0.05)
	#t = 2.217 + 0.2667 * v
	#v = ( t - 2.217 ) / 0.2667
	v = ( t - b0 ) / b1
	s = np.exp(v) / (1+np.exp(v))
	plt_log = sns.lineplot(t, s, color="C2", label="Fitted Logistic Model", zorder=1 )
	
	# Get the desired legend order... this sucks
	#plt_order = [ plt_data, plt_null, plt_sat, plt_log ]
	ax = plt.gca()
	#ax.legend( plt_order, [p.get_label() for p in plt_order] )
	handles, labels = ax.get_legend_handles_labels()
	#labels, handles = zip(*sorted(zip(labels, handles), key=lambda t: t[0]))
	handles = [ handles[3], handles[0], handles[1], handles[2] ]
	labels  = [ labels[3],  labels[0],  labels[1],  labels[2] ]
	ax.legend(handles, labels)
	
	#ax.legend()
	#plt.add_legend(label_order = [0,1,2,3])
	fig = plt.gcf()
	figsize = fig.get_size_inches()
	figsize[0] *= 1.5
	fig.set_size_inches(figsize)
	plt.tight_layout()
	#plt.show()
	plt.savefig("logistic_regression.svg", format='svg')
	#plt.savefig("logistic_regression.pdf", format='pdf')
	
plot_dots()
