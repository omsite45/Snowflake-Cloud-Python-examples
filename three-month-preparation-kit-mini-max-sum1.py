def min_max():
    arr=[]
    s_arr=[]
    a=0
    a1=1
    a2=2
    a3=3
    a4=4
    i=0
    k=0
    Sum=0


    for i in range(5):
        arr.append(int(input()))
    print(arr)
    while(a<=len(arr)):

        for k in range(len(arr)):
            if(arr[i]!=arr[a]):
                Sum+=arr[i]
                s_arr.append(Sum)
    a+=1
    print("Sum",a,"=",Sum)
        
    print(Sum)
    print((s_arr))
min_max()
