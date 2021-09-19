# numbers_set = {1, 2, 3, 4, 4}         # duplicate values removed

# numbers_set = {1, 2, 3, 4, [5, 6]}    # cannot use mutable data types

numbers_set = {1, 2, 3, 4, (5, 6)}      # tuples are immutable, OK to use!
# print(numbers_set)

# Accessing set values
words_set = {"Alpha", "Bravo", "Charlie"}

# Iterating through a set using the 'for' loop
abcd = ""
for words in words_set:
    abcd += words
print(abcd)

# Checking if values are in sets using the 'in' keyword
if "Alpha" in words_set:
    print("Alpha is in set")
else:
    print("Alpha is not in set")

# Modifying set values

words_set.add("Delta")
print(words_set)

words_set.discard("Bravo")
print(words_set)
