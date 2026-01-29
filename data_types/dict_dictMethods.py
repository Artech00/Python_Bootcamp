# Dict

user = {
    "name": "Alex",
    "age": 25,
    "is_working": True
}
# remove age
removed = user.pop("age")
print(user)
print(f"Username: {user["name"]}")
print(user.keys())
print(user.values())
print(user.items())  # keys and vals

user.update({"age": 22})
print(user["age"])  # new age
