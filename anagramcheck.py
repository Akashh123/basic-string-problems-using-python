# Basic:

s1 = input("First Word: ")
s2 = input("Second Word: ")
if sorted(s1) == sorted(s2):
    print("These are anagram")
else:
    print("These are not anagram")

# Func:


def matching(s1, s2):
    if sorted(s1) == sorted(s2):
        print("These are anagram")
    else:
        print("These not anagram")


s1 = input("First Word: ")
s2 = input("Second Word: ")
matching(s1, s2)
