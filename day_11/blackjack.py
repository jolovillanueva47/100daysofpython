from art import logo
from replit import clear
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
wanna_play=False
user_score=0
computer_score=0

def deal_card():
    """
    Deal a random card
    """
    return random.choice(cards)

def calculate_score(list_of_cards):
    """
    Return the sum of a list of cards
    """
    score=0
    if  sum(list_of_cards) == 21 and len(list_of_cards)== 2:
        return score
    elif sum(list_of_cards) >21 and 11 in list_of_cards:
        list_of_cards.remove(11)
        list_of_cards.append(1)
    score=sum(list_of_cards)
    return score

def compare(user_score,computer_score):
    if user_score==0:
        print("You win with a Blackjack!")
    elif computer_score==0:
        print("You lose the opponent has a Blackjack")
    elif user_score==computer_score:
        print("It's a draw")
    elif user_score > 21:
        print("Your score went over.You lose")
    elif computer_score > 21:
        print("Opponent went over.You win!")
    else:
        if user_score > computer_score:
            print("You win!")
        else:
            print("You lose")

def play_blackjack():
    user_cards=[]
    computer_cards=[]
    for _ in range(2):  
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    is_game_not_over=True
    print(logo)
    while is_game_not_over:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_not_over=False
        else:
            if input("Type 'y' to get another card, type 'n' to pass: ") != 'y':
                is_game_not_over=False
            else:
                user_cards.append(deal_card())
        while computer_score  !=0 and computer_score<17:
            computer_cards.append(deal_card())
            computer_score=calculate_score(computer_cards)
    print(f"\nYour final hand: {user_cards}, final score {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    compare(user_score,computer_score)

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")=="y":
    clear()
    play_blackjack()
