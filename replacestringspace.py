#First Approach:

s1 = input("String: ")
s2 = input("Enter the character: ")
result = ""
for i in s1:
    if i == " ":
        i = s2
    result = result+i
print(result)

#Using Method/Func:

def replacing(s1, s2, result):
    for i in s1:
        if i == " ":
            i = s2
        result = result+i


print(result)
result = ""
s1 = input("String: ")
s2 = input("Enter the character: ")
replacing(s1, s2, result)
