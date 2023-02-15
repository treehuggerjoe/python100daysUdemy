# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1= input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
conbine_name = name1 + name2
true_Count = 0
love_Count = 0
true_Count = conbine_name.count("t")
true_Count += conbine_name.count("r")
true_Count += conbine_name.count("u")
true_Count += conbine_name.count("e")

love_Count += conbine_name.count("l")
love_Count += conbine_name.count("o")
love_Count += conbine_name.count("v")
love_Count += conbine_name.count("e")
final_love_score = {str(true_Count) + str(love_Count)}
final_love_score = ( true_Count * 10) + love_Count
if int(final_love_score) < 10 or int(final_love_score) > 90:
    print(f"Your score is  {str(true_Count) + str(love_Count)}, you go together like coke and mentos.")
elif final_love_score > 40 and final_love_score < 50:
    print(f"Your score is  {str(true_Count) + str(love_Count)}, you are alright together.")
else:  print(f"Your score is  {str(true_Count) + str(love_Count)} ")

