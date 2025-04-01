# Lists are used to store multiple items in a single variable and it has interabel data type as well
our_list = [1, 2, 3, 4, 5]
print(our_list)
print(type(our_list))

# A list in python can have more than 1 data type and we can iternate to check that
items = ["There", "are", 4, "directions", "and", "that's", "universally", True ]
print(items[:3])
print(type(items[2]))

# A list can have other lists inside it
our_list = [1, 2, [3, 4, 5], 6, 7, 8]
print(our_list[2])

# To get the index of a small list inside another big list: list[index_of_big_list][index_of_small_list]. This is useful when creating a table
print(our_list[2][0]) #3
print(our_list[2][1]) #4
print(our_list[2][2]) #5
print(our_list[2][1:]) #4, 5
print(our_list[2][0::2]) #3, 5  --> o to 2 means from index 0 to end in steps of 2. 

# creating a table
our_table = [[1,2,3], [4,5,6], [7,8,9]]
print(our_table[0])
print(our_table[1])
print(our_table[2])

# get 2 coordinates: our_table[row][colunm]
print(our_table[0][2]) # 3
print(our_table[1][2]) # 6
print(our_table[2][2]) # 9
print(our_table[1][1:]) # [5,6]




