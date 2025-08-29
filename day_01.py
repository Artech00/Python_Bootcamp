# ===============================
# Lesson 1: Intro to Python Data Types
# ===============================

# Python-ում հիմնական Data Type-երը
# integers        → int → ամբողջ թիվ
# floating point  → float → կոտորակային թիվ
# strings         → str → տեքստ(IMMUTABLE)
# list            → list → ցուցակ (MUTABLE) → փոփոխվող է, այսինքն կարելի է փոխել ներսի արժեքները)
# dictionaries    → dict → բառարան key-value
# tuples          → tuple → անփոփոխ ցուցակ (IMMUTABLE)
# sets            → set → հավաքածու (unique items)
# booleans        → bool → True / False արժեքներ

# ===============================
# Lesson 2: Python Numbers
# ===============================

print(2 - 1)  # minus → 1
print(2 * 2)  # multiply → 4
print(7 / 2)  # division → 3.5
print(7 % 2)  # remainder → 1
print(50 % 5)  # remainder → 0
print(2 ** 3)  # exponentiation → 2^3 = 8 (2-ի խորանարդը)

# ===============================
# Lesson 6: Variable Assignment
# ===============================

# Փոփոխականների անուններ գրելու կանոններն են, որ։
# 1. Չի կարա սկսվի թիվով
# 2. Չի կարա պարունակի space-եր → օգտագործել "_"
# 3. Չենք կարա օգտագործենք `/ $ ? - + ! @` symbol-ները՝ և այլն

# Python-ում օգտագործվումա DYNAMIC TYPING
# Փոփոխականի type-ը որոշվում է runtime-ի ժամանակ
# (այսինքն ծրագրի աշխատելու պահին)
#
# C++-ում type-ը որոշվում է compile-time
# (մինչ մեր կոդը run անելը)

my_dog = 1  # type → int
my_dog = "sammy"  # type → str
print(type(my_dog), my_dog)  # <class 'str'> sammy

# C++-ում նման բան error կտա

my_income = 100
tax_rate = 0.1
my_taxes = my_income * tax_rate
print(my_taxes)  # 10.0

# ===============================
# Lesson 7: Intro to Strings(IMMUTABLE)
# ===============================
# String-ը char-երի ինդեքսավորված հաջորդականությունա (ordered sequence)
# String-երը գրում ենք " " -ի  կամ '' -ի մեջ (double quotes-ի կամ single quotes-ի մեջ)
intention = "I'm going\n to run"  # \n adds a new line
print(intention)
print(len(intention))  # string-ի երկարությունը

# ===============================
# Lesson 9: String Indexing and Slicing
# ===============================

word = "Hello"

# Indexing
print(word[0])  # first element
print(word[-1])  # last element

# Slicing → word[start:stop:step]
# - start → index, որտեղից սկսումա slice-ը (default=0)
# - stop  → index, որտեղ կանգնումա (excluded, default: end of string)
# - step  → քայլ, քանի հատ skip անի (default=1)

print(word[::])  # 'Hello' (full string)
print(word[0:4])  # 'Hell' (0-ից մինչև 4, բայց 4-ը չի մտնում)
print(word[0::2])  # 'Hlo'  (սկսումա 0-ից, քայլ=2 → յուրաքանչյուր 2-րդ սիմվոլը)

# Հետ շրջել string-ը
print(word[::-1])  # 'olleH'

# ===============================
# Lesson 12: String Properties and Methods(IMMUTABLE)
# ===============================

# String-երը Python-ում ԱՆՓՈՓՈԽ են (IMMUTABLE).
# Այսինքն string-ի մեջ առժեք(value) չենք կարա փոխենք
# բայց կարանք ստեղծենք նոր string-եր՝ հնի հիման վրա։

name = "Sam"

# name[0] = "P"   # ❌ ERROR → str immutable

# Նոր string՝ հնի հիման վրա։
new_name = "P" + name[1:]
print(new_name)  # Pam

# String concatenation + slicing
name = "Sam"
name2 = "P" + name[1:]
print(name2)  # Pam

# Repetition with *
letter = 'z'
letters = letter * 3
print(letters)  # zzz

# Concatenation (numbers as strings)
print('2' + '3')  # 23 (not 5)

# Changing case
name = "kate"
print(name.upper())  # KATE
print(name.lower())  # kate
print(name.capitalize())  # Kate

# Splitting
current_date = "8/15/2025"
current_date = current_date.split("/")
# split() → բաժանումա string-ը մասերի ըստ delimiter-ի
# օրինակ "8/15/2025".split("/") → ["8","15","2025"]
print(current_date)

# ==========================================
# Lesson 15: Print Formatting with Strings
# ==========================================

# Python-ում կա մի քանի ձև string-ները format անելու համար:
# Հին տարբերակը -> .format()
# Նոր ու ամենաշատ օգտագործվող տարբերակը -> f-strings (Python 3.6+)

# --- .format() օրինակ ---
print("This is a string {}".format("INSERTED"))

# Curly braces {} օգտագործվում են որպես placeholder-ներ,
# իսկ format()-ի մեջ փոխանցած արժեքները դրվում են placeholder-ների տեղը:
print("The {q} {b} {f}".format(f="fox", b="brown", q="quick"))

# --- f-string օրինակ (նույնը, բայց ավելի modern) ---
q = "quick"
b = "brown"
f = "fox"

# f-string-ի դեպքում string-ի սկզբում դնում ենք 'f',
# և curly braces {}-ի մեջ ուղղակի գրում ենք փոփոխականի անունը:
print(f"The {q} {b} {f}")

# f-string-ի մեկ ուրիշ օրինակ
name = "Bob"
# curly braces {}-ի մեջ գրումենք փոփոխականի անունը,
# ու Python-ը ավտոմատ տեղադրումա իրա արժեքը string-ի մեջ:
print(f"my name is {name}")  # Output -> my name is Bob

# Python-ում թվերի (հատկապես float-երի) print-ի ժամանակ
# կարանք կառավարենք ինչպես են նրանք երևում:
#
# Սինտաքսը -> {value:width.precisionf}
# - width -> ընդհանուր տողի երկարությունը (ներառյալ թվերն ու կետը)
# - precision -> քանի նիշ ցույց տալ կետից հետո
# - f -> float format

# --- Օրինակներ ---

# Սովորական print
result = 100 / 777
print(result)  # 0.1287001287001287

# f-string տարբերակ (modern)

print(f"Result: {result:.3f}")  # 3 նիշ կետից հետո (precision=3), no width set

# Եթե width-ը նշում ենք (օր․ -> 10), Python-ը "տեղ" է բացում,
# որ ընդհանուր output-ը լինի նվազագույնը 10 նիշ երկարությամբ։
# Եթե թվերը քիչ են, ավելացնում է space-եր ձախից:
print(f"Result: {result:10.5f}")  # total width=10, precision=5, left padded with spaces

# ============================
# Lesson 18: Lists in Python (օգտագործվում է '[]' -ի հետ (MUTABLE) )
# ============================

# List-ը պահումա տարբեր տիպի օբյեկտներ։ (ints, strings, floats, etc.)
# List-ը mutable-ա, այսինքն իրա էլեմենտները կարանք փոխենք
# List-ի էլեմենտները ինդեքսավորված են՝ սկսած 0-ից։

# Example demonstrating mutability
my_list = [1, 2, 3]  # list
print(f"Original list: {my_list}")
my_list[0] = 10  # changing first element in list
print(f"Modified list: {my_list}")  # Works

# === Simple list ===
list1 = [1, 2, 3]
print(list1[0])  # first element

# === Mixed-type list ===
list2 = ["String", 5, 10.7]
print(list2)

# === List concatenation (լիստերի միավորում) ===
new_list = list1 + list2
print(new_list)

# === Modify elements (list-երը mutable են) ===
new_list[0] = "ONE ALL CAPS"
print(new_list)

# === Append element ===
new_list.append(11)  # ավելացնում ենք նոր value
print(new_list)

# === Remove last element ===
new_list.pop()  # ջնջում ենք վերջի արժեքը
print(new_list)

# === Sorting lists ===
letters_list = ['a', 'e', 'x', 'c', 'b']
num_list = [4, 1, 3, 6]

letters_list.sort()  # փոքրից մեծը
num_list.sort()
print(letters_list, num_list)

# === Correct way to get a sorted copy ===
num_list2 = [4, 1, 3, 6]
sorted_num_list2 = sorted(num_list2)  # creates a new sorted list, original stays intact
print(sorted_num_list2)

# === Reverse a list ===
num_list2.reverse()  # reverses the original list
print(f"Reversed num_list2: {num_list2}")
