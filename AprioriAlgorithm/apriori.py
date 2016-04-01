
"F(k-1) X F(k-1) Method"
def aprioriGen(freq_sets,k): 
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

#Frequent itemset generation using apriori
def apriori(dataset,minsupport=0.5):
    import scan
    "Generate candidate itemsets"
    c1=scan.create_itemset1(dataset)
    d=map(set,dataset)
    l1,support_data=scan.scanDataset(d,c1,minsupport)
    l=[l1]
    k=2
    while(len(l[k-2])>0):
        ck=aprioriGen(l[k-2],k) #candidate generation step
        lk,supk=scan.scanDataset(d,ck,minsupport) #scanning dataset for support based pruning(frequent itemset generation)
        support_data.update(supk)
        l.append(lk)
        k +=1

    return l,support_data    