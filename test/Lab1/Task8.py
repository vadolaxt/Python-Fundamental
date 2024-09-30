"""
Task 8. Write a Python program to check whether a given password meetsthe following
requirements: The password must be at least eight characters long; contain at least
one uppercase letter; contain at least one lowercase letter; contain at least one
numeric digit; and contain at least one special symbol (i.e., @, &, ...)
"""
import re
def check(s):
    if not re.search("[a-z]",s):
        return False
    if not re.search("[A-Z]",s):
        return False
    if not re.search("[0-9]",s):
        return False
    if not re.search("[!@#$%^&*()]",s):
        return False
    if not (len(s)>=8):
        return False
    return True
print(check("Aa1@abcd"))
print(check("Ab1#a"))
print(check("b1#aaaa"))
print(check("A1#AAAAA"))
print(check("Ab1aaaaa"))
print(check("Ab#aaaaa"))


