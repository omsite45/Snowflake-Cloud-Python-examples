import ast
def dynamic_input_list():
    lst1 = []
    lst2 = []
    n=int(input("Enter the number of elements you wanna to enter in the list 1 "))
    n1=int(input("Enter the number of elements you wanna to enter in the list 2 "))
    s=1
    for i in range(1,n+1):
            print("Enter the ",i,"element ", end="")
            ele=str(input())
            lst1.append(ele)
    print (lst1)
    for i in range(1,n1+1):
            print("Enter the ",i,"element ", end="")
            ele=str(input())
            lst2.append(ele)
    print (lst2)
    
    
    
dynamic_input_list()
