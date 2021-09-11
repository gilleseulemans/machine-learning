import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 5.0, 100000)
print(x)
#this will show a histogram which is made out of a random dataset created by random.unifrom(0.0,5.0,100000) this gives 100000 random floats bewteen 0 and 5
plt.hist(x, 100)
plt.show()