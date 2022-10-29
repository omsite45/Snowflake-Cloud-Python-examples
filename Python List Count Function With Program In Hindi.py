
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
          print("Freq of ",lst[m]," is ", fre)
    print(lst)
    
    fre=[] 
    

dynamic_list()
    
