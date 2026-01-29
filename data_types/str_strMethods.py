# str, str methods

firstName = "Ashot"
lastName = "Ayvazyan"

fullName = firstName + " " + lastName
print(fullName)

print(firstName.upper())
print(lastName.upper())
print(firstName.replace("Ashot", "Hayk"))

splitFullname = fullName.split(" ")
print(f"Splitted: {splitFullname}")
print(type(splitFullname))

joinedFullname = "-".join(fullName)
print(f"Joined: {joinedFullname}")
print(type(joinedFullname))
