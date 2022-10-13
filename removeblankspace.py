string = input("Enter your string: ")
blankspace = " "
result = ""
for i in string:
    if i not in blankspace:
        result = result+i
print(result)