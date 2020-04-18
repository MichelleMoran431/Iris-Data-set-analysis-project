
import csv


import pandas

df = pandas.read_csv("C:\\Users\\User\\Desktop\\Iris-Data-set-analysis-project\\Irisdataset.txt")
attributes = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]
df.columns = attributes

#describe() Function gives the mean, std and IQR values. It excludes character column and calculate summary statistics only for numeric columns
desc = df.describe()
print(df.head() ,file = open("Summary File.txt", "a"))
print(desc ,file = open("Summary File.txt", "a"))

import matplotlib.pyplot as plt
df = pandas.read_csv("C:\\Users\\User\\Desktop\\Iris-Data-set-analysis-project\\Irisdataset.txt")
attributes = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]
df.columns = attributes


import numpy as np
import matplotlib.pyplot as plt
import pandas


plt.title ("Sepal Length in cm")
x = df["sepal_length"]
plt.hist( x, bins = 20, color = "green", edgecolor="black") 
plt.xlabel("Sepal_Length_cm") 
plt.ylabel("Count")
plt.savefig ("sepal_length.png")
plt.clf()


plt.title ("Sepal Width in cm")
x = df["sepal_width"]
plt.hist( x, bins = 20, color = "green", edgecolor="black") 
plt.xlabel("Sepal_Width_cm") 
plt.ylabel("Count")
plt.savefig ("sepal_width.png")
plt.clf()

import numpy as np
import matplotlib.pyplot as plt
import pandas



plt.title ("Petal Length in cm")
x = df["petal_length"]
plt.hist( x, bins = 20,color = "green", edgecolor="black") 
plt.xlabel("petal_length_cm") 
plt.ylabel("Count")
plt.savefig ("petal_length.png")
plt.clf()


plt.title ("petal width")
x = df["petal_width"]
plt.hist( x,bins = 20, color = "green", edgecolor="black") 
plt.xlabel("petal_width_cm") 
plt.ylabel("Count")
plt.savefig ("petal_width.png")
plt.clf()

