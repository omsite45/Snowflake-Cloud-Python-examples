word = 'geeks for geeks vnjrkj dbh geeks eb geeks d4ybyb'
 
# returns first occurrence of Substring
result=str(input("Enter the word you wanna tro search "))
result1 = word.find(result)
res=word.split()
count=0

for i in range(len(res)):
    if(res[i]==result):
        count+=1
print("Number of times ", result,"Occured is ",count)
        

