

import pickle


fobj = open("./Data/iris/iris.data", "r")
my_data=[line.split(',') for line in fobj]
#print(my_data)
for i in range(0,len(my_data)):
	for j in range(0,len(my_data[i])-1):
		my_data[i][j]=float(my_data[i][j])
		
colname=[['sepal_length','sepal_width','petal_length','petal_width']]
my_data=colname+my_data
pickle.dump(my_data,open("./Data/iris/data.p","wb"))
