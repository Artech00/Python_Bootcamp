# Bool

age = 20
has_id = True

can_enter = age >= 18 and has_id  # if both true
needs_permission = age < 18 or not has_id

print(can_enter)
print(needs_permission)
