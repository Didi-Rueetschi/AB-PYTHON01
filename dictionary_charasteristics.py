# Dictionaries

# generating a dictionary
alter = {"Peter":31, "Julia":28, "Werner":35}
print(alter)

# Change a value
alter["Julia"] = 27

# Add an element
alter["Moritz"] = 22

# Delete an element
del alter["Peter"]
print(alter)

# Output
print("Julia:", alter["Julia"])
