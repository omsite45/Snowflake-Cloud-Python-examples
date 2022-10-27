n= int(input("Enter the number"))
x=n
Sum=''
y=0
while(n>0):
    j=0
    Sum=Sum+str(n%10)
    
    y=int(Sum)
    n=n//10
print("Sum", y)

if(x==y):
    print("palindronme Number ")
else:
    print("NOT Palindrome Number")
    print(y)

    
    
