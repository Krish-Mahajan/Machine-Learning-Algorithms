#!/usr/bin/python
# -*- coding: utf-8 -*-

#reading raw files and inserting content into dictionary
import json
import os
###Storing data to json dictionary format
def loadData(path='./Data/10M'):
	movies={}
	#newpath='./DataStore'
	#os.makedirs(newpath)

	###Making Master list of dictionary

	for line in open(path +'/movies.csv',encoding="utf8"):
		(id,title)=line.split(',')[0:2]
		movies[id]=title
	
	with open('./DataStore/movies_10M.json','w') as fp:
		json.dump(movies,fp)
	
    
    ##For each fold making 
	'''
	for i in [1,2,3,4,5]: 
		prefsTrain={}
		for line in open(path +'/u'+str(i)+'.base'):
			(user,movieid,rating)=line.split('::')[0:3]
			prefsTrain.setdefault(user,{})
			#prefsTrain[user][movies[movieid]]=int(rating)
			prefsTrain[user][movieid]=round(float(rating),2)

		with open('./Datastore/prefsTrain'+str(i)+'.json','w') as fp:
			json.dump(prefsTrain,fp)
    
		prefsTest={}
		for line in open(path +'/u'+str(i)+'.test'):
			(user,movieid,rating)=line.split('::')[0:3]
			prefsTest.setdefault(user,{})
			prefsTest[user][movieid]=round(float(rating),2)

		with open('./Datastore/prefsTest'+str(i)+'.json','w') as fp:
			json.dump(prefsTest,fp)
	'''		
	'''
def loadDataNew(path='./Data/100K/ml-100k/'):
		prefsTrain={}
		
		for line in open(path+'u.user'):
			(user,age,gender,occupation)=line.split(',')[0:4]
			prefsTrain.setdefault(user,{})
			prefsTrain[user]['age']=int(age)
			prefsTrain[user]['gender']=gender
			prefsTrain[user]['occupation']=occupation
			prefsTrain[user]['movies']={}

		for line in open(path+'u1.base'):
			(user,movieid,rating)=line.split('\t')[0:3]
			prefsTrain[user]['movies'][movieid]=int(rating)

		with open('./Datastore/prefsTrain_demographic.json','w') as fp:
			json.dump(prefsTrain,fp)	

    ''' 	


#reading the json format
def readPrefs(pref):
	with open(pref,'r') as fp:
	     data=json.load(fp)
	return data 

      
    

################################Testing######################################################
#x=loadData()
#writeData(x)
#x=loadDataNew()