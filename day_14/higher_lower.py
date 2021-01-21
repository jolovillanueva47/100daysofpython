import random
from art import logo,vs
from game_data import data
from replit import clear

def random_account():
    """
    Generate a random account from game data
    """
    num_of_elements=len(data)-1
    return data[random.randint(0,num_of_elements)]


def format_data(acct_data):
    """
    Format account data into printable format
    """
    name=acct_data["name"]
    follower_count=acct_data["follower_count"]
    description=acct_data["description"]
    country=acct_data["country"]
    return f"{name}, {description}, from {country}"

def get_higher_acct(a_acct,b_acct):
    """
    Check data with higher follower account then return it
    """
    if a_acct["follower_count"] > b_acct ["follower_count"]:
        return "A"
    elif a_acct["follower_count"] == b_acct ["follower_count"]:
        return "A"
    else:
        return "B"

def game():
    comparison_dict={}
    score=0
    comparison_dict["A"]=random_account()
    a_acct_formatted=format_data(comparison_dict["A"])
    a_follower_count=comparison_dict["A"]["follower_count"]
    game_not_over=True
    print(logo)
    while game_not_over:
        comparison_dict["B"]=random_account()
        b_acct_formatted=format_data(comparison_dict["B"])
        b_follower_count=comparison_dict["B"]["follower_count"]
        print(f"Compare A: {a_acct_formatted}")
        print(vs)
        print(f"Against B: {b_acct_formatted}")
        guess=input("Who has more followers?: Type 'A' or 'B': ")
        higher_acct=get_higher_acct(comparison_dict["A"],comparison_dict["B"])
        if guess==higher_acct:
            clear()
            print(logo)
            score+=1
            print(f"You right! Current score: {score}")
            comparison_dict["A"]=comparison_dict[higher_acct]
            a_acct_formatted=format_data(comparison_dict["A"])
            a_follower_count=comparison_dict["A"]["follower_count"]
        else:
            clear()
            print(logo)
            print(f"Sorry that's wrong: Final score: {score}")
            game_not_over=False

game()