
from impurity import *
from  buildtree import *
from drawtree import * 
from  classifier import *
import pickle 
from prune import *
from buildtree_pessimistic import *


#To print decision tree as an image:
def printtree(dataset=None,path="./Data",filename="data.p"):
        filepath=path+ "/"+ dataset + "/" + filename
        data=pickle.load(open(filepath,"rb"))
        #data=pickle.load(open("./Data/iris/folds/trainFold_1.p","rb"))
        writepath=path+ "/"+ dataset + "/treeview.jpg"
        writepath_pes=path+ "/"+ dataset + "/treeview_pes.jpg"
        
        tree=buildtree(rows=data[1:len(data)])
        tree_pes=buildtree_pessimistic(rows=data[1:len(data)])
        #colname=['sepal_length','sepal_width','petal_length','petal_width']
        drawtree(tree=tree,jpeg=writepath,colname=data[0]) 
        #drawtree(tree=tree,jpeg=writepath,colname=colname) 
        drawtree(tree=tree_pes,jpeg=writepath_pes,colname=data[0])
        #drawtree(tree=tree_pes,jpeg=writepath_pes,colname=colname)
        #drawtree(tree=prune(tree,0.3),jpeg=writepath,colname=data[0])
        
  
##############################
#printtree(dataset="iris")
#printtree(dataset="banknote")
#printtree(dataset="wine")
