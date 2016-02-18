


import csv
#Function to read the raw data file in pickle format
def read(dataset=None,path="./Data",filename=None ,colname=None,sep=","):
	filepath=path+ "/"+ dataset + "/" + filename
	
	f=open(filepath,'rb')
	my_data=[line.rstrip().split(',') for line in f]
	
	#converting numerical outcome into float
	for i in range(0,len(my_data)):
		for j in range(0,len(my_data[i])-1):
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
colname=['variance','skewness','curtosis','entropy','class']
read(dataset="banknote",filename="banknote.data",colname=colname)
validation(dataset="banknote")

