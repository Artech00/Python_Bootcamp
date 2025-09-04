import os

# ========================================
# Lesson 32: IO with Basic Files(PART 2)
# ========================================
#
# ====================
# File Modes Examples
# ====================
# 1. mode='r'      → read only → Բացումա ֆայլը կարդալու համար։ Սկզբնական Ֆայլը պետքա գոյություն ունենա
# 2. mode='w'      → write only → Փոխարինումա գոյություն ունեցող ֆայլի միջինը, եթե ֆայլը գոյություն չունի՝ ստեղծումա նոր ֆայլ
# 3. mode='a'      → append only → Ավելացնումա ինֆո-ն ֆայլի վերջում, եթե ֆայլը գոյություն չունի՝ ստեղծումա նոր ֆայլ
# 4. mode='a+'     → append and read → Ավելացնումա տվյալները ֆայլի վերջում ու կարդումա, եթե ֆայլը գոյություն չունի՝ ստեղծումա նոր ֆայլ
# 5. mode='r+'     → read and write → Բացումա ֆայլը կարդալու ու գրելու համար։ Ֆայլը պետքա արդեն գոյություն ունենա, նոր ֆայլ չի ստեղծվում
# 6. mode='w+'     → writing and reading → Բացումա ֆայլը գրելու ու կարդալու համար։ Ֆայլի մեջ եղածը փոխարինվումա, եթե ֆայլը չկա՝ ստեղծումա նորը

print("<File Modes Examples>")

# Create folder
folder = "day_03_file_modes_examples"
os.makedirs(folder, exist_ok=True)

# 1. File for 'r' mode
path1 = os.path.join(folder, 'file_read_only.txt')
with open(path1, 'w') as f:  # pre-fill file with some text
    f.write("Initial content for read mode\n")

# 1. 'r' – Read
print("1. 'r' – Read")
with open(path1, 'r') as f:
    print(f.read())
print("-" * 30)

# 2. File for 'w' mode
path2 = os.path.join(folder, 'file_write_only.txt')
with open(path2, 'w') as f:
    f.write("Initial content for write mode\n")

# 2. 'w' – Write
print("2. 'w' – Write (overwrites file)")
with open(path2, 'r') as f:
    print(f"Before writing:\n{f.read()}")  # BEFORE
with open(path2, 'w') as f:
    f.write("Text overwritten in write mode\n")
with open(path2, 'r') as f:
    print(f"After writing:\n{f.read()}")  # AFTER
print("-" * 30)

# 3. File for 'a' mode
path3 = os.path.join(folder, 'file_append_only.txt')
with open(path3, 'w') as f:
    f.write("Initial content for append mode\n")

# 3. 'a' – Append
print("3. 'a' – Append")
with open(path3, 'r') as f:
    print(f"Before appending:\n{f.read()}")  # BEFORE
with open(path3, 'a') as f:
    f.write("Appended line in append mode\n")
with open(path3, 'r') as f:
    print(f"After appending:\n{f.read()}")  # AFTER
print("-" * 30)

# 4. File for 'r+' mode
path4 = os.path.join(folder, 'file_read_write.txt')
with open(path4, 'w') as f:
    f.write("Initial content for read and write mode\n")

# 4. 'r+' – Read and Write
print("4. 'r+' – Read and Write")
with open(path4, 'r+') as f:
    print(f"Before writing:\n{f.read()}")  # BEFORE
    f.write("Added line in r+ mode\n")
with open(path4, 'r') as f:
    print(f"After writing:\n{f.read()}")  # AFTER
print("-" * 30)

# 5. File for 'w+' mode
path5 = os.path.join(folder, 'file_write_read.txt')
with open(path5, 'w') as f:
    f.write("Initial content for w+ mode\n")

# 5. 'w+' – Write and Read
print("5. 'w+' – Write and Read")
with open(path5, 'r') as f:
    print(f"Before writing:\n{f.read()}")  # BEFORE
with open(path5, 'w+') as f:
    f.write("Fresh text in w+ mode\n")
    f.seek(0)  # Reset-ենք անում cursor-ը դեպի սկիզբ
    print(f"After writing:\n{f.read()}")  # AFTER
print("-" * 30)

# 6. File for 'a+' mode
path6 = os.path.join(folder, 'file_append_read.txt')
with open(path6, 'w') as f:
    f.write("Initial content for a+ mode\n")

# 6. 'a+' – Append and Read
print("6. 'a+' – Append and Read")
with open(path6, 'r') as f:
    print(f"Before appending:\n{f.read()}")  # BEFORE
with open(path6, 'a+') as f:
    f.write("Appended line in a+ mode\n")
    f.seek(0)  # Reset-ենք անում cursor-ը դեպի սկիզբ
    print(f"After appending:\n{f.read()}")  # AFTER
print("-" * 30)
