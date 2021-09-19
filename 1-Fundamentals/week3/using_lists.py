states = ["Washington", "Oregon", "California"]


# Accessing list values

# Printing the first/second/third items in a list normally
print(states[0])
print(states[1])
print(states[2])

# Accessing items from the opposite ends of an index
print(states[-1])
print(states[-2])
print(states[-3])


# Modifying list values
states[2] = "Arizona"
print(states)

# Finding out how many items are in a list
print(len(states))

# Appending (adding an item) a list
states.append("New York")
print(states)

# Removing an item from a list
states.pop()    # Leaving the parameter list empty removes the last item from the list
print(states)

states.pop(1)   # Removing a specific item from the list
print(states)
