
import scan
import apriori
import json
import load
import csv

#load.load(dataset="Groceries",filename="groceries.csv")
with open('./Data/Car/trans.json','r') as fp:
	d=json.load(fp)
l,support_data,c,f=apriori.apriori(d,minsupport=0.3)
print("l is",l)
print("support is",support_data)

writer = csv.writer(open('./Data/Car/support_0.3.csv', 'wb'))
for key, value in support_data.items():
   	writer.writerow([list(key)[:], value])
print("generated itemset is",c)
print("frequent itemset",f)
#print("support data is",support_data)
#mining.generateRules(l,support_data)

