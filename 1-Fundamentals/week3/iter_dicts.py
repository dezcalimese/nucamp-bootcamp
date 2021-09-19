state_capitals = {"Washington": "Olympia",
                  "Oregon": "Salem", "California": "Sacremento"}


# Iterate using values
for city in state_capitals.values():
    print(city)     # The values will be printed


# Iterate with both keys and values
for state in state_capitals:
    print(state_capitals[state], "is the capital of", state)

# The keys will be printed
for state, city in state_capitals.items():
    print(city, "is the capital of", state)
