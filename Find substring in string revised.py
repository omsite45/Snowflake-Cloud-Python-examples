import re
#
search_string = "ABCDCDC"
pattern = str(input("Enter the string you wanna to search :"))
match = re.findall(pattern, search_string)

    
#If-statement after search() tests if it succeeded
if match:
   print("regex matches: ", match, "Number of time :", len(match))
else:
   print('pattern not found')
