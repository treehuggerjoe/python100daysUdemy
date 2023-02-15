import random
# from random import
#
# # Split string method
# names_string = input("Give me everybody's names, separated by a comma\\.")
# names = names_string.split(", ")
# # 🚨 Don't change the code above 👆
#
# #Write your code below this line 👇
# limiter_random = len(names)
# lucky_one = random.randrange(0, limiter_random)
# print( names[lucky_one],"is going to buy the meal today!$")
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)
print(dirty_dozen[1][2])
print(dirty_dozen[1][3])

print(dirty_dozen[0])
print(dirty_dozen[1])

print(dirty_dozen[1][1])
