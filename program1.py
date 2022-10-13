# Creating a list:
StringA = "Computer"
print("Computer is Great Machine")
print(StringA)

# String Methods:
# 1. len() func:
stringB = "Computer"
print(len(stringB))

# 2. count() func:
stringC = "Computer"
print(stringC.count("C", 0, len(stringC)))  # Here 0 is the starting index

# 3. Allignment funcs:
stringD = "Computer"
print(stringD.center(20, "-"))
print(stringD.ljust(20, "+"))
print(stringD.rjust(20, "+"))

# 4. isalpha() isalnum() isspace() funcs:
string1 = "Computer"
string2 = "123456ABC"
string3 = " "
print(string1.isalpha())
print(string2.isalnum())
print(string3.isspace())

# 5. join() func:
list = ["Computer", "Keyboard", "Mouse"]
s = "+"
print(s.join(list))

# 6. Accessing chars of string by indexing:
stringE = "Computer"
print(stringE[-1])

# 7. Reverse a string:
# Approach 1
stringF = "Computer"
print(stringF[::-1])
# Approach 2
stringG = "Computer"
result = ""
for i in range(len(stringG)-1, -1, -1):
    result = result+stringG[i]
print(result)
# Approach 3
stringH = "Computer"
ABCDEFGH = reversed(stringH)
print("".join(ABCDEFGH))
# String Slicing:

string4 = "Computer"
i = string4[0:4]
print(i)

# Updating string:
# 1
string5 = "Computer"
print(string5)
# -----string5[2]="COM"
# -----str1=("".join(string5))
# -----print(str)
# 2
str2 = (string5[0:2] + "COM" + string5[3:len(string5)])
print(str2)

# Update entire string:

string6 = "Computer"
print(string6)
string6 = "COMPUTER123456"
print(string6)

# Deletion of a character in a string:

str3 = string6[0:2] + string6[3:len(string6)]
print(str3)

# Deletion of one entire string:

# -----del string6
# -----print(string6)

# Escape Sequencing:

# Space
string7 = "Computer\tLaptop"
print(string7)
# New Line
string8 = "Computer\nLaptop"
print(string8)

# Formatting of strings:

# Default
string9 = "{} {}".format("Computer", "Laptop")
print(string9)
# By Index
string9 = "{1} {0}".format("Computer", "Laptop")
print(string9)
# By Keyword
string9 = "{B} {A}".format(A="Computer", B="Laptop")
print(string9)

# Binary representation:

string10 = "{0:b}".format(18)
print(string10)

# Exponent representation:

string10 = "{0:e}".format(18)
print(string10)

# Rounding off:

string10 = "{0:2f}".format(18/2)
print(string10)

# Format method using % operator:

string11 = 18
print("Percentage value will be: %3.2f" % string11)

string11 = 18
print("Percentage value will be: %3.4f" % string11)

# String Concatenation:

v1 = "Computer"
v2 = "Laptop"
print(v1)
print(v2)

# Basic

v3 = (v1, v2)
print(v3)

# Using + Operator:

print(v1 + v2)

# Using Format Func:

v4 = ("{} {}".format(v1, v2))
print("{} {}".format(v1, v2))
print(v4)

# Using Percentage Operator:

print("%s %s" % (v1, v2))

# Using Join Func:

v5 = "".join([v1, v2])
print("".join([v1, v2]))
print(v5)

# String Interpolation:
# Formatting strings using f-string:
string12 = "Computer"
string13 = "Laptop"
# Using f, Python is capturing all the values from variables
print(f"This {string12} and This {string13} : These both are best!")

# Inline arithmetic using f-string:

s1 = 1
s2 = 2
s3 = 3
print(f"{s1}*{s2}-{s3}={s3*(s1-s2)}")
