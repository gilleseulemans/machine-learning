#here we will learn how to create an array where the values are concentrated around a given value
#in probability theory this is known as the normal data distribution or the gaussian data distribution

#this is a typical normal data distribution
import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(5.0, 1.0, 100000)

plt.hist(x,100)
plt.show()
