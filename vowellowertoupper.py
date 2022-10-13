# Using Function:
def toggle(phrase):
    answer = ""
    for letter in phrase:
        if letter not in "aeiouAEIOU":
            answer = answer + letter.lower()
        else:
            answer = answer + letter.upper()
    return answer


print(toggle(input("Enter a phrase: ")))