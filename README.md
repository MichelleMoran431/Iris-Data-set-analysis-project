# Iris-Data-set-analysis-project
# **Iris-Data-set-analysis-Project**
## Programming and Scripting Project 2020

### 1. The Iris Data Set

***References*** :
* http://archive.ics.uci.edu/ml/datasets/iris
* https://en.wikipedia.org/wiki/Iris_flower_data_set

#### Background

The Iris flower data set is an example of a multivariate data set developed by the British statistician and biologist Ronald Fisher using data collected by Edgar Anderson, an american biologist.
Fisher developed a linear discrimnant model to distinguish between the species of Iris.

#### The Data Set

The data set consists of 50 samples of each class of Iris, 150 rows and 4 columns of data :

**Data Set Class and Attributes details**:
 - []
 **Class**
* *Iris Setosa
* 
* *Iris Versicolor
* 
* *Iris Virginica
* 
 - [
] **Attributes**
*    *sepal length in cm
*    
*    *sepal width in cm
*    
*    *petal length in cm
*    
*    *petal width in cm


Here are the three Classes of Iris examined :

![](https://cdn-images-1.medium.com/max/1000/1*gwmXliaxIBkY4NQBhoe9JQ.png)

* 
#### **Download the data set and add it to a Repository**

**Reference **: http://archive.ics.uci.edu/ml/datasets/iris 

**Project Github URL** : 

* https://github.com/g00387856/Iris-Data-set-analysis-project.git

Data set downloaded from the UCI - Machine Learning Repository, center for machine learning and intelligent systems. It is saved as a txt.file called Irisdataset.txt , an example of a CSV file. 
            
            
#### **Write a Program called analysis.py to do the following:**

**Reference **: https://gist.github.com/curran/a08a1080b88344b0c8a7
														https://realpython.com/python-csv/
													  GMIT Programming and Scripting Module: Topic 8 Presentations
														 https://stackoverflow.com/questions/36571560/directing-print-output-to-a-txt-                              file-in-python-3/36571602
														 
														 
1. To output a summary of each variable to a single text file :

* Pandas package was imported as it makes importing and analyzing data easy in python.
The CSV text file "Irisdataset.txt was read from the desktop folder and a dataframe (df) created of the same file name which can be viewed in python:

		df = pandas.read_csv( filename)
		
* Column names were added to the dataframe through attributes :
	
		Attributes = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"] 
		df.columns = attributes

*  Pandas **describe()** is used to view statistical details like percentile, mean, std etc. for each variable -
      
|       | sepal_length | sepal_width | petal_length | petal_width |
|-------|:------------:|------------:|--------------|-------------|
| count |  150.000000  |  150.000000 |  150.000000  |  150.000000 |
| mean  |   5.843333   |   3.054000  |   3.758667   |   1.198667  |
| std   |   0.828066   |   0.433594  |   1.764420   |   0.763161  |
| min   |   4.300000   |   2.000000  |   1.000000   |   0.100000  |
| 25%   |   5.100000   |   2.800000  |   1.600000   |   0.300000  |
| 50%   |   5.800000   |   3.000000  |   4.350000   |   1.300000  |
| 75%   |   6.400000   |   3.300000  |   5.100000   |   1.800000  |
| max   |   7.900000   |   4.400000  |   6.900000   |   2.500000  |






* Using **print(df.head())** - Returns the first 5 rows of the dataframe ( however you can input any no. in the parenthesis not just  5)
     

* To output the summary as a single text file , I used the following code : 

						desc = df.describe()
						head  = df.head ()
						info  = df.info

						df = open("SummaryA.txt", "w")
						print(desc,file = df)
						print(head,file = df)
						print(info,file = df)

Where I defined describe / head / info in terms of the dataframe (df) and then I opened the file ( given it name in the parenthesis) and then passed that variable to print's file option, I used "w" to overwrite the file everytime the code is ran.
Prints the outputs which is the summary results to a txt. file called "SummaryA File". 
       
   **Reference :
                https://realpython.com/python-csv/ - how to read and write to files in python
                https://gist.github.com/curran/a08a1080b88344b0c8a7 - assigning attributes
                https://stackoverflow.com/questions/36571560/directing-print-output-to-a-txt-file-in-python-3 - 
      
   2. Create a histogram of each variable to png files
     
A Histogram is is a visual tool for quickly assessing the probability distribution ( or PDF - Probability density function). For the IRIS dataset - the histogram represents the probability distribution of each of the variable for each of the species.In python , the histograms Y axis tells the count of flower at a particular x axis or how often they come at this value. 
Below is the code for creating a histogram of a variable :

Import module **matplotlib.pyplot as plt**
Where we assign the variable to x and use plt.hist to create histogram. 

		plt.title ("Sepal Length in cm")  # title of plot
		x = df["**Variable**"] # assigning a variable to x
		plt.hist( x, bins = 20, color = "green", edgecolor="black") # create histogram with the characteristics : bins (intervals) / Colour /edgecolor
		plt.xlabel("Sepal_Length_cm") #Assigning axsis lables
		plt.ylabel("Count")
		plt.savefig ("sepal_length.png")# saving to a png file
		plt.clf() #Close plt to revent overlapping of future plts
     
     
     
     
   References : https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/