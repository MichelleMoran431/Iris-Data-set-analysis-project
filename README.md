##          ** # THE IRIS FLOWER DATA SET-Project 2020**
				



**PROJECT REPORT** - Submitted by:Michelle Moran - Student Number: G00387856

**Programming & Scripting - Higher Diploma in Data Analytics - Galway Mayo I.T.**

**Submission Date**: 29th April 2020												


	
	
### 1. The Iris Data Set

###**1.1** **Introduction**

**1.1.1 Aim**

The aim of this project is to investigate "The Iris Flower Data Set" through  researching and documenting my findings. To use python code to investigate it. To understand the importance of this dataset in terms of machine learning and why its most commonly used as an example.

I hope to break this project into several smaller tasks as follows : 

* **Research** data set online - write a summary in README. using the markdown 

* **Download the dataset** and add it to my repository

* **Write a program** using python programing code calling it analysis.py to include the following tasks :

*   A summary of each variable is output to a single text file
*   Create a **histogram** of each variable to png files
*   To output a **scatter plot** of each pair of variables

•	Moodle page - internal college site used to access class notes and videos


#### **1.2  Background**[1,2,3,4,5]

The Iris flower data set is an example of a multivariate data set developed by the British statistician and biologist Ronald Fisher using data collected by Edgar Anderson, an american biologist.Fisher developed a linear discrimnant model to distinguish between the species of Iris.

The data set consists of 50 sames of each class of Iris, 150 rows and 4 columns of data :

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

This particular data set is good example of how  to classify iris flowers among three species (setosa, versicolor or virginica) from measurements of length and width of sepals and petals .This is a widely used dataset by everyone trying to learn machine learning and statistics.
Machine learning can be defined as

*"Machine learning is an application of artificial intelligence (AI) that provides systems the ability to automatically learn and improve from experience without being explicitly programmed. Machine learning focuses on the development of computer programs that can access data and use it learn for themselves"* 

Python is the most popular, general purpose programming language suitable for a variety of tasks in machine learning. 

Some advantages of using the Iris flower dataset is : 

* Attributes are numeric 
* It is a classification problem, allowing you to practice with perhaps an easier type of supervised learning algorithm.
* It only has 4 attributes and 150 rows, meaning it is small and easily fits into memory (and a screen or A4 page).
* All of the numeric attributes are in the same units and the same scale, 

**1.3 Download the data set and add it to a Repository**[1,6,7]

* Created the repository  called  'Iris-Data-set-analysis-project - reference

			https://github.com/g00387856/Iris-Data-set-analysis-project.git

* Using Visual Studio Code as the text editor - I called up the desktop folder *Iris-Data-set-analysis-project* and created file called *Irisdataset.txt* for my programming called *Analysis.py*. This file is an example of CSV file , comma separated file. 
* Imported python modules Pandas and CSV  to load the Iris flower data set ( which was saved in forementioned folder). This created a dataframe (df) - also using attributes , column headings were added.

				df = pandas.read_csv("C:\\Users\\User\\Desktop\\Iris-Data-set-analysis-project\\Irisdataset.txt")
				attributes = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]
				df.columns = attributes
* Pandas is also used to investigate the data through summary statistics and data visualisation via matplotlib and seaborn modules.
            
       
														 
#### 1.4 To output a summary of each variable to a single text file [12,13,14]:


*  Using Pandas **describe()** to view statistical details like percentile, mean, std etc. for each variable -
      
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

Conclusions about Iris Flower data Set from the summary file : 

The sepal length measurements gives the largest range difference of all species of 5.9cm between the min 1.0 - max 6.9 .This would be the category that covers the largest range of the data.The other categories range is as follows: Petal Length - 3.6cm Petal Width - 2.4cm Sepal Width - 2.4cm


#### 1.5   Data Visualisation


##### **1.5.1 Univariate plots :Histogram of each variable ** [14,15,16,17,18]**


Aim :To better understand each attribute.

For the IRIS dataset - we need the histogram to answer the following question :Which among the four variables is more useful than other variables in order to distinguish between the species of Iris flower ? 

A Histogram is is a visual tool for quickly assessing the probability distribution ( or PDF - Probability density function).


Definitions :

* Probability Density Function (PDF) is the probability that the variable takes a value x. (smoothed version of the histogram)
* Kernel Density Estimate (KDE) is the way to estimate the PDF. The area under the KDE curve is 1.


Two methods of creating histograms investigated:

Version 1 : Using  matplotlib.pyplot. 
Version 2 : Using Seaborn package 


**Version 1:**

Import module **matplotlib.pyplot as plt** and **Pandas**

Below is the code used to create a histogram  for each of the attributes ( input each variable)  . These histograms  distinguishes between the species for each attribute. All histograms are saved as a .png file. Version 1 coding is long winded and labour intensive between having to associate the attribute with its species and making the plot more aesthetically pleasing to the eye. 



					plt.title ("**Sepal Length** in cm")
					x1= df.loc[df.species == 'setosa','sepal_length']
					x2= df.loc[df.species == 'versicolor','sepal_length']
					x3= df.loc[df.species == 'virginica', 'sepal_length']
					kwargs = dict(alpha=0.5, bins=20)
					plt.hist(x1, **kwargs, color ='b', label = 'setosa',edgecolor='black')
					plt.hist(x2, **kwargs,color ='r', label = 'versicolor',edgecolor='black')
					plt.hist(x3, **kwargs,color ='g', label = 'virginica',edgecolor='black')
					plt.xlim(3,9)
					plt.xlabel("Sepal_Length_cm") 
					plt.ylabel("Count")
					plt.legend ()
					plt.savefig ("sepal_length version 1.png")
					plt.clf()
     
  **Version 2:**
	
Import module **Seaborn as sns**
	
	
	
By using Seaborn , we can plot the probability density function(PDF) with each feature as a variable on X-axis and it’s histogram and corresponding kernel density plot on Y-axis

Plotting the Histogram & PDF using Seaborn FacetGrid object —

FacetGrid object takes the dataframe as input and the names of the variables that will form the row, column, or hue dimensions of the grid.
Distribution plots in seaborn are used to visually assess how the data points are distributed with respect to its frequency.Histograms and KDE can be combined using distplot.

Definition :
* Kernel Density Estimate (KDE) is the way to estimate the PDF. The area under the KDE curve is 1.

An advantage to using Seaborn here is it uses alot less coding and interacts directly with dataframe . 
	
					sns.FacetGrid(df,hue="species").map(sns.distplot,'petal_length').add_legend()
					sns.FacetGrid(df,hue="species").map(sns.distplot,'petal_width').add_legend()
					sns.FacetGrid(df,hue="species").map(sns.distplot,'sepal_width').add_legend()
					sns.FacetGrid(df,hue="species").map(sns.distplot,'sepal_length').add_legend()
	
Conclusions 

Examining version 1 Histograms ( created using matplotlib )  you can conclude that there the variables Petal length and width data could be used to distinguish the species Setosa clearly from the others species. 
However looking at histogram plots created by seaborn as sns , version 2 , the density plots of the petal width show there is a small overlapping between species setosa and versicolor. So overall petal length can be used to distinguish the species Setosa . Looking at the actual figures for petal length with regards Versicolor and Virginica species , the overlapping occurs at around 4.8 cm, but the majority of versicolor have petal length less than 4.8 whereas the majority of virginica have petal length greater than 4.8. Again because of the overlapping there is still a chance of misidentification.



![](https://miro.medium.com/max/1106/1*AnGVVtk9pEuMl_uiwcPIyQ.png)


1.5.2 Multivariate Plots  :Scatter plot of each pair of variables ** []**

**Import seaborn as sns**

The pairs plot builds on the histogram and the scatter plot. The histogram on the diagonal allows us to see the distribution of a single variable while the scatter plots on the upper and lower triangles show the relationship (or lack thereof) between two variables. 
		 
			import seaborn as sns
			sns.set(style="ticks")
			df = pandas.read_csv("C:\\Users\\User\\Desktop\\Iris-Data-set-analysis-project\\Irisdataset.txt")
			sns.pairplot(df,hue='species')
			



![](https://miro.medium.com/max/1400/1*v34h7DKNcw74qtQxjpHUbA.png)
			
			







		 
##     ***References* **:
[1] http://archive.ics.uci.edu/ml/datasets/iris
[2]https://en.wikipedia.org/wiki/Iris_flower_data_set
[3]https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342
[4]https://expertsystem.com/machine-learning-definition/
[5]https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
[6]https://realpython.com/python-histograms/#building-up-from-the-base-histogram-calculations-in-numpy
[7]http://www.datasciencemadesimple.com/histogram-in-python-using-matplotlib/
[8]https://gist.github.com/curran/a08a1080b88344b0c8a7
[9]https://realpython.com/python-csv/
[10]GMIT Programming and Scripting Module on Moodle: Topic 8 Presentations
[11]https://stackoverflow.com/questions/36571560/directing-print-output-to-a-txfile-in-python-3/36571602
[12]https://realpython.com/python-csv/ - how to read and write to files in python
[13]https://gist.github.com/curran/a08a1080b88344b0c8a7 - assigning attributes
[14]https://realpython.com/python-histograms/#building-up-from-the-base-histogram-calculations-in-numpy
[15]http://www.datasciencemadesimple.com/histogram-in-python-using-matplotlib/
[16]https://www.machinelearningplus.com/plots/matplotlib-histogram-python-examples
[17]https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/
[18]https://medium.com/analytics-vidhya/exploratory-data-analysis-uni-variate-analysis-of-iris-data-set-690c87a5cd40

														 