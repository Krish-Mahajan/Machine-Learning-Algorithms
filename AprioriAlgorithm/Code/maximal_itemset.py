


def maximal(frequent_set):
	maximal_frequent_set=[]
	maximal_frequent_item_count=0
	for i in range(len(frequent_set)):
		row=frequent_set[i]
		for item in  row:
			maximal_frequent_item=True
			for next_item in frequent_set[i+1]:
				if(item.issubset(next_item)):
					maximal_frequent_item=False
			if(maximal_frequent_item): 
				maximal_frequent_set.append(item)
				maximal_frequent_item_count +=1
	return maximal_frequent_set,maximal_frequent_item_count			
					
#########################Count##############################3
#l=l=[[frozenset(['A']), frozenset(['C']), frozenset(['D']), frozenset(['E'])], [frozenset(['E', 'D']), frozenset(['C', 'D']), frozenset(['A', 'C']), frozenset(['A', 'D']), frozenset(['A', 'E']), frozenset(['C', 'E'])], [frozenset(['A', 'C', 'E']), frozenset(['A', 'E', 'D']), frozenset(['C', 'E', 'D'])], []]
#s,sc=maximal(l)
#print(s)
#print(sc)