#split dataset int a training set and a testing set
#80%for training, 20% for testing

#we will start with a dataset
import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

#plt.scatter(x, y)
#plt.show()

#The x axis represents the number of minutes before making a purchase.
#The y axis represents the amount of money spent on the purchase.

#we will now split into Test/Tain

#this :80 means that the test x values will contain 80% of random points from the original dataset
train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

#displaying the trainingset
#plt.scatter(train_x,train_y)
#plt.show()

#displaying the testing set
#plt.scatter(test_x, test_y)
#plt.show()

#we will now fit the datatset with polynomial regression
mymodel = numpy.poly1d(numpy.polyfit(train_x,train_y,4))
myline = numpy.linspace(0,6,100)

r2 = r2_score(train_y, mymodel(train_x))
print(r2)
plt.scatter(train_x, train_y)
plt.plot(myline, mymodel(myline))
plt.show()²