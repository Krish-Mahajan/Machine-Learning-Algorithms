
from sklearn.cross_validation import StratifiedKFold
from sklearn.cross_validation import StratifiedShuffleSplit
import pickle
import csv


'''
Function to create 10  stratified Folds
'''
def createFold(dataset=None,path="./Data"):

	#Reading the data (which was stored in list of list format)
	filepath=path+ "/"+ dataset + "/" + "data.p"
	'''
	fobj = open(filepath, "rb")
	my_data=[line.split(',') for line in fobj]
    '''

	data=pickle.load(open(filepath,"rb"))

	my_data=data[1:len(data)]

	#Extracting class variable to see thier distribution
	c=[row[len(row)-1] for row in my_data]
	label=[]
	labeldict={}
	i=0
	for target in c:
		if target in labeldict:continue
		else:
			labeldict[target]=i
			i=i+1

	#print(labeldict)  
	for target in c:
		label.append(labeldict[target])

	#print(label)

	#Performing Strattified K fold
	skf = StratifiedKFold(label, 10)
	

	#Performing Stratified Kfold shuffle split
	'''
	skf=StratifiedShuffleSplit(label,10,test_size=0.25)
	'''
	


	#Writing all Fold of testing+training sets[textfile or pickle or csv]    
	i=1
	for train,test in skf:
		#print("fold no", i)

	    #Training Data
		mydata_train=[]
		for row in train:
			mydata_train.append(my_data[row])
        
        ##Writing Training Folds in csv & pickle
		with open('./Data/'+ dataset+'/folds/trainFold_'+str(i) + '.csv','wb') as fp:
			a=csv.writer(fp)
			a.writerows(mydata_train)
		pickle.dump(mydata_train,open('./Data/'+ dataset+'/folds/trainFold_'+str(i) + '.p',"wb"))	
		    
	    #Testing Data
		mydata_test=[]
		for row in test:
			mydata_test.append(my_data[row])
	    
	    ##Writing Testing Folds in csv & pickle
		with open('./Data/'+ dataset+'/folds/testFold_'+str(i)+'.csv', 'wb') as fp:
			a=csv.writer(fp)
			a.writerows(mydata_test)
		pickle.dump(mydata_test,open('./Data/'+ dataset+'/folds/testFold_'+str(i)+'.p',"wb"))    

		i=i+1	
