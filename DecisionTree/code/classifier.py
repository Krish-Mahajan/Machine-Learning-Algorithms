
import operator


'''
def classify(observation,tree):
    
    if tree.results!=None:
        #print(tree.results)
        return max(tree.results,key=lambda i:tree.results[i])
        
        
    else:
        #print("here")
        v=observation[tree.col]
        branch=None
        if isinstance(v,int) or isinstance(v,float):
            if v>=tree.value: branch=tree.tb
            else: branch=tree.fb
        else:
            if v==tree.value: branch=tree.tb
            else: branch=tree.fb
        return classify(observation,branch)
'''

#max(stats.iteritems(), key=operator.itemgetter(1))[0]
def mdclassify(observation,tree):
    if tree.results!=None:
        return max(tree.results,key=lambda i:tree.results[i])
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
            for k,v in fr.items(): 
                if (k in result): result[k]=result[k] + v*fw
                else: result[k]=result.setdefault(k,0) + v*fw
            return result
        else:
            if isinstance(v,int) or isinstance(v,float):
                if v>=tree.value: branch=tree.tb
                else: branch=tree.fb
            else:
                if v==tree.value: branch=tree.tb
                else: branch=tree.fb
        return mdclassify(observation,branch)

'''
def classify_pessimistic(observation,tree):
    
    if tree.col==None:
       return max(tree.results,key=lambda i:tree.results[i]) 
    else:
        v=observation[tree.col]
        print(v)
        branch=None
        if isinstance(v,int) or isinstance(v,float):
                if v>=tree.value: branch=tree.tb
                else: branch=tree.fb
        else:
                if v==tree.value: branch=tree.tb
                else: branch=tree.fb
        return classify_pessimistic(observation,branch)
        
    
    if tree.tb==None and tree.fb==None:
        print(tree.results)
        return max(tree.results,key=lambda i:tree.results[i])
        
        
'''        