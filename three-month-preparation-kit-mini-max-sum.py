
arr=[]

a=0
a1=1
a2=2
a3=3
a4=4
i=0
Sum=0
Sum1=0
Sum2=0
Sum3=0
Sum4=0

for i in range(5):
    arr.append(int(input()))

for i in range(5):
    if(arr[i]!=arr[a]):
        
        Sum+=arr[i]

    if(arr[i]!=arr[a1]):
        
        Sum1+=arr[i]

    if(arr[i]!=arr[a2]):
        
        Sum2+=arr[i]

    if(arr[i]!=arr[a3]):
        
        Sum3+=arr[i]
    if(arr[i]!=arr[a4]):
        
        Sum4+=arr[i]
print(min(Sum,Sum1,Sum2,Sum3,Sum4),max(Sum,Sum1,Sum2,Sum3,Sum4) , end="")
