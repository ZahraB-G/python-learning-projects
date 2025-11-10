import matplotlib.pylab as plt
import numpy as np
subject =['Math','Chemistary','Physic','Science']
grade = [89,100,76,50]
plt.plot(subject,grade,marker='*',markersize=10,markerfacecolor='red')
plt.show()
################################################
x = np.array([1,2,3,4,5])
y = np.array([100,28,34,67,23])
plt.plot(x,y,marker='.'
         ,markersize=30
         ,markerfacecolor='yellow'
         ,markeredgecolor='red'
         ,linestyle='dashed'
         ,linewidth=3
         ,color='darkblue'
         )
plt.show()