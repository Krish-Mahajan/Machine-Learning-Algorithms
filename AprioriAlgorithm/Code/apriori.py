
import aprioriGen


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
        #ck=aprioriGen.aprioriGen2(l[k-2],k) #candidate generation step ()
        ck=aprioriGen.aprioriGen1(l[k-2],l1)
        no_of_generated_itemset=no_of_generated_itemset+len(ck)
        #print("ck is",ck)
        lk,supk=scan.scanDataset(dataset,ck,minsupport) #scanning dataset for support based pruning(frequent itemset generation)
        no_of_frequent_itemset=no_of_frequent_itemset + len(lk)
        #print("l_",k,"is",lk)
        #print("********************************************************")
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