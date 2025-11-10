import matplotlib.pylab as plt
import numpy as np
subject =['Math','Chemistary','Physic','Science']
grade = [89,100,76,50]
plt.plot(subject,grade,marker='*',markersize=10,markerfacecolor='red')
plt.show()
################################################
# Ploting using Numpy array since they are faster than python lists
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
################################################
# Ploting using the same style
line_style = dict(marker='.'
         ,markersize=30
         ,markerfacecolor='yellow'
         ,markeredgecolor='red'
         ,linestyle='dashed'
         ,linewidth=3
         ,color='darkblue')
z = np.array([76,2,33,45,67])
plt.plot(x,z,**line_style)
plt.show()
################################################
# Adding title and naming x-axis and y-axis
plt.title('Class Size',fontsize=20, fontfamily='Arial', fontweight='bold', color='red')
plt.xlabel('Year',fontsize=20,fontfamily='Arial',fontweight='bold',color='blue')
plt.ylabel('Students',fontsize=20,fontfamily='Arial',fontweight='bold',color='blue')
plt.plot(x,z,**line_style)
plt.show()
################################################
# gride() = Helps make plots easier to read by adding reference lines.
x = [1,2,3,4,5]
y = [5,10,15,20,25]
plt.grid(axis='y',
         linewidth=2,
         color='gold',
         )
plt.plot(x,y)
plt.show()
################################################
# Bar Chart = compare categories of data by reperesenting each categor with a bar
