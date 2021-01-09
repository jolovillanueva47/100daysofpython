#Rock Paper Scissors
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
player_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
choices=[rock,paper,scissors]
you=choices[player_choice]
computer_choice=random.randint(0,2)
computer=choices[computer_choice]
print(you)
print("Computer chose: ")
print(computer)

player_wins="You Win"
player_lose="You Lose"
player_draw="It's a Draw"

if player_choice == 0 and computer_choice == 1:
    print(player_lose)
elif player_choice == 0 and computer_choice == 2:
    print(player_wins)
elif player_choice == 1 and computer_choice == 0:
    print(player_wins)
elif player_choice == 1 and computer_choice == 2:
    print(player_lose)
elif player_choice == 2 and computer_choice == 0:
    print(player_lose)
elif player_choice == 2 and computer_choice == 1:
    print(player_wins)
else:
    print(player_draw)
