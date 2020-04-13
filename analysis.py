
import csv


import pandas
#import numpy as np
#df = pandas.read_csv( "C:\\Users\\User\\Desktop\\Iris-Data-set-analysis-project\\Irisdataset.txt", index_col=0 )
#type (df)
#desc = df ["petal_width" ].describe()
#desc
#print(desc)

df = pandas.read_csv("C:\\Users\\User\\Desktop\\Iris-Data-set-analysis-project\\Irisdataset.txt", sep=',', names=["sepal_length", "sepal_width", "petal_length", "petal_width", "class"])
desc = df.describe('index_col=0')
print(desc)

#type (df)
#print (df)