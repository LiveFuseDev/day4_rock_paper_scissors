import random

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

rps_list = [rock, paper, scissors]

user_choice = int(input("Let's play rock, paper, scissors. Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# Validate input using if-elif-else structure
if user_choice >= 0 and user_choice <= 2:
    computer_choice = random.randint(0, 2)  # Picks 0, 1, or 2 randomly

    print(f"You chose:\n{rps_list[user_choice]}")
    print(f"The computer chose:\n{rps_list[computer_choice]}")

    # Game logic
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("You lose!")
else:
    print("Invalid number. You lose.")