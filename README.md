# Iris-Data-set-analysis-project
#Programming and Scripting Project 2020#

##1. The Iris Data Set##

References : 

http://archive.ics.uci.edu/ml/datasets/iris
https://en.wikipedia.org/wiki/Iris_flower_data_set

###Background###

The Iris flower data set is an example of a multivariate data set developed by the British statistician and biologist Ronald Fisher using data collected by Edgar Anderson, an american biologist.
Fisher developed a linear discrimnant model to distinguish between the species of Iris.

###The Data Set###

The data set consists of 50 samples of each class of Iris, 150 rows and 4 columns of data : 

Data Set Class and Attributes details:

1. Class
    *Iris Setosa
    *Iris Versicolor
    *Iris Virginica
2. Attributes
    *sepal length in cm
    *sepal width in cm
    *petal length in cm
    *petal width in 



####Download the data set and add it to a Repository####

GITHUB URL : https://github.com/g00387856/Iris-Data-set-analysis-project.git

Data set downloaded from the UCI - Machine Learning Repository, center for machine learning and intelligent systems. It is saved as a txt.file called Irisdataset.txt , an example of a CSV file.


            
3. Write a Program called analysis.py to do the follow : 
  
    1. Outputs a summary of each variable to a single text file:
    
      1.1 Import modules : CSV and Pandas - Using Pandas to call up "Irisdataset.txt" from desktop folder. 
          Create a df ( dataframe) - associating data from the Irisdataset.txt
      1.2 Identify the column headings and add the columns headings as attributes to the dataframe (df)
      1.3 Using the describe() to give a statistical summary output for each variable
      1.4 print(df.head()) - Returns the first 5 rows of the dataframe ( however you can input any no. in the parenthesis not just 5)
      1.5 print(desc ,file = open("Summary File", "a")) -outputs the summary results to a txt. file
   
   Reference :
                https://realpython.com/python-csv/ - how to read and write to files in python
                https://gist.github.com/curran/a08a1080b88344b0c8a7 - assigning attributes
                https://stackoverflow.com/questions/36571560/directing-print-output-to-a-txt-file-in-python-3 - outputing to a text file                 in python
      
     2. Create a histogram of each variable to png files
     
   References : https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/
    
    
