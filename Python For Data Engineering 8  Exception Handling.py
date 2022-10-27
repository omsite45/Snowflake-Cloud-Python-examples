try:
    a=int(input("Enter the first number "))
    b=int(input("Enter the first number "))
    c=a/b
    print("Try Block : ", c)
except Exception as e:
    print("Exception block error message:", e)
