import random
from random import randint

# Split string method
names_string = input("^""Give me everybody's names, separated by a comma\\.")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
limiter_random = len(names)-1
lucky_one = random.randrange(0, limiter_random)
print( "", names[lucky_one],"is going to buy the meal today!$")
