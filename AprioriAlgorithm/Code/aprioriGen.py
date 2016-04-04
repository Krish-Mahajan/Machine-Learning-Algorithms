


"F(k-1) X F(k-1) Method"
def aprioriGen2(freq_sets,k): 
    "Generate k+1 len itemsets from k len candidate itemsets sets"
    retList=[]
    lenLk=len(freq_sets)
    #print("Lk is",lenLk)
    for i in range(lenLk):
        for j in range(i+1,lenLk):
            l1=list(freq_sets[i])[:k-2]
            #print("l1 is",l1)
            l2=list(freq_sets[j])[:k-2]
            #print("l2 is",l2)
            l1.sort()
            l2.sort()
            if l1==l2:
                retList.append(freq_sets[i]|freq_sets[j])
    return retList        


"F_1 X F(k-1) Method"
def aprioriGen1(freq_sets,c_1):
    retList=[]
    for i in range(len(freq_sets)):
        l1=list(freq_sets[i])[:]
        l1.sort()
        #print("l1 is" ,l1)
        for j in range(len(c_1)):
            l2=list(c_1[j])[0]
            #print("l2 is",l2)
            if(all(l2>k for k in l1)):
                retList.append(((freq_sets[i])|(c_1[j])))
                #print("retlist is",retList)
    return retList          
    