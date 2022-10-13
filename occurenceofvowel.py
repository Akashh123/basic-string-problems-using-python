string = input("Enter your string: ")
vowel = 0
consonant = 0
vowels = "AEIOUaeiou"
for i in string:
    if i in vowels:
        vowel = vowel+1
    elif i.isalpha():
        consonant = consonant+1
print("Ocuurence of Vowels: ", vowel, "Occurence of Consonants: ", consonant)
