import numbers


string = input("Enter your string: ")
alphabets = 0
numbers = 0
specialchar = 0
for i in string:
    if i.isdigit():
        numbers = numbers+1
    elif i.isalpha():
        alphabets = alphabets+1
    else:
        specialchar = specialchar+1
print("Ocuurence of Alphabets: ", alphabets, "Occurence of Numbers: ",
      numbers, "Occurence of SpecialChars", specialchar)
