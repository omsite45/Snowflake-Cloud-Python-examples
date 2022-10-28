def dynamic_input_list():
    lst = []
    n=int(input("Enter the number of elements you wanna to enter in the list "))
    for i in range(1,n+1):
        print("Enter the ",i,"element ", end="")
        ele=input()
        lst.append(ele)
        n-=1
    print (lst)

dynamic_input_list()
