import numpy

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

#will give 43 back which means that 75% of the people are 43yrs old or younger
x = numpy.percentile(ages, 75)

print("this is the percentile of the dataset age ", x)