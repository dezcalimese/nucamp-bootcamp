my_string = "alpha"

# Multiline string
multiline_string = """bravo
charlie"""

print(my_string)
print(multiline_string)

# Accessing and slicing characters
print(my_string[0])
print(my_string[3])

print(my_string[0:3])
print(my_string[:2])
print(my_string[2:])
print(my_string)


# Iterating through a string using 'for'
for char in my_string:
    print(char)


# The 'in' keyword
print("pha" in my_string)
print("z" not in my_string)
