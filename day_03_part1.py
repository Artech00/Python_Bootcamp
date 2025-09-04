import os

# ========================================
# Lesson 32: IO with Basic Files(PART 1)
# ========================================
#
# ================================
# --- Old-style file handling (Python 2.x+; must manually close files) ---
# ================================

# Create folder
folder = "day_03_file_modes_examples"
os.makedirs(folder, exist_ok=True)

# 1. File for 'r' mode
path1 = os.path.join(folder, 'file.txt')
with open(path1, 'w') as f:  # pre-fill file with some text
    f.write("First line\n"
            "Second line\n"
            "Third line\n")

print("<OLD style method>")
print("->First read")
my_file = open(path1)
print(my_file.read())
print(my_file.read())  # returns empty string, cause cursor is at the end of our file

my_file.seek(0)  # Reset-ենք անում cursor-ը դեպի սկիզբ
print("->Second read")
print(my_file.read())
print('\n')
# my_file = open('fileee.txt')

# readlines() մեթոդը կարդում է ֆայլի բոլոր տողերը ու վերադարձնումա դրանք ցուցակի տեսքով(returns`list)
# ամեն տող դառնում է ցուցակի էլեմենտ, ներառելով (\n) սիմվոլը
print("->Reading with readlines() method")
my_file.seek(0)  # Reset the cursor to the beginning. (Reset-ենք անում cursor-ը դեպի սկիզբ)
print(my_file.readlines())
print('\n')

# --- Close the file manually since we are not using 'with' here ---
my_file.close()

# ================================
# --- New-style 'with' (Python 2.5+; standard in Python 3.x) ---
# ================================

# 'with' block-ը context manager-ա
# Ինքը ավտոմատ ձևով կառավարումա ֆայլի բացումն ու փակումը
# Ու ավտանգա, էն առումով որ`դաժը եթե error ունենանք, ֆայլը մեկա ապահով փակեվելուա

print("<NEW style method>")
# Explicitly setting mode='r'; reading is the default when mode is not specified
with open(path1, mode='r') as f:  # Level 0
    # Level 1: indented under 'with'
    # 'f' exists here (temporary variable representing the open file)
    # Read all lines from the file into a list
    file_lines = f.readlines()  # Level 1: file_lines created
    print(file_lines)  # Level 1: valid
    # 'file_lines' is a regular variable storing the content
    # unlike 'f', it still exists after the block ends
    # 'f' will be automatically closed when this block ends

# --- Outside of 'with' block ---
# Level 0
# 'f' is no longer accessible (file is closed automatically)
# 'file_lines' still exists and can be used
print('\n')
print("File is automatically closed, but lines are still stored in file_lines variable:")  # Level 0
print(file_lines)  # Level 0
print('\n')

# The following line would give an error if uncommented:
# print(f.read())  # Level 0: ERROR, 'f' no longer exists
