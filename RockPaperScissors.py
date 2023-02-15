rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
choices = [rock, paper, scissors]

computer_choice = random.randint(0,2)

print(choices[computer_choice])
if user_choice >= 3:
    print("you lose !")
print(choices[user_choice])

if user_choice == computer_choice:
    print("It's a draw")
if user_choice == 0 and computer_choice == 2 or \
     user_choice == 1 and computer_choice == 0 or user_choice == 2 and computer_choice == 1:
    print("you wind!")
else:
    if user_choice == 0 and computer_choice == 1 or user_choice == 1  and  computer_choice == 2 or user_choice == 2 and computer_choice == 0:
      print("Your loose!")



    # Rock wins against scissors.0
    # #Paper wins against rock.1
    # #Scissors win against paper.
