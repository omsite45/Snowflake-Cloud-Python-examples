i= int(input("Enter Number :"))
rev=0
rev1=""
while(i>0):
    rev=(rev*10)+(i%10)
    rev1=rev1+str(rev)
    i=i//10
    
    
print("rev ", rev)
