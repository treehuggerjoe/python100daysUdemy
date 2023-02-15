"""find i f number is add or even34

numToCheck=int(input("which number do you want to check?"))
modNumber = numToCheck % 2
if modNumber == 0:
    print(f"the number {numToCheck} is even")
else:
    print(f"the number {numToCheck} is odd")



# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = round((weight/height **2))
if BMI <= 18.5: print(f"Your BMI is {BMI}, you are underweight.")
elif BMI >= 18.5  and BMI <= 25: print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI >= 25 and BMI <= 30: print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI >= 30and BMI <= 35 : print(f"Your BMI is {BMI},  you are obese.")
elif BMI > 35: print(f"Your BMI is {BMI}, you are clinically obese.")

"""

"""
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
# first check if year no remainder then leap
if year % 4 == 0:
    if year % 100 == 0:
        if (year % 400) == 0:

            print("Leap year.")
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
    print("not a leap year.")
"""