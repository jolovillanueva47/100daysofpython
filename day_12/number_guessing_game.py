from art import logo
from replit import clear
import random

def compare_guess(answer,guess):
    """
    Checks answer to guess then returns a Boolean
    """
    if answer == guess:
        return True
    elif guess > answer:
        print("Too high")
    else:
        print("Too Low")
    return False

def guess_number():
    """
    Guessing Game itself
    """
    if input("Choose a difficulty. Type 'easy' or 'hard': ") == "easy":
        number_of_attempts=10
    else:
        number_of_attempts=5
    random_number=random.randint(1,100)
    correct_guess=False
    while number_of_attempts > 0 and correct_guess==False:
        print(f"You have {number_of_attempts} remaining to guess the number. ")
        guess=int(input("Make a guess: "))
        correct_guess=compare_guess(random_number,guess)
        number_of_attempts-=1
        if number_of_attempts!=0 and correct_guess==False:
            print("Guess Again")
    print(f"\nThe random number is: {random_number}")
    if correct_guess==True:
        print("You guessed the correct number. You Win!\n")
    else:
        print("You used all your attempts and guessed incorrectly. You Lose!\n")

while input("Do you want to play 'Guess the Number' type 'y' for yes or any other letter for no: ") == 'y':
    clear()
    print(logo)
    print("Welcome to the Number Guessing Game")
    print("I'm thinking of a number between 1 and 100")
    guess_number()