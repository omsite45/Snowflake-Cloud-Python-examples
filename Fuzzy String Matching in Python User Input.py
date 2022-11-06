from thefuzz import fuzz, process
n=int(input("Enter the number of  book elements you wanna to enter "))
books=[]
i=0
for i in range(1,n+1):
            print("Enter the book ",i," ", end="")
            ele=str(input())
            books.append(ele)
print("Enter the string you wanna to extract :", end="")
print(process.extract(str(input()),books, limit=3,
                scorer=fuzz.token_sort_ratio))
