# Jake Million
# 3/1/22

# Dictionary of all letter and numbers and their morse code equivalents(I added an apostrophe for fun)
morse = {' ': ' ', ',': '--..--', '.': '.-.-.-', '?': '..--..', '\'': '·----·', '0': '-----', '1': '.----',
         '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
         'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
         'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
         'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.-', 'Z': '--..'}

# string to store the morse code
morseStr = ""

# Comparing 's' string to 'morse' dictionary
s = input("Enter a sentence: ")
s = s.upper()
for e in s:
    for i in morse:
        if e == i:
            morseStr += morse[e]

print(morseStr)
