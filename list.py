A = [1,2,3,4,5]
print(A)

# Add 6 to list A using append
A.append(6)
print(A)

# Add 7 to list A using +
A = A + [7]
print(A)

# Add 8, 9 to list A
A = A + [8,9]
print(A)

# Add ABC to list A using + list("ABC"), since "ABC" is iterable but this won't work for integers
A = A + list("ABC")
print(A)

# Convert the integer into the string and add to the list A
A = A + list(str(123))
print(A)

# Add a list having it's own elements, for example: [5, 6, 7, 8]
A = A + [[5, 6, 7, 8]]
print(A[-1]) # [5, 6, 7, 8]

# we can also do the above using append method
A.append([10, 11, 12])
print(A[-1]) # [10, 11, 12]

# but the append method deletes the list if used as follows
A=A.append(10) # When we do A = A.append(10), we're overwriting the list variable A with None so, the type of A becomes None 
print(type(A)) # <class 'NoneType'>
print(A) # None

A=[5,12,72,55,89,1]
# insert 100 between 12 and 72
# A.insert(index,element)
A.insert(2,100)
print(A)

# insert [10,20,30]  in index 2
A.insert(2,[10,20,30])
print(A)

# we don't need to reassign with these list methods

A.remove(12)
print(A)