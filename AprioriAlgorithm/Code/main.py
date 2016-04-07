
import scan
import apriori
import json
import load
import csv
import maximal_itemset
import closed_itemset
import mining 
import mining_lift


def main_frequencyset(dataset=None,filename=None,path="./Data",sep="," ,minsupport=0.1,min_factor=0.50):
	
	#reading binarize file(changing binarize file into transaction)
	filepath=path + "/" + dataset + "/" + filename 
	load.load(dataset=dataset,filename=filename) 
	
	#reading binarized transactions
	transpath=path + "/" + dataset + "/" + "trans.json"
	with open(transpath,'r') as fp:
		d=json.load(fp)
	
	#running apriori with minsupport to get frequency sets
	l,support_data,c,f=apriori.apriori(d,minsupport=0.1)
	print("l is",l)
	print("support is",support_data)


	#printing frequency set with support 
	filepath=path + "/" + dataset + "/support_" + str(minsupport) + ".csv"
	writer = csv.writer(open(filepath, 'wb'))
	for key, value in support_data.items():
	   	writer.writerow([list(key)[:], value])
	
    
	#generating maximal and closed itemset
	print("# of candidate itemset is",c)	
	print("# of frequent itemset is",f)   	
	s,sc=maximal_itemset.maximal(l)
	print("# of maximal frequent itemset",sc)
	c,cc=closed_itemset.closed(l,support_data)
	print("# of closed frequent itemset is",cc)
	#print("support data is",support_data)
	#mining.generateRules(l,support_data)

	#generating rules   	
	#rules,noofrules=mining_lift.generateRules(l,support_data,min_factor=0.85)
	rules,noofrules=mining.generateRules(l,support_data,min_factor=0.50)


	print("rules generated",noofrules)
	print("rules pruned",len(rules))

	#writing rules with confindence measure
	filepath=path + "/" + dataset + "/rules_" + str(minsupport) + "_" + str(min_confidence) + ".csv"
	writer = csv.writer(open(filepath, 'wb'))
	for rule in rules:
	   	writer.writerow(rule)
	


#main_frequencyset(dataset="Car",filename="binarize_car.csv")
#main_frequencyset(dataset="nursery",filename="binarize_nursery.csv")	