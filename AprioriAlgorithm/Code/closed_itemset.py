
def closed(frequent_set,support_data):
	closed_frequent_set=[]
	closed_frequent_item_count=0
	for i in range(len(frequent_set)):
		row=frequent_set[i]
		for item in  row:
			closed_frequent_item=True
			for next_item in frequent_set[i+1]:
				if(support_data[item]==support_data[next_item]):
					closed_frequent_item=False
			if(closed_frequent_item): 
				closed_frequent_set.append(item)
				closed_frequent_item_count +=1
	return closed_frequent_set,closed_frequent_item_count			
	
#########################################################Testing###################################################################
#s={frozenset({'D'}): 0.6666666666666666, frozenset({'C'}): 0.8333333333333334, frozenset({'A', 'C', 'E'}): 0.5, frozenset({'C', 'E'}): 0.8333333333333334, frozenset({'A', 'D'}): 0.5, frozenset({'A', 'D', 'E'}): 0.5, frozenset({'A', 'C'}): 0.5, frozenset({'D', 'E'}): 0.6666666666666666, frozenset({'A'}): 0.6666666666666666, frozenset({'E'}): 1.0, frozenset({'C', 'D'}): 0.5, frozenset({'A', 'E'}): 0.6666666666666666, frozenset({'C', 'D', 'E'}): 0.5}
#l=[[frozenset({'A'}), frozenset({'C'}), frozenset({'D'}), frozenset({'E'})], [frozenset({'D', 'E'}), frozenset({'C', 'D'}), frozenset({'A', 'C'}), frozenset({'A', 'D'}), frozenset({'A', 'E'}), frozenset({'C', 'E'})], [frozenset({'A', 'C', 'E'}), frozenset({'A', 'D', 'E'}), frozenset({'C', 'D', 'E'})], []]

#cs,csc=closed(l,s)
#print("closed set is",cs)
#print("closed set count is",csc)
