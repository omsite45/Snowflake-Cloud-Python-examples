n= int(input("Enter the number "))

Count=0
if(n>0):
    for i in range(1,n+1):
        print(i)
        if(n%i==0):
            Count+=1
    if(Count==2):
        print("primt Number")
    else:
        print("Composite Number")
else:
    print("Enter greater than zero")
    
        
    

        
            
