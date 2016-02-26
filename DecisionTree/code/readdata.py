


import csv
import pickle
#Function to read the raw data file in pickle format
def read(dataset=None,path="./Data",filename=None ,colname=None,sep=","):
	filepath=path+ "/"+ dataset + "/" + filename
	
	f=open(filepath,'rb')
	my_data=[line.rstrip().split(',') for line in f]
	
	#converting numerical outcome into float
	for i in range(0,len(my_data)):
		for j in range(0,len(my_data[i])-1):
			if isinstance(my_data[i][j],int) or isinstance(my_data[i][j],float):
				my_data[i][j]=float(my_data[i][j])
			
	colname=[colname]
	my_data=colname+my_data
	
	writepath=path+ "/"+ dataset + "/data.csv" 
	
	#Writing in CSV
	with open(writepath, 'wb') as fp:
			a=csv.writer(fp)
			a.writerows(my_data)
	
	#writing in pickle
	writepath=path+ "/"+ dataset + "/data.p" 
	pickle.dump(my_data,open(writepath,"wb"))

######################Testing###############################

#Iris
'''
colname=['sepal_length','sepal_width','petal_length','petal_width','class']
read(path="./Data/iris/iris.data",colname=colname,sep=",")
'''

#wine
'''
colname=[ 'Alcohol','Malic acid','Ash','Alcalinity of ash','Magnesium','Total Phenols','Flavanoids','Non Flavanoid Phenols','Proanthocyanins','color intensity','Hue','OD280','Proline','class']
read(dataset="wine",filename="wine.data",colname=colname,sep=",")
'''

#balance scale
'''
colname=['LeftWeight','LeftDistance','RightWeight','RightDistance']
read(dataset="balancescale",filename="balancescale.data",colname=colname)
validation(dataset="balancescale")
'''

#banknote:
'''
colname=['variance','skewness','curtosis','entropy','class']
read(dataset="banknote",filename="banknote.data",colname=colname)
validation(dataset="banknote")
'''

#Blood
'''
colname=['Recency','Frequecy','ccc_blood','times','donated']
read(dataset="blood",filename="transfusion.data",colname=colname)
import createFolds
createFolds.createFold(dataset="blood")
import script
script.printtree(dataset="blood")
accuracy.accuracy10Fold(dataset="blood")
'''

#breast cancer
'''
colname=["code_number","thickness","cell_size","cell_shape","Mar_Adhesion","single_cell_size","Nuclie","Chromatin","Nucleoli","Mitoses","class"]
readdata.read(dataset="breastcancer",filename="breastcancer.data",colname=colname)
'''

#car
'''
colname=["buying","maint","doors","persons","lug_boot","safety"]
readdata.read(dataset="car",filename="car.data",colname=colname)
'''

#customer
'''
colname=["region","Fresh","milk","grocery","Frozen","detergents","Deli","Channel"]
readdata.read(dataset="customer",filename="customer.data",colname=colname)
'''

#haberman
'''
colname=["Age","Year","positive_nodes","status"]
readdata.read(dataset="haberman",filename="haberman.data",colname=colname)
'''

#yeast
'''
colname=['name','mcg','gvh','alm','mit','erl','pox','vac','nuc','class']
readdata.read(dataset="yeast",filename="yeast.data",colname=colname)
'''