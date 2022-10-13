string = input("Enter your string: ")
chars = ""
nochars = ""
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in string:
    if i in characters:
        chars = chars+i
    else:
        nochars = nochars+i
print("Characters are: ", chars, "& Without Characters: ", nochars)
