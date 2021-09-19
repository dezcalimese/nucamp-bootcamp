states = ["Washington", "Oregon", "California"]

# Iterating through a list using a 'for' loop

for state in states:
    print(state)

# Example of editing each item in a list before iterating through it
for state in states:
    state = state.lower()
    print(state)

# The 'in' keyword (Checking whether the item is in a list or not, returns a boolean value)
print("Washington" in states)
print("Tennessee" in states)
print("Washington" not in states)

# Concatenating lists
states2 = ["New York", "Florida", "Arizona"]
best_states = states + states2
print(best_states)

# Slicing lists
# Grabbing the items from index 1 up to 3, but not including 3
print(best_states[1:3])
# Grabbing the items from the start of the list up to but not including a certain index
print(best_states[:2])
# Grabbing the items from a certain index to the end of the list
print(best_states[4:])
