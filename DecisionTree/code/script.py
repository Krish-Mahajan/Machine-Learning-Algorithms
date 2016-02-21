
from impurity import *
from  buildtree import *
from drawtree import * 
from  classify import *
import pickle 
from prune import *
from buildtree_pessimistic import *


#To print decision tree as an image:
def printtree(dataset=None,path="./Data",filename="data.p"):
        filepath=path+ "/"+ dataset + "/" + filename
        data=pickle.load(open(filepath,"rb"))
        writepath=path+ "/"+ dataset + "/treeview.jpg"
        tree=buildtree_pessimistic(rows=data[1:len(data)],no_leafnode=1)
        drawtree(tree=tree,jpeg=writepath,colname=data[0]) 
        writepath=path+ "/"+ dataset + "/treeview_prune.jpg"
        #drawtree(tree=prune(tree,0.3),jpeg=writepath,colname=data[0])
        

##############################
#printtree(dataset="iris")
#printtree(dataset="balancescale")
printtree(dataset="wine")
