#   This Python code prompts the user to input their name, age, city, and something they enjoy doing. It
#   then stores this information in variables and uses string formatting to create an output message
#   that includes the user's input. Finally, it prints out the formatted output message to the screen.
#   The comments in the code provide explanations and tips on string concatenation, placeholders, and
#   the `.format()` method for string formatting.
#   1. Ask user for name
name = input("What is your name?: ")
print(name)

#   2. Ask user for age
age = input("What is your age?: ")
print(age)

#   3. Ask user for city
city = input("What city do you live in?: ")
print(city)

#   4. Ask user what they enjoy
love = input("what do you love doing?: ")
print(love)

#   5. Create output text
output = "Your name is {} and you are {} years old. You live in {} and you love {}"

#   6. Format and print output text to the screen
print(output.format(name, age, city, love))


#  string concatenation:  string1 + string2
#  {} - placeholders: {0} {1} {2}
#   .format() - format method eg. "Hello {0} you are {1}".format(name, age)


