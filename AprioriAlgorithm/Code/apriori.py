
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
    



#Frequent itemset generation using apriori
def apriori(dataset,minsupport=0.4):
    import scan
    no_of_generated_itemset=0
    no_of_frequent_itemset=0
    "Generate candidate itemsets"
    c1=scan.create_itemset1(dataset) #k=1 (candidate itemset)
    no_of_generated_itemset=no_of_generated_itemset+len(c1)
    #print("c1 is",c1)
    dataset=map(set,dataset)
    l1,support_data=scan.scanDataset(dataset,c1,minsupport) #First support based pruning (k=1) for frequent itemset generation
    no_of_frequent_itemset=no_of_frequent_itemset+len(l1)
    #print("l1 is",l1)
    #print("l1 supk is",support_data)
    l=[l1]
    k=2
    while(len(l[k-2])>0):
        ck=aprioriGen2(l[k-2],k) #candidate generation step ()
        no_of_generated_itemset=no_of_generated_itemset+len(ck)

        #ck=aprioriGen1(l[k-2],l1)
        #print("ck is",ck)
        lk,supk=scan.scanDataset(dataset,ck,minsupport) #scanning dataset for support based pruning(frequent itemset generation)
        no_of_frequent_itemset=no_of_frequent_itemset + len(lk)
        #print("lk is",lk)
        #print("supk is",supk)
        support_data.update(supk)
        l.append(lk)
        k +=1

    return l ,support_data,no_of_generated_itemset,no_of_frequent_itemset    


 ###############Testing################################
#c1=[frozenset(['beer']), frozenset(['bread']), frozenset(['cola']), frozenset(['diaper']), frozenset(['egg']), frozenset(['milk'])]
#freq_sets=[frozenset(['beer', 'diaper']), frozenset(['diaper', 'bread']), frozenset(['milk', 'diaper']), frozenset(['milk', 'bread'])]
#x=aprioriGen1(freq_sets,c1)
'''
c1=[['beer'],['bread'],['cola'],['diaper'],['egg'],['milk']]
freq_sets=[['beer', 'diaper'],['diaper', 'bread'],['milk', 'diaper'], ['milk', 'bread']]
x=aprioriGen1(freq_sets,c1)
print(x)
'''