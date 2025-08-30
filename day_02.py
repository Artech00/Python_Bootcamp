# ===================================
# Lesson 22: Dictionaries in Python
# ===================================

# Dictionary-ն data structure է, որտեղ object-ները պահվում են key-value զույգերով:
# Key-ի միջոցով access -ենք ունենում իրա value-ին, առանց index-ի մասին մտածելու:
# Key-երը պտի լինեն unique ու immutable (օրինակ՝ string, number, tuple):
# Եթե key-երը կրկնվեն, dictionary-ում կմնա միայն վերջի overwrite արածը։

# Simple dictionary example
person = {
    'first_name': 'Anna',
    'last_name': 'Petrosyan'
}

print(person)  # {'first_name': 'Anna', 'last_name': 'Petrosyan'}
print(person['first_name'])  # 'Anna'

# Dictionary-ի օրինակ՝ immutable keys-ով
my_dict = {
    "name": "Ali",  # string
    42: "answer",  # integer
    (1, 2): "tuple key"  # tuple
    # [1, 2, 3]: "value"  # ❌ list is mutable
    # {"set"}: "value"  # ❌ set is mutable
}

# Accessing values using keys
print(my_dict["name"])  # Output: Ali
print(my_dict[42])  # Output: answer
print(my_dict[(1, 2)])  # Output: tuple key

# Nested dictionary (dict inside another dict) and list example
profile = {
    'hobbies': ['reading', 'gaming', 'swimming'],  # list used as the value for this key
    'details': {'username': 'ali', 'age': 25},  # nested dictionary with user details
    'membership': 'premium'  # simple key-value pair
}
print(f"Hobbies: {profile['hobbies']}")  # All hobbies
print(f"First hobby: {profile['hobbies'][0]}")  # Access first hobby
print(f"Username: {profile['details']['username']}")  # Access nested dictionary value

# Example of .upper() method
print(f"Capitalized username: {profile['details']['username'].upper()}")  # ALI

# Adding a new element to an existing dictionary
profile['city'] = 'Gyumri'
print(profile)  # {'hobbies': [...], 'details': {...}, 'membership': 'premium', 'city': 'Gyumri'}

# Dictionary methods
grades = {'math': 90, 'english': 85, 'history': 92}
print(f"All keys of grades: {grades.keys()}")  # dict_keys(['math', 'english', 'history'])
print(f"All values of grades: {grades.values()}")  # dict_values([90, 85, 92])
print(f"All items of grades: {grades.items()}")  # dict_items([('math', 90), ('english', 85), ('history', 92)])

# =============================
# Lesson 26: Tuples in Python(օգտագործվում է '()' -ի հետ (IMMUTABLE) )
# =============================

# tuple-ը պահումա տարբեր տիպի օբյեկտներ։ (ints, strings, floats, etc.)
# tuple-ի էլեմենտները ինդեքսավորված են՝ սկսած 0-ից։

# Tuple-ը նմանա list-ին, մենակ են տարբերությամբ որ ինքը անփոփոխա(IMMUTABLE),
# այսինքն իրա մեջի էլեմենտները չենք կարա փոխենք

# Example demonstrating immutability vs mutability
my_list = [1, 2, 3]  # list
my_tuple = (1, 2, 3)  # tuple

print(f"Original list: {my_list}")
my_list[0] = 10  # changing first element in list
print(f"Modified list: {my_list}")  # Works

print(f"Original tuple: {my_tuple}")
# my_tuple[0] = 10     # This would give an error because tuples are immutable

# Basic tuple examples
t = (1, 2, 3)
print(f"Type of t: {type(t)}")
print(f"First element of t: {t[0]}")
print(f"Last element of t: {t[-1]}")

t2 = ('a', 'a', 'b')
print(f"{t2[0]} occurs {t2.count('a')} times, first index is {t2.index('a')}")

# ===========================
# Lesson 28: Sets in Python (օգտագործվում է '{}' կամ set() -ի հետ (MUTABLE) UNIQUE values))
# ===========================

# Set -ը unordered(ոչ դասավորված) էլեմենտների հավաքածուա,
# որտեղ էտ ելեմենտները չեն կարա կրկնվեն
# այսինքն եթե duplicate արժեքներ ունենանք set-ի մեջ,
# էտ duplicate արժեքները ավտոմատ ջնջվելեւ են

# Քանի որ set-ի էլեմենտները չունեն կոնկրետ հերթականություն,
# print-ի ժամանակ էլեմենտների հերթականությունը կարա տարբերվի
unordered_example = {"one", "two", "three", "four"}
print(unordered_example)  # Output might differ each time

# set-ի էլեմենտները ինդեքսավորված չեն։ (unindexed),
# այսինքն չենք կարա access ունենանք իրա էլեմենտներին ինդեքսով
# set-ը mutable-ա, այսինքն իրա էլեմենտները կարանք փոխենք

# Example: sets are mutable
numbers = {1, 2, 3}
print("Original set:", numbers)  # Output: {1, 2, 3}

# Add a new element
numbers.add(4)
print("After adding 4:", numbers)  # Output: {1, 2, 3, 4}

# Remove an existing element
numbers.remove(2)
print("After removing 2:", numbers)  # Output: {1, 3, 4}

# empty set
my_set = set()

my_set.add(1)
my_set.add(2)
my_set.add(2)  # կրկնվող արժեքը չի ավելացվի
print(my_set)  # Output: {1, 2}

# ===== Example: list -> set casting =====
my_list = [1, 1, 1, 1, 2]
unique_values = set(my_list)  # casting list as a set
print(unique_values)  # Output: {1, 2}

# ===== Another example
basket = {"apple", "banana", "cherry", "apple", "banana"}
print(basket)  # show that duplicates have been removed

# ===== Example: membership test =====
print(1 in my_set)  # True
print(3 in my_set)  # False

# ===============================
# Lesson 30: Booleans in Python
# ===============================

# Booleans-ը ներկայացնումա 2 արժեք՝ True կամ False(ճշմարիտ կամ կեղծ արժեքներ)

print(type(True))  # Output: <class 'bool'>
print(1 > 2)  # Output: False
print(3 > 2)  # Output: True
print(1 == 1)  # Output: True

# None keyword-ն օգտագործվում է որպես placeholder էն օբյեկտների համար,
# որոնց դեռ արժեք չենք նշանակել
b = None
print(type(b))  # Output: <class 'NoneType'>
print(b)  # Output: None
