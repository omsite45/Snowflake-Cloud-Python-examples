n= int(input("Enter the number "))
x=0
y=1
z=0
while(n>0):
    while(z<=n):
        x=y
        y=z
        print(z)
        z=x+y
        
