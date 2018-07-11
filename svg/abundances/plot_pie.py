#!/usr/bin/python
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
#from matplotlib.gridspec import GridSpec


sns.set(style="whitegrid")

cmap = plt.get_cmap('Spectral')
colors = [cmap(i) for i in np.linspace(0, 1, 7)]

# Make square figures and axes
#plt.figure(1, figsize=(20,10))
#the_grid = GridSpec(2, 2)

# create data
names='Alveolata', 'Rhizaria', 'Amoebozoa', 'Excavata', 'Stramenopiles', 'Archaeplastida', 'Others'
size=[0.4358,0.2591,0.1321,0.0803,0.03278,0.0223,0.03762]
 
# Create a circle for the center of the plot
my_circle=plt.Circle( (0,0), 0.7, color='white')


#Alveolata	0.4358
#Rhizaria	0.2591
#Amoebozoa	0.1321
#Excavata	0.0803
#Stramenopiles	0.03278
#Archaeplastida	0.0223
#Other	0.02433504


plt.pie(size, labels=names, colors=colors, autopct='%1.1f%%')


# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')  

#plt.tight_layout()

p=plt.gcf()
p.gca().add_artist(my_circle)
#plt.show()

plt.savefig( "neotrop_abundance_pie.svg", format='svg')
plt.savefig( "neotrop_abundance_pie.png", format='png')
