#string.method()
#.count() -> the no. of occurance of a string character or group of characters
print("count".count("c"))

text = "happy birthday"
print(text.count("day"))

#.lower() -> convert to lowercase
#.upper() -> convert to uppercase
x = "Happy Birthday"
print(x.lower())
print(x.upper())

#the string methods doesn't change the original value of the varibale unless we assign/overwrite the the new value with any methods. So the strings are immutable
print("Original value: " + x)

x= x.upper() 
print("New value: " + x)

x= x.lower() 
print("New value: " + x)


#capitalize(): turns the first letter to uppercase
y = '''hello world, it's me Roba'''
print(y.capitalize())
y = y.capitalize()
print(y)

#.title(): turns the first letter of every word to uppercase
print(y.title())
y=y.title()
print("New y: " + y)

