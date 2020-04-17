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
    
    
