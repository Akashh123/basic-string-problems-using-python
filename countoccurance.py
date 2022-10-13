# 1st Approach:

s1 = input("Type your word: ")
s2 = input("Type the character: ")
print(s1.count(s2))

# 2nd Approach:

s1 = input("Word: ")
s2 = input("Character: ")
count = 0
for i in range(0, len(s1)):
    if (s1[i] == s2):
        count = count+1
print(count)

# 3rd Approach

s1 = input("Word: ")
s2 = input("Chracter: ")
count, index = 0, 0
while(index < len(s1)):
    if s2[index] == s2:
        count=count+1
index = index+1
print(count)

        