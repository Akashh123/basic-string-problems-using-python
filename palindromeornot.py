#First Approach

s1=input("Word: ")
if s1==s1[::-1]:
    print("It is Palindrome")
else:
    print("It is not palindrome")
    
#Second Approach
    
def palindrome(s1):
    for i in range(int(len(s1)/2)):
        if (len(s1)-i-1)!=s1[i]:
            print("It is not palindrome")
        else:
            print("It is palindrome")
s1=input("Word: ")
palindrome(s1)