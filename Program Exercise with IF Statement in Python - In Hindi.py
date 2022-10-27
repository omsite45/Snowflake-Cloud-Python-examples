a=int(input("Enter First Number"))
b=int(input("Enter First Number"))
c=int(input("Enter First Number"))
if(a>b and a<c) or(a<b and a>c):
    print ("Middle Number is :", a)
elif (b>a and b<c) or(b<a and b>c):
    print ("Middle Number is :",b)
else:
    (c>a and c<b) or(c<a and c>b)
    print ("Middle Number is :",c)
