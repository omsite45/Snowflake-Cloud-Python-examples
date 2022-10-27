i=int(input("Enter the lower range "))
n=int(input("Enter the higher range "))
Sum=0

while(i<n):
    if (i%2==0):
        print( i)
        Sum=Sum+1
        i+=1
    else:
        print()
print("Sum ",Sum)
