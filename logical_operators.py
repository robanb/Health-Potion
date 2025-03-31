# The logical operators combine and modify the conditions to make bigger conditions
#  not  operator: gives the opposite
print(not True) # prints False
print(not 2 == 3)
print(not 3 > 7)

x = 10
y = 20
if not y < x:
    print("not: works!")

# and  operator: True only if all the given conditions are true. eg: if conditin A and condition B are true, then it returns true
a = 12
b = 13
if a < b and b > 1:
    print("and: works!")

# the default is False in a comparision b/n False and True
print(False and True) # False
print(True and True) # True
print(False and False) # False

#not true
if not (a > b and b > 1):
    print("not and : works!")

# or operator: if any of the condition is true, it returns true
a = 12
b = 13
if (a > b or a > 1):
    print("or: works!")

#combining not and or
if not (a > 100 or b > 100):
    print("not or: works!")

# combining if, and, or
C = 6
D = 2
if(C > 5 and D > 5) or (C > 1 and D > 1):
    print("if, and, or : works")


# combining if, and, or, not
C = 6
D = 2
if not(C > 5 and D > 5) or (C > 1 and D > 1):
    print("if, and, or, not : works")