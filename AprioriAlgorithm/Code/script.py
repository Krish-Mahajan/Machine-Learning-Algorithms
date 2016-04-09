
import scan
import apriori
import json
import load
import csv
import maximal_itemset
import closed_itemset
import mining 
import mining_lift

#load.load(dataset="Groceries",filename="groceries.csv")
with open('./Data/Groceries/trans.json','r') as fp:
	d=json.load(fp)
l,support_data,c,f=apriori.apriori(d,minsupport=0.1)
#print("l is",l)
#print("support is",support_data)


'''
writer = csv.writer(open('./Data/nursery/support_0.3_f1.csv', 'wb'))
for key, value in support_data.items():
   	writer.writerow([list(key)[:], value])
'''


'''
rules,noofrules=mining_lift.generateRules(l,support_data,min_lift=0.85)

print("rules generated",noofrules)
print("rules pruned",len(rules))
'''
'''
writer = csv.writer(open('./Data/Groceries/rules_0.01_0.9.csv', 'wb'))
for rule in rules:
   	writer.writerow(rule)
'''

'''
writer = csv.writer(open('./Data/Groceries/lift_rules_0.1_0.85.csv', 'wb'))
for rule in rules:
   	writer.writerow(rule) 
'''   	