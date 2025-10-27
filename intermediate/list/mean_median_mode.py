# Calculate mean, median and mode of a list
import statistics as st
list = [6,8,4,9,3,10,8,11,5,7,8,4,]
mean = st.mean(list)
median = st.median(list)
mode = st.mode(list)
print(f'Mean of the list is {mean}\nMedian is {median}\nMode is {mode}')
