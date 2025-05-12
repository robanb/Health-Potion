# Tuples are similiar to list but are immutable data type
# Tuples cab be used to protect the pieces of data 

our_tuple = 1,2,3, "A", "B", "C" 
# usually we use () --> our_tuple = (1,2,3, "A", "B", "C" )
print(type(our_tuple))


# Tuples are iterable data types and are consists of elements
print(our_tuple[0:3])

# List can be changed after defining but the tuples can't be changed after defining
#Example: list
our_list = [1,2,3,4,5,6,7]
our_list[2] = 100
print(our_list)

# Example: tuples
# our_tuple[2] = 100 
# print(our_tuple) 
# TypeError: 'tuple' object does not support item assignment


# convert other data to Tuple using tuple function : tuple()
A = [1,2,3]
print(type(A)) # type: list
A = tuple(A)
print(type(A)) # type: tuple

# multiple assignment, since it is a iterable data type
(A,B,C) = 1,2,3
print(A) # 1
print(B) # 2
print(C) # 3


