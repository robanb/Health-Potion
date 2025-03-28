import random
health = 50
difficulty = 3
#   1. Using the random module, generate a random integer between 25 and 50 and save it to a variable called potion_health
 #   int() is used to convert the float value to integer
 #   randint() is used to generate random integer value between the given range (a, b)

potion_health = int(random.randint(25,50) / difficulty)

#   2. Add potion_health to health and print the result.
health += potion_health

#   3. Print the value of health
print(health)
#   4. Now, change difficulty to see how it affects the health value.
