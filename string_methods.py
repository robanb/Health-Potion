#  string.method()
#  .count() -> the no. of occurance of a string character or group of characters
print("count".count("c"))

text = "happy birthday"
print(text.count("day"))

#  .lower() -> convert to lowercase
#  .upper() -> convert to uppercase
x = "Happy Birthday"
print(x.lower())
print(x.upper())

#  the string methods doesn't change the original value of the varibale unless we assign/overwrite the the new value with any methods. So the strings are immutable
print("Original value: " + x)

x= x.upper() 
print("New value: " + x)

x= x.lower() 
print("New value: " + x)


#  capitalize(): turns the first letter to uppercase
y = '''hello world, it's me Roba'''
print(y.capitalize())
y = y.capitalize()
print(y)

#  .title(): turns the first letter of every word to uppercase
print(y.title())
y=y.title()
print("New y: " + y)

#  .islower() -> check if it's in lowercase
print(y)
print(y.islower())

#  .isupper() -> check if it's in uppercase
y = "This is in uppercase"
z = "THIS IS IN UPPERCASE"
print(y.isupper())
print(z.isupper())

#  .istitle() -> checks if the string is in titlecase
y = "This Is Titlecase"
z = "This is not titlecase"
print(y.istitle())
print(z.istitle())


#  .isalpha() -> checks if the string contains only the strings
x = "It does not contain, becase it has spaces as well"
y = "helllo"
print(x.isalpha())
print(y.isalpha())


#  .isdigit() -> checks if the string contains only the digits
x = "hello12"
y="12345"
print(x.isdigit())
print(y.isdigit())

print("123".isdigit())

#  .isalnum() -> checks  if the strings contains letters from a-z and numbers from 0-9 (alpha numeric)
print("happybirthday123".isalnum())
print("happybirthday123#".isalnum())

# .index() -> checks the index and it crashes the program if the character doesn't exist and it is case sensitive as well
x = "happy birthday"
print(x.index("birthday"))

# id the character or substring doesn't exist, we get ValueError: substring not found
#print(x.index("dkfsjdlfksjd"))

#  .find()  -> checks the index but it will return -1 if the character/substring doesn't exist and it's not case sensitive
print(x.find("birthday"))
print(x.find("dkfsjdlfksjd"))


#  .strip()  ->  remove the strings 
y = "00000happybirthday00000"
print(y.strip("0"))


#  remove on left side
print(y.lstrip("0"))

#  remove on right side
print(y.rstrip("0"))

#  y.strip()  -> removes the spaces from starting and the end
y = "  hello world     "
print(y.strip())

# example use case
name = input("What is your name?:")
print(name)
print(len(name)) #counts the spaces as well
print(len(name.strip())) # the spaces are removed