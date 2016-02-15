
#import main 

#calculation of impurity	
def giniimpurity(rows):
	total=len(rows)
	from main import uniquecounts
	counts=uniquecounts(rows)
	imp=0
	for k1 in counts:
		p1=float(counts[k1])/total
		for k2 in counts:
			if k1==k2:continue
			p2=float(counts[k2])/total
			imp=imp+p1*p2
    
	return imp

#calculation of entropy

def entropy(rows):
	from math import log
	from main import uniquecounts
	log2=lambda x:log(x)/log(2)
	results=uniquecounts(rows)	
	ent=0
	for r in results.keys():
		p=float(results[r])/len(rows)
		ent=ent-p*log2(p)
	return ent	