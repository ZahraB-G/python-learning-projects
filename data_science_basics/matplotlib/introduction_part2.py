import matplotlib.pyplot as plt 
import numpy as np
# scatter graph = Shows the relationship between two variables
# Helps to identify a correlation (+, -, none)
# Example: Study hours vs. Test scores
x = np.array([0,1,1,2,3,4,5,6,7,7,8])# Hours Studies
y = np.array([55,60,65,62,68,70,75,78,82,85,87]) # Grades
plt.scatter(x,y,color='skyblue', alpha=0.5, s = 200, label='Class A')
plt.legend()
plt.title('Test Scores')
plt.xlabel('Hours Studied')
plt.ylabel('Grade')
plt.show()
################################################
z = np.array([0,1,2,2,3,4,5,6,7,8,8]) # Hours Studies
t = np.array([50,58,65,60,72,78,83,88,92,95,97]) # Grades
plt.scatter(z,t,color='red', alpha=0.5, s = 200, label='Class B')
plt.legend()
plt.title('Test Scores')
plt.xlabel('Hours Studied')
plt.ylabel('Grade')
plt.show()
################################################
# Histogram = A visual represeontation of the distribution of quantitative data.
# They group values into bins (intervals)
# and counts how many fall in each range.
scores = np.random.normal(loc=50, scale=10,size=100 )
scores = np.clip(scores,0, 100)
plt.hist(scores, bins=10, color='lightgreen',edgecolor='black')
plt.title('Exam Scores')
plt.xlabel('Score')
plt.ylabel('# of students')
plt.show()
################################################
# Figure = the entire canvas
# Ax = a singlle plot (subplot)
x = np.array([1,2,3,4,5])
figure, axes = plt.subplots(2,2)
axes[0,0].plot(x,x*2, color='red')
axes[0,0].set_title('x*2')
axes[0,1].plot(x,x**2, color='yellow')
axes[0,1].set_title('x**2')
axes[1,0].plot(x,np.log(x), color='blue')
axes[1,0].set_title('log2')
axes[1,1].plot(x,x**3, color='green')
axes[1,1].set_title('x**2')
plt.tight_layout()
plt.show()
