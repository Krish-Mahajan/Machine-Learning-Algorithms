
import apriori
import mining 
import json

def create_itemset1(dataset):
	"create a list of candidate of size 1"
	c1=[]
	for trans in dataset:
		for item in trans:
			if  not [item] in c1:
				c1.append([item])

	c1.sort()
	
	return map(frozenset,c1)
	#return c1


def scanDataset(dataset,candidates,min_support):
	"Return candidate itemset that meets a minimum suport"
	candidate_support={}
	#print("candidates are",candidates)
	#calculating support count  of each candidate itemset by scanning dataset
	for trans in dataset:
		for can in candidates:
			if  can.issubset(trans):
				candidate_support.setdefault(can,0)
				candidate_support[can] +=1

	#calculating support count of each itemset			
	num_items=float(len(dataset))			
	retlist=[]
	support_data={}
	for candidate in candidate_support:
		support=candidate_support[candidate]/num_items
		if support >= min_support:
			retlist.insert(0,candidate)
			support_data[candidate]=support
		
	return retlist,support_data		


################################################################

#d=[[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]

'''
d=[      ['bread','milk'],
		 ['bread','diaper','beer','egg'],
		 ['milk','diaper','beer','cola'],
		 ['bread','milk','diaper','beer'],
		 ['bread','milk','diaper','cola']
 ]

'''
'''
d=[      ['A','B','C','E'],
		 ['A','C','D','E'],
		 ['B','C','E'],
		 ['A','C','D','E'],
		 ['C','D','E'],
		 ['A','D','E']
 	]
'''
#c1=create_itemset1(d)
#print(c1)
#d=map(set,d)
#print(d)
#L1,support_data=scanDataset(d,c1,0.5)
#print(L1)
#print(support_data)
#print(apriori.aprioriGen(L1,2))
'''
with open('./Data/Groceries/trans_1.json','r') as fp:
	d=json.load(fp)
'''
#l,support_data,c,f=apriori.apriori(d,minsupport=0.5)
#print("l is",l)
#print("support is",support_data)
#print("generated itemset is",c)
#print("frequent itemset",f)
#print("support data is",support_data)
#rules,noofrules=mining.generateRules(l,support_data,min_confidence=0.5)
#print("rules generated",noofrules)
#print("rules pruned",len(rules))

