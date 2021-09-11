import numpy;
from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.mean(speed)
y= numpy.median(speed)
#mean is the average value
print("this is the average value of the speed array ", x)
print("this is the median of the speed array ", y)

#the mode value is the value that appears the most in a dataset --> scipy
z = stats.mode(speed)
print("this is the value that appears the most in the speed dataset ", z)



