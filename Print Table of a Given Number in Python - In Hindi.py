n= int(input("Enter the number  you want to print the table of "))
x=10
table=1
while(n>0):
    for i in range(1,x+1):
        table= n*i
        print(n, "*",i,"=", table)
    if(i==10):
        break
        
    
    

