
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



import matplotlib.pyplot as plt
plt.hist(df["sepal_length"])
plt.title ("Sepal Length")
plt.savefig ("sepal_length.png")
plt.clf()

plt.hist(df["sepal_width"])
plt.title ("Sepal Width")
plt.savefig ("sepal_width.png")
plt.clf()

plt.hist(df["petal_length"])
plt.title ("Petal Length")
plt.savefig ("petal_length.png")
plt.clf()

plt.hist(df["petal_width"])
plt.title ("Petal Width")
plt.savefig ("petal_width.png")
plt.clf()

import seaborn as sns
sns.set(style="ticks")

df = sns.load_dataset("C:\\Users\\User\\Desktop\\Iris-Data-set-analysis-project\\Irisdataset.txt")
sns.pairplot(df, hue="species")