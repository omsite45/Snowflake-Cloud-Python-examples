n=int(input("Enter the number of elements to input :"))
i=0
lst=[]
for i in range(1, n+1):
    x=input("Enter the element ")
    lst.append(x)
print(lst)
lst.sort()
print("Sorted list is  :",lst )

