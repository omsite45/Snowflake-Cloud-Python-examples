def is_leap(year):
    leap = False
    
    year=int(input("Enter your year :"))
    n=year
    while(year>=1900) and (year<1000000):
        if(year%4==0) and (year % 100==0) and (year % 400 ==0):
            return True
        else:
            return False
    is_leap(n)



def unique_names(names1, names2):
    return None

if __name__ == "__main__":
    names1 = ["Ava", "Emma", "Olivia"]
    names2 = ["Olivia", "Sophia", "Emma"]
    lst1=[]
    lst2=[]
    i=0
    l=0
    for i in range(len(names1)):
        for l in range(len(names2)):
            if (names1[i]== names2[l]):
                lst1.append(names1[i])
            if (names1[i]!= names2[l]):
                lst2.append(names1[i])
    print(lst1)
    print(lst2)
    print(unique_names(names1, names2)) 
    # should print Ava, Emma, Olivia, Sophia
