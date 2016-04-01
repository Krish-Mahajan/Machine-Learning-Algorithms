
import apriori
import mining 

def create_itemset1(dataset):
	"create a list of candidate of size 1"
	i1=[]
	for trans in dataset:
		for item in trans:
			if  not [item] in i1:
				i1.append([item])

	i1.sort()
	
	return map(frozenset,i1)


def scanDataset(dataset,candidates,min_support):
	"Return candidate itemset that meets a minimum suport"
	candidate_support={}

	#calculating support count  of each candidate itemset by scanning dataset
	for trans in dataset:
		for can in candidates:
			if can.issubset(trans):
				candidate_support.setdefault(can,0)
				candidate_support[can]	+=1

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
dataset=[[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]

c1=create_itemset1(dataset)
#print(c1)
d=map(set,dataset)
#print(d)
L1,support_data=scanDataset(d,c1,0.5)
#print(L1)
#print(support_data)
#print(apriori.aprioriGen(L1,2))
l,support_data=apriori.apriori(dataset)
#print("l is",l)
#print("support data is",support_data)
mining.generateRules(l,support_data)

