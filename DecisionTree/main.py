

from treenode import *

#function that tells us if a row is in the first group(True)
#or the second group(false)	
def divideset(rows,column,value):
	split_function=None
	if isinstance(value,int) or isinstance(value,float):
		split_function=lambda row:row[column]>=value
	else:
		split_function=lambda row:row[column]==value

	#Divide the rows into two sets and return them
	set1=[row for row in rows if split_function(row)]
	set2=[row for row in rows if not split_function(row)]
	return (set1,set2)		

def uniquecounts(rows):
	results={}
	for row in rows:
		#The result is the last column
		r=row[len(row)-1]
		if r not in results:results[r]=0
		results[r]=results[r]+1
	return results	


#Building the tree
from  impurity import *
def buildtree(rows,scoref=entropy):
	if len(rows)==0:
		return decisionnode()
	current_score=scoref(rows)

	#Set up some variables to track the bst criteria
	best_gain=0.0
	best_criteria=None
	best_sets=None

	column_count=len(rows[0])-1	
	for col in range(0,column_count):

		#generate the list of different values in this column
		column_values={}
		for row in rows:
			column_values[row[col]]=1

		#Dividing the rows for each value in this column
		for value in column_values.keys():
			(set1,set2)=divideset(rows,col,value)
		
		#information gain
		p=float(len(set1)/len(rows))
		gain=current_score-p*scoref(set1)-(1-p)*scoref(set2)
		if gain>best_gain and len(set1)>0 and len(set2)>0:
			best_gain=gain
			best_criteria=(col,value)
			best_sets=(set1,set2)
	
	# Create the subbranches		
	
	if best_gain>0:
		trueBranch=buildtree(best_sets[0])
		falseBranch=buildtree(best_sets[1])
		return decisionnode(col=best_criteria[0],value=best_criteria[1],
			tb=trueBranch,fb=falseBranch)
	else:
		return decisionnode(results=uniquecounts(rows))	

	
