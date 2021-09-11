#The Matplotlib module has a method for drawing scatter plots, it needs two arrays of 
#the same length, one for the values of the x-axis, and one for the values of the y-axis:

#The x array represents the age of each car.

#The y array represents the speed of each car.

import numpy
import matplotlib.pyplot as plt
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x,y)

#Create a function that uses the slope and intercept values to return a new value. 
#This new value represents where on the y-axis the corresponding x value will be placed:

def my_func(x):
    return slope*x + intercept

#Run each value of the x array through the function. This will result in a new array with new values for the y-axis:
myModel = list(map(my_func, x))
plt.scatter(x, y)

plt.plot(x, myModel)
plt.show()