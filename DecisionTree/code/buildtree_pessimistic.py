

from buildtree import *


def pessimistic_error(rows):
    class_dict=uniquecounts(rows)
    te=sum([i for i in class_dict.values() if i!=max(class_dict.values())])/float(len(rows))
    pe=(te+ no_leafnode*0.5)/len(dataset)
          

'''
Building Tree from Generalize pessimistic error
approach i,e 'll stop growing tree once Generalize pessimisric error
starts growing
'''
from impurity import *
def buildtree_pessimistic(rows,no_leafnode,scoref=entropy):
  
  #print("No of leafnode till now is",no_leafnode)
  if len(rows)==0: 
    no_leafnode=no_leafnode+1
    return decisionnode()
  current_score=scoref(rows)


  # Set up some variables to track the best criteria
  best_gain=0.0
  best_criteria=None
  best_sets=None
  
  
  column_count=len(rows[0])-1
  for col in range(0,column_count):
    # Generate the list of different values in
    # this column
    column_values={}
    for row in rows:
       column_values[row[col]]=1
    # Now try dividing the rows up for each value
    # in this column
    
    for value in column_values.keys():
      (set1,set2)=divideset(rows,col,value)
      
      # Information gain
      p=float(len(set1))/len(rows)
      gain=current_score-p*scoref(set1)-(1-p)*scoref(set2)
      if gain>best_gain and len(set1)>0 and len(set2)>0:
        best_gain=gain
        best_criteria=(col,value)
        best_sets=(set1,set2)
  # Create the sub branches   
  if best_gain>0:
    trueBranch=buildtree_pessimistic(best_sets[0],no_leafnode)
    falseBranch=buildtree_pessimistic(best_sets[1],no_leafnode)
    return decisionnode(col=best_criteria[0],value=best_criteria[1],
                        tb=trueBranch,fb=falseBranch)
  else:
    print("Leaf made")
    no_leafnode=no_leafnode+1
    #print("No of leafnode till now is",no_leafnode)
    return decisionnode(results=uniquecounts(rows))      
