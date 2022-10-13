string = input("Enter your string: ")
vowel = "aeiouAEIOU"
result = ""
for i in string:
    if i in vowel:
        i = ""
    result = result + i
print("String without vowels", result)