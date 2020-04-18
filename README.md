# Iris-Data-set-analysis-project
Programming and Scripting Project 2020
Aim : To complete the following  by breaking them into several smaller tasks that are easier to solve and combining together once completed
  -Research the data set online and write a summary in this Readme file.
  -Download the data set and add it to this repository
  - Write a program called analysis.py that: 
    - outputs a summary of each variable to a single text file
    - save a histogramof each variable to png files
    - outputs a scatter plot of each pair of variables


1. The Iris Data Set



2. Download the data set and add it to the Repository:

Data set downloaded from the UCI - Machine Learning Repository, center for machine learning and intelligent systems

Reference : http://archive.ics.uci.edu/ml/datasets/iris 
            https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x - Fishers Original Paper
            https://gist.github.com/curran/a08a1080b88344b0c8a7
            
3. Write a Program called analysis.py to do the follow : 
  
    1. -  **Outputs a summary of each variable to a single text file**
    
      1.1  - Import modules : **CSV and Pandas** - Using Pandas to call up "Irisdataset.txt" from desktop folder. 
          Create a df ( dataframe) - associating data from the Irisdataset.txt
          Pandas is used for working with tabular data e.g. CSV files , by creating dataframes. 
          
      1.2  - Identify the column headings and add the columns headings as attributes to the dataframe (df)
      1.3 -  Using the **describe()** to give a statistical summary output for each variable -
      
      count    150.000000   150.000000    150.000000   150.000000
      mean       5.843333     3.054000      3.758667     1.198667
      std        0.828066     0.433594      1.764420     0.763161
       min        4.300000     2.000000      1.000000     0.100000
      25%        5.100000     2.800000      1.600000     0.300000
      50%        5.800000     3.000000      4.350000     1.300000
      75%        6.400000     3.300000      5.100000     1.800000
      max        7.900000     4.400000      6.900000     2.500000
  
      1.4  - **print(df.head())** - Returns the first 5 rows of the dataframe ( however you can input any no. in the parenthesis not just              5)
      
      <<<<<<< HEAD
     sepal_length  sepal_width  petal_length  petal_width     class
       0             5.1          3.5           1.4          0.2  setosa
       1             4.9          3.0           1.4          0.2  setosa
       2             4.7          3.2           1.3          0.2  setosa
        3            4.6          3.1           1.5          0.2  setosa
        4            5.0          3.6           1.4          0.2  setosa
        
      **1.5  - print(desc ,file = open("Summary File", "a"))** 
        Prints the outputs which is the summary results to a txt. file called "Summary File". 
        It was realised that everytime the "analysis.py" file was saved and ran , it updated the summary file. By updating this file, it         repeated the statistical summary output for each variable and the head information. 
        To overcome this , even though it could be deemed as expected error, a time stamp could be added or before making the last        commit to git hub deleting all the duplicate entries leaving just one representation.
      
   **Reference :
                https://realpython.com/python-csv/ - how to read and write to files in python
                https://gist.github.com/curran/a08a1080b88344b0c8a7 - assigning attributes
                https://stackoverflow.com/questions/36571560/directing-print-output-to-a-txt-file-in-python-3 - outputing to a text file                 in python
      
     2. Create a histogram of each variable to png files
     
     Firstly to define what Histograms is : it is a visual tool for quickly assessing the probability distribution ( or PDF - Probability density function. For the IRIS dataset - the histogram represents the probability distribution of each of the variabelse for each of the species.In python , the histograms Y axis tells the count of flower at a particular x axis or how often they come at this value. 
Below is the code for creating a histogram of a variable :

Import module **matplotlib.pyplot as plt**
Where we assign the variable to x and use plt.hist to create histogram. 

plt.title ("Sepal Length in cm")
x = df["**Variable**"]
plt.hist( x, bins = 20, color = "green", edgecolor="black") 
plt.xlabel("Sepal_Length_cm") 
plt.ylabel("Count")
plt.savefig ("sepal_length.png")
plt.clf()
     
     
     
     
   References : https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/
    
    
