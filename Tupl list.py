import itertools
n=(["vanilla","chocolate"],["chocolate sauce"])
newlist=[]

for x in  range(len(n)):
    if x%2==0:
        list1=n[x]
        list2=n[x+1]
        print(list1, list2)
        for z in range(len(list1)):
            list1.append(list2)
print(list1)
