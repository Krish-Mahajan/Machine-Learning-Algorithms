
import csv
import json
def load(dataset=None,path="./Data",filename=None,sep=","):
	filepath=path + "/" + dataset + "/" + filename 
    
	with open(filepath,'r') as f:
		reader=csv.reader(f)
		ll=[]
		for row in reader:
			l=[]
			for i in range(1,len(row)):
				if(row[i] !=''):
					l.append(row[i])
			ll.append(l)		
		#print(ll[0:5])
	with open(path + "/" + dataset + "/"+'trans.json','w') as fp:
		json.dump(ll,fp)
	
	#only if Binarize Data	
	'''
	trans=[]		
	for i in range(1,len(ll)):
		t=[]
		for j in range(len(ll[0])):
			if(ll[i][j]=='1'):
				t.append(ll[0][j])
		trans.append(t)
	print(trans[1:5])	
	with open(path + "/" + dataset + "/"+'trans.json','w') as fp:
		json.dump(trans,fp)			
	'''	
#########################Testing###########################
#load(dataset="Groceries",filename="groceries.csv")