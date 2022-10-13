# 1st Approach:

s1 = input("Word: ")
s2 = input("Character: ")
string = s1.replace(s2, "")
print(string)
# 1st Approach Func:


def deletion(s1, s2):
    print(s1.replace(s2, ""))


s1 = input("Word: ")
s2 = input("Character: ")
deletion(s1, s2)

# 2nd Approach:


def deletionchar(s1, s2):
    dict = {ord(s2): None}
    print(s1.translate(dict))


s1 = input("Word: ")
s2 = input("Character: ")
deletionchar(s1, s2)
