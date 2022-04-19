
player_choice = input("Enter rock, paper or scissors ")
# print(f"You chose {player_choice}")


import random

computer = ["rock", "paper", "scissors"]
i= (random.randrange(len(computer)))
computer_choice = computer[i]
# print(f"The computer chose {computer_choice}")
# print(f"{computer[i]}")

if player_choice == "rock" and computer_choice == "rock":
    print(f"You chose {player_choice}")
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
    print(f"The computer chose {computer_choice}")
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
    print("Draw!")
elif player_choice == "rock" and computer_choice == "paper":
    print(f"You chose {player_choice}")
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
    print(f"The computer chose {computer_choice}")
    print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
    print("Computer Wins!")
if player_choice == "rock" and computer_choice == "scissors":
    print(f"You chose {player_choice}")
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
    print(f"The computer chose {computer_choice}")
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
    print("Player Wins!")
if player_choice == "paper" and computer_choice == "rock":
    print(f"You chose {player_choice}")
    print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
    print(f"The computer chose {computer_choice}")
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
    print("Player Wins!")
if player_choice == "paper" and computer_choice == "paper":
    print(f"You chose {player_choice}")
    print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
    print(f"The computer chose {computer_choice}")
    print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
    print("Draw!")
if player_choice == "paper" and computer_choice == "scissors":
    print(f"You chose {player_choice}")
    print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
    print(f"The computer chose {computer_choice}")
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
    print("Computer Wins")
if player_choice == "scissors" and computer_choice == "rock":
    print(f"You chose {player_choice}")
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
    print(f"The computer chose {computer_choice}")
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
    print("Computer Wins!")
elif player_choice == "scissors" and computer_choice == "paper":
    print(f"You chose {player_choice}")
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
    print(f"The computer chose {computer_choice}")
    print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
    print("Player Wins!")
if player_choice == "scissors" and computer_choice == "scissors":
    print(f"You chose {player_choice}")
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
    print(f"The computer chose {computer_choice}")
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
    print("Draw!")