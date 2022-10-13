#First Approach:

s1 = input("Check here: ")
if s1 >= "0" and s1 <= "1000":
    print("It is a Digit")
else:
    print("It is not a Digit")
    
#Second Approach using isdigit() func:

s1=input("Check here: ")
if (s1.isdigit()):
    print("It is a digit")
else:
    print("It is not a digit")