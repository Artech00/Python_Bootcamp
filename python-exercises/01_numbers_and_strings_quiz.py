# Numbers quiz

import string

# 1. What is the output of the following number comparison function call

print((1.1 + 2.2) == 3.3)

# Տասնորդական թվերը համակարգչի հիշողության մեջ պահվում են որոշակի շեղումով
# Օրինակ՝ 1.1 կամ 2.2–ը պահվում են մոտավոր, ոչ թե 100% ճշգրիտ։
# Դրա համար (1.1 + 2.2) == 3.3 տալիսա False
# print((1.1 + 2.2) == 3.3)

number = (1.1 + 2.2)  # 3.3000000000000003
number *= 10 ** 10  # Բազմապատկում ենք, որ սխալը ավելի նկատելի լինի
number1 = 33000000000  # Ամբողջ թիվը պահվում է միշտ ճշգրիտ
number1 /= 10 ** 10  # Բաժանում ենք, ստանում ենք ճիշտ 3.3
print(number1)  # 3.3

# Ստեղ համեմատությունը չի ստացվում՝ նույն պատճառի համար.
# print((1.1 + 2.2) == 3.3)

# Օգտագործում ենք round() ֆունկցիան, որ էտ թվերի որոշակի շեղումը չունենաք
print(round(1.1 + 2.2, 10) == round(3.3, 10))  # Արդյունքը կլինի 3.3

# 2. What is the output of the following python code

import math

# math.ceil(x) → վերադարձնումա ՄՄԵՆԱՓՈՔՐ ամբողջ թիվը,
# որը մեծ կամ հավասար է մեր տվյալ թվին
# Օրինակ՝ x = 3.2
# բոլոր ամբողջ թվերը, որոնք ≥ 3.2, են՝ 4, 5, 6, ...
# դրանցից ամենափոքր թիվը, որը բավարարում է «≥ 3.2»-պայմանին, 4-ա
print(math.ceil(3.2))  # 4  (3.2–ից մեծ կամ հավասար ամենափոքր ամբողջ թիվը)
print(math.ceil(-3.2))  # -3 (-3.2–ից մեծ կամ հավասար ամենափոքր ամբողջ թիվը)

# math.floor(x) → վերադարձնում է ԱՄԵՆԱՄԵԾ ամբողջ թիվը,
# որը փոքր կամ հավասար է մեր տվյալ թվին
# Օրինակ՝ x = 3.7
# բոլոր ամբողջ թվերը, որոնք ≤ 3.7, են՝ 3, 2, 1, ...
# դրանցից ամենամեծ թիվը, որը բավարարում է «≤ 3.7»-ը, 3-ա
print(math.floor(3.7))  # 3  (3.7–ից փոքր կամ հավասար ամենամեծ ամբողջ թիվը)
print(math.floor(-3.7))  # -4 (-3.7–ից փոքր կամ հավասար ամենամեծ ամբողջ թիվը)

# String quiz

# Exercise 1A: Create a string made of the first, middle and last character

str1 = "James"
print(str1[::2])

# Exercise 1B: Create a string made of the middle three characters
str1 = "JaSonAy"
str1_len = int(len(str1) / 2)

print(str1[str1_len - 1:str1_len + 2])

# Exercise 3: Create a new string made of the first, middle,
# and last characters of each input string

s1 = "America"
s2 = "Japan"

s1_len_half = int(len(s1) / 2)
s2_len_half = int(len(s2) / 2)
string_mix = s1[0] + s2[0] + s1[s1_len_half] + s2[s2_len_half] + s1[-1] + s2[-1]
print(string_mix)

# Exercise 4: Arrange string characters such that lowercase letters should come first

# version 1
str1 = "PyNaTive"
lowers = ""
uppers = ""
for letter in str1:
    if letter.islower():
        lowers += letter
    else:
        uppers += letter
print(lowers + uppers)

# version 2
str1 = "PyNaTive"
lowers = []
uppers = []
for char in str1:
    if char.islower():
        lowers.append(char)
    else:
        uppers.append(char)
sorted_str1 = ' '.join(lowers + uppers)  # separated by space
print(sorted_str1)

# Exercise 5: Count all letters, digits, and special symbols from a given string

str1 = "P@#yn26at^&i5ve"
chars = []
digits = []
symbols = []

chars_count = 0
digits_count = 0
symbol_count = 0

for char in str1:
    if char.isalpha():
        chars.append(char)
        chars_count += 1
    elif char.isdigit():
        digits.append(char)
        digits_count += 1
    else:
        symbols.append(char)
        symbol_count += 1

print(chars_count, chars)
print(digits_count, digits)
print(symbol_count, symbols)

# Exercise 7: String characters balance Test
s1 = "Yn11"
s2 = "PYnative11"

for char in s1:
    if char in s2:
        print(True, char)
    else:
        print(False, char)

# Exercise 8: Find all occurrences of a substring in a given string by ignoring the case
# Write a program to find all occurrences of “USA” in a given string ignoring the case

str1 = "Welcome to USA. usa awesome, isn't it?"
word = "USA"
str1_lower = str1.lower()
word_lower = word.lower()

count = str1_lower.count(word_lower)
print("The USA count is", count)

# Exercise 9: Calculate the sum and average of the digits present in a string

str1 = "PYnative29@#8496"
str1_digits = []
str1_sum = 0
for char in str1:
    if char.isdigit():
        str1_digits.append(char)
        str1_sum += int(char)

str1_average = str1_sum / len(str1_digits)
print("Sum is:", str1_sum, "Average is", str1_average)

# Exercise 10: Write a program to count occurrences of all characters within a string
str1 = "Apple"
for char in str1:
    count = str1.count(char)
    print(count, char)

# Exercise 11: Reverse a given string
str1 = "PYnative"
print(str1[::-1])

# Exercise 12: Find the last position of a given substring
# Write a program to find the last position of a substring “Emma” in a given string.
str1 = "Emma is a data scientist who knows Python. Emma works at google."
print(str1)
index = str1.rfind("Emma")
print(index)

# Exercise 13: Split a string on hyphens
# Write a program to split a given string on hyphens and display each substring.

str1 = "Emma-is-a-data-scientist"
str1_substr = str1.split("-")
print(str1_substr)
for char in str1_substr:
    print(char)

# Exercise 14: Remove empty strings from a list of strings
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric"]
clean_list = []
for s in str_list:
    if s:
        clean_list.append(s)
print(clean_list)

# Exercise 15: Remove special symbols / punctuation from a string
import string

str1 = "/*Jon is @developer & musician"

# 1st('') & 2nd('') args empty (skipped), 3rd deletes punctuation
# str.maketrans('', '', string.punctuation) creates a mapping table(dictionary) that tells translate()
# to remove all punctuation characters
table = str.maketrans('', '', string.punctuation)
# string.punctuation = !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ → Unicode: 33-126
# string.punctuation-ը Python-ի string մոդուլի մեջի պատրաստի փոփոխականա, որտեղ արդեն ներառված էն տարբեր ձևի symbol-ներ

# Removes or replaces characters in str1 according to the translation table 'table'
new_str = str1.translate(table)

print(table)
print(new_str)

# Exercise 17: Find words with both alphabets and numbers
# Write a program to find words with both alphabets and numbers from an input string.
str1 = "Emma25 is Data scientist50 and AI Expert"

wrds_letters = []  # list to store words with both letters and numbers

words = str1.split()  # split string into words
# ['Emma25', 'is', 'Data', 'scientist50', 'and', 'AI', 'Expert']

print(words)
for w in words:  # from each word
    # from each word, check for each char(if at least 1 letter, and 1 digit is found)
    if any(str1.isalpha() for str1 in w) and any(str1.isdigit() for str1 in w):
        wrds_letters.append(w)

print("Words with letters and numbers:")
for w in wrds_letters:
    print(w)

import string

# Exercise 18: Replace each special symbol with # in the following string

str1 = '/*Jon is @developer & musician!!'
replace_char = '#'

# string.punctuation = !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ → Unicode: 33-126
# string.punctuation-ը Python-ի string մոդուլի մեջի պատրաստի փոփոխականա, որտեղ արդեն ներառված էն տարբեր ձևի symbol-ներ
for char in string.punctuation:
    str1 = str1.replace(char, '#')

print(type(string.punctuation))
print(str1)
