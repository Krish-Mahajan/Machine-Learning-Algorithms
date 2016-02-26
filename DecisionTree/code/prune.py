
from buildtree import *  
from math import log

def pessimistic_error(rows):
    class_dict=uniquecounts(rows)
    pe=sum([i for i in class_dict.values() if i!=max(class_dict.values())])
    return pe

def  mdl_error(row1,row2): 

     class_dict=uniquecounts(row1+row2)
     class_dict1=uniquecounts(row1)
     class_dict2=uniquecounts(row2)

     no_of_classes=len(class_dict)
     no_of_attributes=4
     
     
     #no_of_nodes=10 #(It doesn't matter as during comparison it'll be subracted)
     #no_of_leafs=10 #(It doesn't matter as during comparison it'll be subracted)
     #n=100 #(it doesn't matter as during comparison it'll be subracted)
     e=sum([i for i in class_dict.values() if i!=max(class_dict.values())])
     e1=sum([i for i in class_dict.values() if i!=max(class_dict1.values())])
     e2=sum([i for i in class_dict.values() if i!=max(class_dict1.values())])
     
     #lambda function to calculate log2
     
     log2=lambda x:log(x)/log(2)
     
     mdl=log2(no_of_attributes)+2*log2(no_of_classes)+(e1+e2-e)*log2(1372)
     return mdl




def prune(tree):
  # If the branches aren't leaves, then prune them
  if tree.tb.results==None:
    prune(tree.tb)
  if tree.fb.results==None:
    prune(tree.fb)
    
  # If both the subbranches are now leaves, see if they
  # should merged
  if tree.tb.results!=None and tree.fb.results!=None:
    # Build a combined dataset
    tb,fb=[],[]
    for v,c in tree.tb.results.items():
      tb=tb+[[v]]*c
    for v,c in tree.fb.results.items():
      fb=fb+[[v]]*c
    
    # Test the reduction in pessimistic error
    
    pes_error=pessimistic_error(tb+fb)-((pessimistic_error(tb)+pessimistic_error(fb))+1)
    

    #Testing reduction in MDL
    '''
    mdl=mdl_error(tb,fb)
    '''
    #print(pes_error)
    if pes_error<=0:
    #if  mdl>25:
      #print("here")
      #print(mdl)
      # Merge the branches
      tree.tb,tree.fb=None,None
      tree.results=uniquecounts(tb+fb)
  return tree    