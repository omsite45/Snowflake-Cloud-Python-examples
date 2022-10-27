

n=int(input("Enter the 4 digit number : "))
x=n
Sum=0
while(n>0):
    if(len(str(x)))==4:
        j=0
        j=j+n%10
        Sum=Sum+(j*j*j*j)
        n=n//10
        
    else:
        print("Enter number whose length is 4  only NOT less")
        break
if(len(str(x)))==4:
    if(Sum==x):
        print("Armstrong Numnber ")
    else:
        print("NOT Armstroing")
