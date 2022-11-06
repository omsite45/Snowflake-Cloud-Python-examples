import calendar
yr=int(input("Enter the year "))

while((yr) >=1900 ) and (yr <=1000000):
    if(calendar.isleap(yr)==True):
        print("Leap year")
        print(calendar.isleap(yr))
        break
    else:
        print(calendar.isleap(yr))
        break
