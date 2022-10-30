

def dynamic_list():
    import ast
    lst=[]
    n=int(input("Enter the number of elements you want to enter :"))
    for i in range(1,n+1):
        
        
                   print("Enter the element  ", i," " , end="")
                   ele=str(input())
                   lst.append(ele)
    a=0               
    for m in range(len(lst)):
          fre=(lst.count(lst[m]))
          a+=1
    print("The list is ", lst)
    l=input("Enter the element you want to search :")
    for k in range(len(lst)):
        if(l==lst[k]):
            i=lst.count(l)
            print("Freq of ",l," is ", i)
            print(lst)
            

        else:
         print(l, " does NOT exist in the list ")
         break

        
            
            
            
    
    fre=[] 
    

dynamic_list()
    
