


#classifying new observations

def classify(observation,tree):
	if tree.results!=None:
		return tree.results
	else:
		v=observation[tree.col]
		branch=None
		if isinstance(v,int) or isinstance(v,float):
			if v>=tree.value : branch=tree.tb
			else: branch=tree.fb

		else:
			if v==tree.value: branch=tree.tb
			else: branch=tree.fb
	return classify(observation,branch)		
			

