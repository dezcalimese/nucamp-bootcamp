state_capitals = {"Washington": "Olympia",
                  "Oregon": "Salem", "California": "Sacremento"}

# Printing the length of a dictionary
print(len(state_capitals))

# Accessing dictionary values
print(state_capitals["Washington"])

# Adding and modifying key:value pairs
state_capitals["Washington"] = "Aberdeen"
state_capitals["Texas"] = "Austin"
print(state_capitals)

# Removing a key:value pair
del state_capitals["California"]
print(state_capitals)

state_capitals.pop("Oregon")
print(state_capitals)

# With the 'pop' method, you can return the value of the deleted key unlike using the 'del' keyword
removed_capital = state_capitals.pop("Oregon")
print(removed_capital)
