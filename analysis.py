
import csv


import pandas

df = pandas.read_csv("C:\\Users\\User\\Desktop\\Iris-Data-set-analysis-project\\Irisdataset.txt")
attributes = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]
df.columns = attributes

desc = df.describe()
print(df.head() ,file = open("Summary File.txt", "a"))
print(desc ,file = open("Summary File.txt", "a"))

