from math import *   # Here we import certain math functions
# This basically the introduction

# Data types, Variables, Print function
print("This is my first program with Python")

# Variables with different data types
character_name = "Caleb"    # String Data type
character_age = 20   # Integer data type
is_male = False  # Boolean Data type

print("Well Well Well, if it isn't the guy himself "+ character_name + "!")
print("He is ", str(character_age), "years old by the time of this publishing.")

# Concatenation - appending a string to another
phrase = "Cybersecurity"
print(phrase + " is cool")

# Below are some functions one could implement with strings
print(phrase.upper())
print(phrase.lower())
print(phrase.islower())
print(len(phrase))   # To get the length of a string
print(phrase[0])  # indexing to get the first character
print(phrase.index("c"))
print(phrase.replace("security", "crime"))

num1 = 5.6
print(ceil(num1))
