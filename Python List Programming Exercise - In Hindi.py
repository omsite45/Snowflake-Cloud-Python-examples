def dynamic_list():
    import ast
    lst=[]
    n=int(input("Enter the number of elements you want to enter :"))
    for i in range(1,n+1):
                   print("Enter the element  ", i," " , end="")
                   ele=str(input())
                   lst.append(ele)
    print(lst)
dynamic_list()
    
