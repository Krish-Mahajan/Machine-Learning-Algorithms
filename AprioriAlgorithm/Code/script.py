
import scan
import apriori
import json
import load
import csv
import maximal_itemset
import closed_itemset
import mining 

#load.load(dataset="Groceries",filename="groceries.csv")
with open('./Data/Car/trans.json','r') as fp:
	d=json.load(fp)
l,support_data,c,f=apriori.apriori(d,minsupport=0.3)
#print("l is",l)
#print("support is",support_data)


'''
writer = csv.writer(open('./Data/nursery/support_0.3_f1.csv', 'wb'))
for key, value in support_data.items():
   	writer.writerow([list(key)[:], value])
'''
#print("generated itemset is",c)
#print("frequent itemset",f)
#s,sc=maximal_itemset.maximal(l)
#print("# of maximal frequent itemset",sc)
#c,cc=closed_itemset.closed(l,support_data)
#print("# of closed frequent itemset is",cc)
#print("support data is",support_data)
#mining.generateRules(l,support_data)
rules,noofrules=mining.generateRules(l,support_data,min_confidence=0.25)
#rules,noofrules=mining.generateRules(l,support_data,min_confidence=0.5)
print("rules generated",noofrules)
print("rules pruned",len(rules))

writer = csv.writer(open('./Data/Car/rules_0.3_0.25.csv', 'wb'))
for rule in rules:
   	writer.writerow(rule)
