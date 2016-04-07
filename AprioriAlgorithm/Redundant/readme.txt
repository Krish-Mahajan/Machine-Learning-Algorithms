
# Apriori Algorithm
In this project, I have implemented famous  frequent itemset mining Algorithm **Apriori** as part of my assignment in Data Mining course (B565) at Indiana University under [Prof. Predrag Radivogac](http://www.cs.indiana.edu/~predrag/)   
I have implemented Apriori using Python. 
This implementation has the functionality to binarise regular dataset for general usage of Market Basket Data Analysis.  
I have also implemented support & confidence pruning Algorithm to keep a check on complexity of Apriori.   

###Sample steps to Execute the Algorithm:  
(Please note all the Datasets  are availaible in Data Folder.
These are the steps to run the Algorithm on Iris dataset.Exact steps can be replicated to run the algorithm on any of the 10 datasets availaible in data Folder)  

**1)** Change the Home Directory to "./code"" folder  
**2)** On the R console  run the following command ```data<-read.csv("./Data/nursery/nursery.data.txt",header=FALSE,sep=",")``` to read the raw text file
**3)** Now on the R console ```source("binarize.r")``` to compile binarize function  
**4)** Now on the R console ```binarize(data=data,dataset="nursery") ``` ,This 'll create a binarize csv file **binarize_nursery.csv** in ./Data/nursery/ folder  
**5)** On the python console run  ``` main.main(dataset="nursery",filename="binarize_nursery.csv",min_support=0.1,min_factor=0.50)``` to run the whole apriori Algorithm.  

**Note** The last step 'll create csv file of set of frequent itemsets with min_support=0.1,set of rules with either (confidence =0.50/lift=0.50).
Here the default method for frequent itemset generation is f(k-1) *f(k-1).

  
  

