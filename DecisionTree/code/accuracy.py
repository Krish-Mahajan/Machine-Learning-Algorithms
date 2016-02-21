

from classify import *
import pickle
from buildtree import *

'''
Function to calculate accuracy of decision tree 
on 10 folds.
'''
def accuracy10Fold(dataset=None,path="./Data"):
	
    # Training & Testing on corresponding Train Test pair.
	accuracyList=[]
	for f in range(1,11):
		#print("Building model from Training fold ",f)
		foldPath=path+"/" + dataset + "/folds/"
		
		#Loading trainFold
		trainFoldData=pickle.load(open(foldPath + "trainFold_"+str(f)+".p","rb"))

		#making decision Tree on this trainFold
		tree=buildtree(trainFoldData)
		#print("Testing model for Testing fold",f)
		#Loading tesfold to check accuracy of the model
		testFoldData=pickle.load(open(foldPath + "testFold_"+str(f)+".p","rb"))
		
		# Checking target class for each observation in test fold
		trueMatch=0
		totalCmp=0
		
		for obs in testFoldData:
			totalCmp=totalCmp+1
			result= mdclassify(obs,tree)
			if obs[-1] == result.keys()[0]: #i,e Target class is predicted correctly
				trueMatch=trueMatch+1
		accuracy=trueMatch/float(totalCmp)
		print("Accuracy for Testing fold",f ,accuracy)
		accuracyList.append(accuracy)
		#print(accuracyList)
	finalAccuracy=sum(accuracyList)/float(10)
	print("Final Accuracy of " ,dataset,finalAccuracy)
	return finalAccuracy


