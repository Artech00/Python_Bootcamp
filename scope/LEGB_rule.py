# Local - Inside the current function
# Enclosing - Inside enclosing functions (from inner to outer)
# Global - At the top level of the module
# Built-in - In Python's built-in namespace

x = "global"  # global scope


def outer():
    x = "enclosing"  # local to OUTER (enclosing for INNER)

    def inner():
        x = "local"  # local to INNER
        print(f"Inner: {x}")  # LOCAL x
        print("Length of 'Python':", len("Python"))  # Built-in

    inner()
    print(f"Outer: {x}")  # OUTER local x (enclosing for INNER)


outer()
print(f"Global:{x}")  # GLOBAL x
