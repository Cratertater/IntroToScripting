# Jake Million
# 3/6/22

str1 = "P@#yn26at^&i5ve"
alpha = 0
dig = 0
sym = 0
for i in range(0, len(str1)):
    if str1[i].isalpha():
        alpha += 1
    elif str1[i].isdigit():
        dig += 1
    else:
        sym += 1
print("Number of letters: ", alpha, "\nNumber of digits: ", dig, "\nNumber of symbols: ", sym)

str2 = "/*Jon is @developer&musician"
for i in str2:
    if not i.isalpha():
        str2 = str2.replace(i, "")
print(str2)

str3 = "Emma-is-a-data-scientist"
for i in str3:
    if i == "-":
        str3 = str3.replace("-", " ")
print(str3)

str4 = "Hello, have a good day"
cons = "bcdfghjklmnpqrstvwxyz"
for i in str4:
    if i in cons:
        str4 = str4.replace(i, "")
print(str4)
