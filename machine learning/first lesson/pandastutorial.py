import pandas
from sklearn import linear_model
#reading the file
df = pandas.read_csv("cars.csv")

#make list of independent values, these are the x values
#the dependent values we will store these in the y value
X = df[['Weight', 'Volume']]
y  = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X,y)
#Now we have a regression object that are ready to predict CO2 values based on a car's weight and volume:
#predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
predictedCo2 = regr.predict([[2300,1300]])
print(predictedCo2)

#this pritns the coeficient of the regression object
print(regr.coef_)

#We have predicted that a car with 1.3 liter engine, and a weight of 2300 kg, 
#will release approximately 107 grams of CO2 for every kilometer it drives.