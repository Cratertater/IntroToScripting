# Jake Million
# 3/6/22

# counting vowels
def vowCount(sen):
    vows = "aeiou"
    c = 0
    for i in sen:
        if i in vows:
            c += 1
    return c


# counting consonants
def consCount(sen):
    cons = "bcdfghjklmnpqrstvwxyz"
    b = 0
    for i in sen:
        if i in cons:
            b += 1
    return b


s1 = input("Enter a string: ")
print("Number of vowels in entered string: ", vowCount(s1))
print("Number of consonants in entered string: ", consCount(s1))
