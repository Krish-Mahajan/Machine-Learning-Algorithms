


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

#classify observation if missing data
def mdclassify(observation,tree):
	if tree.results!=None:
		return tree.results
	else:
		v=observation[tree.col]
		if v==None:
			tr,fr=mdclassify(observation,tree.tb),mdclassify(observation,tree.fb)
			tcount=sum(tr.values())
			fcount=sum(fr.values())
			tw=float((tcount)/(tcount+fcount))
			fw=float((fcount)/(tcount+fcount))
			result={}
			for k,v in tr.items(): result[k]=v*tw
			for k,v in fr.items(): result[k]=result.setdefault(k,0)+v*fw
			return result
		else:
			if isinstance(v,int) or isinstance(v,float):
				if v>=tree.value: branch=tree.tb
				else: branch=tree.fb
			else:
				if v==tree.value: branch=tree.tb
				else: branch=tree.fb
			return mdclassify(observation,branch)


def mdclassify_new(observation,tree):
  if tree.results!=None:
    return tree.results
  else:
    v=observation[tree.col]
    if v==None:
      tr,fr=mdclassify(observation,tree.tb),mdclassify(observation,tree.fb)
      tcount=sum(tr.values())
      fcount=sum(fr.values())
      tw=float(tcount)/(tcount+fcount)
      fw=float(fcount)/(tcount+fcount)
      result={}
      for k,v in tr.items(): result[k]=v*tw
      for k,v in fr.items(): result[k]=v*fw      
      return result
    else:
      if isinstance(v,int) or isinstance(v,float):
        if v>=tree.value: branch=tree.tb
        else: branch=tree.fb
      else:
        if v==tree.value: branch=tree.tb
        else: branch=tree.fb
      return mdclassify(observation,branch)			

					
			
		
			

