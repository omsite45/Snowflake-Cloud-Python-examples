n=str(input("Enter the string :"))

k=int(input("Enter the position you want to change the string :"))

rep= str(input("Enter the replace string "))

print("String :", n,"position character :", k," Will be replaced by ", rep)
i=0
list_new=[]
for i in range(len(n )):
    list_new.append(n[i])
#print(list_new)
for k1 in range(len(list_new)):
    if(k1==k):
        list_new[k1]=rep
    print(list_new[k1], end="")
    
