import random

# LETS DRAW!!!! WHAT?

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


game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type '0' for Rock, '1' for Paper or '2' for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0,2)
print(computer_choice)
print(game_images[computer_choice])

# AND - BOTH NEED TO BE TRUE
# OR - ONLY ONE OR TWO NEEDS TO BE TRUE

# So here, this conditional in the if statement is TRUE is at least one of the statements are true (user_choice >= 3) OR (user_choice < 0)
if user_choice >= 3 or user_choice < 0: 
    print("You typed an invalid number, you lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You Win!")
elif computer_choice == 0 and user_choice == 2:
    print("You Lose!")
elif computer_choice > user_choice:
    print("You Lose")
elif user_choice > computer_choice:
  print("You win!")
elif user_choice == computer_choice:
  print("You tied!")
