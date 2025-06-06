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

game_images = [rock,paper,scissors]

user_choice = int(input("What's your choise ?\n"
                        "Rock = 0\n" \
                        "Paper = 1\n" \
                        "Scissor= 2\n"))
if user_choice >= 0 and user_choice <= 2 :
    print(game_images[user_choice])

computer_choice = random.randint(0,2)
print("Computer Choice : ")
print(game_images[computer_choice])

if user_choice >=3 and user_choice < 0:
    print(" Enter a Valid Number !")
elif computer_choice == 2 and user_choice == 0 :
    print(" You Win!\n")
    
elif user_choice == 2 and computer_choice == 0:
    print("you lose!")

elif user_choice > computer_choice:
    print("You Win!\n")

elif computer_choice > user_choice :
    print("You Lose!")

elif computer_choice == user_choice :
    print("It's a Draw!")