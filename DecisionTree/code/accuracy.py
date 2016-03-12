

from classifier import *
import pickle
from buildtree import *
#from buildtree_pessimistic import *
from drawtree import * 
from sklearn.metrics import confusion_matrix
from prune import *
from sklearn.metrics import classification_report
from sklearn.preprocessing import label_binarize
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score



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
		#trainFoldData=pickle.load(open("./Data/iris/folds/trainFold_1.p","rb"))
		
		#making normal decision Tree on this trainFold
		tree=buildtree(trainFoldData)
		
		#pruning the tree using pessimistic error or mdl error
		#tree=prune(tree)

		#making pessimistic decision tree on this trainfold
		

		#print("Testing model for Testing fold",f)
		#Loading tesfold to check accuracy of the model
		testFoldData=pickle.load(open(foldPath + "testFold_"+str(f)+".p","rb"))
		
		# Checking target class for each observation in test fold
		trueMatch=0
		totalCmp=0
		actual=[]
		predictions=[]
		for obs in testFoldData:
			#print("obs is",obs)
			totalCmp=totalCmp+1
			result=mdclassify(obs,tree)
			#print("outcome is",result)
			#print (obs[-1],result)
			#if obs[-1] == result.keys()[0]: #i,e Target class is predicted correctly
			actual.append(obs[-1])
			predictions.append(result)
			if obs[-1] == result:
				trueMatch=trueMatch+1
		accuracy=trueMatch/float(totalCmp)
		print("Accuracy for Testing fold",f ,accuracy)
		accuracyList.append(accuracy)
		#print(accuracyList)
	finalAccuracy=sum(accuracyList)/float(10)
	print("Final Accuracy of " ,dataset,finalAccuracy)
	return finalAccuracy

############################Testing##############################
#accuracy10Fold(dataset="wine")
#data=pickle.load(open("./Data/iris/data.p","rb"))
#tree_pes=buildtree_pessimistic(rows=data[1:len(data)])
#classify([5.1,3.5,1.4,0.2],tree_pes)

def accuracyFold(dataset=None,f=None,path="./Data"):
	
	foldPath=path+"/" + dataset + "/folds/"
	trainFoldData=pickle.load(open(foldPath + "trainFold_"+str(f)+".p","rb"))

	#Training tree on pessimistic mode
	tree=buildtree(trainFoldData)
	
	testFoldData=pickle.load(open(foldPath + "testFold_"+str(f)+".p","rb"))
	
	trueMatch=0
	totalCmp=0
	actual=[]
	predicted=[]	
	for obs in testFoldData:
			totalCmp=totalCmp+1
			result=mdclassify(obs,tree)
			#print("outcome is",result)
			actual.append(obs[-1])
			predicted.append(result)

			if obs[-1] == result:
				trueMatch=trueMatch+1
	accuracy=trueMatch/float(totalCmp)
	createLabels(dataset=dataset)
	labels=pickle.load(open(path+"/"+dataset+"/labels.p","rb"))
	target_names = labels
	print(classification_report(actual, predicted ,target_names=target_names))
	'''
	pb,ab=binarize(actual,predicted)
	fpr, tpr, thresholds = roc_curve(pb, ab, pos_label=2)
	df = pd.DataFrame(dict(fpr=fpr, tpr=tpr))
	ggplot(df, aes(x='fpr', y='tpr')) +\
    geom_line() +\
    geom_abline(linetype='dashed')
    '''  
    
def createLabels(dataset=None):
	filepath="./Data"+ "/"+ dataset + "/" + "data.p"
	data=pickle.load(open(filepath,"rb"))
	labelDict={}
	for row in data[1:len(data)]:
		if row[len(row)-1] in labelDict:continue
		else: labelDict[row[len(row)-1]]=1
	#print(labelDict)
	pickle.dump(labelDict.keys(),open('./Data/'+dataset+'/labels.p',"wb"))
	#return labelDict.keys()  

def binarize(actual,predicted):	
	labelDict={}
	actual_b=[]
	predicted_b=[]
	i=0
	for c in actual:
		if c in labelDict:continue
		else:
			labelDict[c]=i
			i=i+1

	for  c in actual:
		actual_b.append(labelDict[c])


	for c in predicted: 
		predicted_b.append(labelDict[c])
	
	return (predicted_b,actual_b)	

