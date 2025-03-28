#  In Python, strings are iterable and immutable (can't change the value unless we overwrite the initially asigned value) data type (go element by element until you reach the last element) data types
#  Each element has a number and it's called index, by using the index, we get to the element

string= "HELLOWORLD"

#  for single element: variable(index)
print(string[2])

#  for a group of element: variable(start:end:step)
print(string[0:5:1])
print(string[5:11:1])

#  for certain element to the end: variable(start:)
print(string[3:])

#  from certain element to the end in certain steps: variable(start::step)
print(string[3::2])

#  everything upto certain index but not including itself: variable(:index)
print(string[:4])

#  go frm end to the start (reverse the whole string): variable(::-1)
print(string[::-1])

# we can get count from the end as well go get the index, it will start from -1
print(string[-2])

# we can use the index function to avoid having to count the element's index:  variable[variable.index("from_element"):variable.index("to_element")]
print(string[string.index("HELL"):string.index("OW")])

#  eg: take out the word LO
print(string[string.index("LO"):string.index("WO")])