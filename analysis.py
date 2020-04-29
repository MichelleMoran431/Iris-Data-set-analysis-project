

#Using Pandas module for data importing of CSV file and data manipulation
#Reference **: https://gist.github.com/curran/a08a1080b88344b0c8a7
              # https://realpython.com/python-csv/
              #https://stackoverflow.com/questions/36571560/directing-print-output-to-a-txt-file-in-python-3/36571602
            #https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342

#Use pandas to load the data and examine the data through descriptive statistics and data visualization.
import csv
import pandas
import numpy


df = pandas.read_csv("C:\\Users\\User\\Desktop\\Iris-Data-set-analysis-project\\Irisdataset.txt")
attributes = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"] 
df.columns = attributes

# Examining the content of datasets through statistics , info and first 5 data lines
perc =[.20,.40,.60,.80]
include = ['object','float','int']
desc = df.describe(percentiles = perc, include = include)
head  = df.head ()
info  = df.info


print(df.describe(percentiles = perc, include = include))

# output the results to a text file
df = open("Summary.txt", "w")
print(desc,file = df)
print(head,file = df)
print(info,file = df)
print (perc,file =df)
print (include, file =df)


#References : https://realpython.com/python-histograms/#building-up-from-the-base-histogram-calculations-in-numpy
#http://www.datasciencemadesimple.com/histogram-in-python-using-matplotlib/

# Plotting /visualising data in python
import matplotlib.pyplot as plt
df = pandas.read_csv("C:\\Users\\User\\Desktop\\Iris-Data-set-analysis-project\\Irisdataset.txt")
#Adding column headings to the dataframes via attributes
attributes = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]
df.columns = attributes


# Version no. 1 Histograms for each variable of the Iris data set using following modules

#References : https://www.machinelearningplus.com/plots/matplotlib-histogram-python-examples/

import matplotlib.pyplot as plt
import pandas
import numpy as np
from matplotlib.patches import Rectangle 

df = pandas.read_csv("C:\\Users\\User\\Desktop\\Iris-Data-set-analysis-project\\Irisdataset.txt")
# using attributes to name the columns in the dataframe 
attributes = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]
df.columns = attributes


plt.title ("Sepal Length in cm")
# Associating species type with attribute in dataframe
x1= df.loc[df.species == 'setosa','sepal_length']
x2= df.loc[df.species == 'versicolor','sepal_length']
x3= df.loc[df.species == 'virginica', 'sepal_length']
kwargs = dict(alpha=0.5, bins=20) #**kwargs is a dictionary of keyword arguments.
plt.hist(x1, **kwargs, color ='b', label = 'setosa',edgecolor='black')
plt.hist(x2, **kwargs,color ='r', label = 'versicolor',edgecolor='black')
plt.hist(x3, **kwargs,color ='g', label = 'virginica',edgecolor='black')
plt.xlim(3,9)
plt.xlabel("Sepal_Length_cm") 
plt.ylabel("Count")
plt.legend ()
plt.savefig ("sepal_length version 1.png")
plt.clf()


plt.title ("Sepal Width in cm")
x1= df.loc[df.species == 'setosa','sepal_width']
x2= df.loc[df.species == 'versicolor','sepal_width']
x3= df.loc[df.species == 'virginica', 'sepal_width']
kwargs = dict(alpha=0.5, bins=20)
plt.hist(x1, **kwargs, color ='b', label = 'setosa',edgecolor='black')
plt.hist(x2, **kwargs,color ='r', label = 'versicolor',edgecolor='black')
plt.hist(x3, **kwargs,color ='g', label = 'virginica',edgecolor='black')
plt.xlim(1,5)
plt.legend ()
plt.xlabel("Sepal_Width_cm") 
plt.ylabel("Count")
plt.savefig ("sepal_width version 1.png")
plt.clf()


plt.title ("Petal Length in cm")
x1= df.loc[df.species == 'setosa','petal_length']
x2= df.loc[df.species == 'versicolor','petal_length']
x3= df.loc[df.species == 'virginica', 'petal_length']
kwargs = dict(alpha=0.5, bins=20)
plt.hist(x1, **kwargs, color ='b', label = 'setosa',edgecolor='black')
plt.hist(x2, **kwargs,color ='r', label = 'versicolor',edgecolor='black')
plt.hist(x3, **kwargs,color ='g', label = 'virginica',edgecolor='black')
plt.xlim(0,9)
plt.legend()
plt.xlabel("petal_length_cm") 
plt.ylabel("Count")
plt.savefig ("petal_length version 1.png")
plt.clf()


plt.title ("petal width")
x1= df.loc[df.species == 'setosa','petal_width']
x2= df.loc[df.species == 'versicolor','petal_width']
x3= df.loc[df.species == 'virginica', 'petal_width']
kwargs = dict(alpha=0.5, bins=20) 
plt.hist(x1, **kwargs, color ='b', label = 'setosa',edgecolor='black')
plt.hist(x2, **kwargs,color ='r', label = 'versicolor',edgecolor='black')
plt.hist(x3, **kwargs,color ='g', label = 'virginica',edgecolor='black')
plt.xlim(0,3)
plt.legend()
plt.xlabel("petal_width_cm") 
plt.ylabel("Count")
plt.savefig ("petal_width version 1.png")
plt.clf()


#Reference:https://www.machinelearningplus.com/plots/matplotlib-histogram-python-examples/

# Version 2 : Histograms created using Seaborn module to better represent the Iris data se
import seaborn as sns
sns.FacetGrid(df,hue="species").map(sns.distplot,'petal_length').add_legend()

sns.FacetGrid(df,hue="species").map(sns.distplot,'petal_width').add_legend()

sns.FacetGrid(df,hue="species").map(sns.distplot,'sepal_width').add_legend()

sns.FacetGrid(df,hue="species").map(sns.distplot,'sepal_length').add_legend()


#Using Seaborn module to give a scatterplot representation of the variables in pairs using pairplot
#References : http://www.datasciencemadesimple.com/histogram-in-python-using-matplotlib/

import seaborn as sns
sns.set(style="ticks")
df = pandas.read_csv("C:\\Users\\User\\Desktop\\Iris-Data-set-analysis-project\\Irisdataset.txt")
sns.pairplot(df,hue='species')