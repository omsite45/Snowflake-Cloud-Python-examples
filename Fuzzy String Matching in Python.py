from thefuzz import fuzz, process
s1=input("Enter the input1 ")
s2=input("Enter the input1 ")
print(fuzz.partial_ratio(s1,s2))
print("Token Sort Ratio ", fuzz.token_sort_ratio(s1,s2))
print()
