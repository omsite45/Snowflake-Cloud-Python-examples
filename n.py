i=0
arr = [1, 2 ,3 ,-1, -2 ,-3 ,0 ,0]
pos=0
neg=0
zer=0
n=6

for i in range(len(arr)):
    if(arr[i]) >0:
        pos+=1
    elif arr[i] <0:
        neg+=1
    else:
        zer+=1
print("{:.6f}".format(pos/len(arr)))
print("{:.6f}".format(neg/len(arr)))
print("{:.6f}".format(zer/len(arr)))

