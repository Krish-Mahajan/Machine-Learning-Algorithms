

import aprioriGen
no_of_generated_rules=0
#c1=[]
def generateRules(l,support_data,min_lift=0.7):
	"""Create the association rules
	L:list of frequent item sets
	support_data:support data for those itemsets
	min_confidence:minimum confidence threshold
	"""

	rules=[]
	
	#global c1
	#c1=l[0]
	for i in range(1,len(l)-1):
		for freqset in l[i]:
			h1=[frozenset([item]) for item in freqset]
			#print("freqset",freqset,"H1",h1)
			if(i>1):
				rules_from_conseq(freqset,h1,support_data,rules,min_lift)
			else:
				calc_confidence(freqset,h1,support_data,rules,min_lift)
	return rules, no_of_generated_rules
	
def calc_confidence(freqset,h,support_data,rules,min_lift):
	"Evaluate the rule generated"
	global no_of_generated_rules
	pruned_H=[]
	for conseq in h:
		no_of_generated_rules +=1
		#print(no_of_generated_rules)
		lift=support_data[freqset]/(support_data[freqset-conseq]*support_data[conseq])
		if lift>=min_lift:
			#print(freqset - conseq, '--->', conseq, 'conf:', conf)
			rules.append((freqset-conseq,conseq,lift))
			pruned_H.append(conseq)
	return pruned_H
     

def rules_from_conseq(freqset,h,support_data,rules,min_lift):
	"Generate a set of candidate rules"
	import apriori
	m=len(h[0])
	if(len(freqset) > (m+1)):
		Hmp1=aprioriGen.aprioriGen2(h,m+1)
		
		#Hmp1=aprioriGen.aprioriGen1(h,c1)
		Hmp1=calc_confidence(freqset,Hmp1,support_data,rules,min_lift)
		if len(Hmp1) > 1:
			rules_from_conseq(freqset,Hmp1,support_data,rules,min_lift)

 
###########################################################Testing################################################################3



