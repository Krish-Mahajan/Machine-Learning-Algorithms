my_data=[['slashdot','USA','yes',18,'None'],
        ['google','France','yes',23,'Premium'],
        ['digg','USA','yes',24,'Basic'],
        ['kiwitobes','France','yes',23,'Basic'],
        ['google','UK','no',21,'Premium'],
        ['(direct)','New Zealand','no',12,'None'],
        ['(direct)','UK','no',21,'Basic'],
        ['google','USA','no',24,'Premium'],
        ['slashdot','France','yes',19,'None'],
        ['digg','USA','no',18,'None'],
        ['google','UK','no',18,'None'],
        ['kiwitobes','UK','no',19,'None'],
        ['digg','New Zealand','yes',12,'Basic'],
        ['slashdot','UK','no',21,'None'],
        ['google','UK','yes',18,'Basic'],
        ['kiwitobes','France','yes',19,'Basic']]




#######################################Testing####################################
#myTree=decisionnode()
from impurity import *
from  main import *
from drawtree import *
import pickle

#
#print(divideset(my_data,2,'yes'))
#print(main.uniquecounts(my_data))
#print(impurity.giniimpurity(my_data))
#print(impurity.entropy(my_data))
#set1,set2=main.divideset(my_data,2,'yes')
#print(impurity.entropy(set1))
#print(impurity.entropy(set2))
#tree=buildtree(my_data)
#print(type(tree))

#Testing pickle to save a node
#pickle.dump(tree,open("save.p","wb"))
tree=pickle.load(open("save.p","rb"))
#drawtree(tree,jpeg='treeview.jpg') 
 
'''
#Testing classify
from  classify import *
print(classify(['(direct)','USA','yes',5],tree))
'''
from prune import *
prune(tree,0.1)