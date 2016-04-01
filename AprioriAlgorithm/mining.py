

def generateRules(l,support_data,min_confidence=0.7):
	"""Create the association rules
	L:list of frequent item sets
	support_data:support data for those itemsets
	min_confidence:minimum confidence threshold
	"""

	rules=[]
	for i in range(1,len(l)):
		for freqset in l[i]:
			h1=[frozenset([item]) for item in freqset]
			print("freqset",freqset,"H1",h1)
			if(i>1):
				rules_from_conseq(freqset,h1,support_data,rules,min_confidence)
			else:
				calc_confidence(freqset,h1,support_data,rules,min_confidence)
	return rules
	
def calc_confidence(freqset,h,support_data,rules,min_confidence):
	"Evaluate the rule generated"
	pruned_H=[]
	for conseq in h:
		conf=support_data[freqset]/support_data[freqset-conseq]
		if conf>=min_confidence:
			rules.append((freqset-conseq,conseq,conf))
			pruned_H.append(conseq)
	return pruned_H
     

def rules_from_conseq(freqset,h,support_data,rules,min_confidence=0.7):
	"Generate a set of candidate rules"
	import apriori
	m=len(h[0])
	if(len(freqset) > (m+1)):
		Hmp1=apriori.aprioriGen(h,m+1)
		Hmp1=calc_confidence(freqset,Hmp1,support_data,rules,min_confidence)
		if len(Hmp1) > 1:
			rules_from_conseq(freqset,Hmp1,support_data,rules,min_confidence)

 
				


