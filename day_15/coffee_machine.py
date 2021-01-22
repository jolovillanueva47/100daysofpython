MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money=0
QUARTERS=0.25
DIMES=0.10
NICKLES=0.05
PENNIES=0.01

def report(resources,money):
    for key,val in resources.items():
        if key=="coffee":
            print(key.title()+": "+str(val)+"g")
        else:
            print(key.title()+": "+str(val)+"ml")
    print(f"Money: ${money}")

def check_sufficiency(resources,choice):
    water_resource=resources["water"]
    coffee_resource=resources["coffee"]
    water_ingredient=MENU[choice]["ingredients"]["water"]
    coffee_ingredient=MENU[choice]["ingredients"]["coffee"]
    sufficiency=True
    if water_resource - water_ingredient < 0:
        print("Sorry there is not enough water.")
        sufficiency=False
    if  coffee_resource - coffee_ingredient < 0:
        print("Sorry there is not enough coffee.")
        sufficiency=False
    if choice!="espresso":
        milk_resource=resources["milk"]
        milk_ingredient=MENU[choice]["ingredients"]["milk"]
        if milk_resource - milk_ingredient < 0:
            print("Sorry there is not enough milk.")
            sufficiency=False
    return sufficiency

def process_coins(total_coins,choice,money):
    coffee_cost=MENU[choice]["cost"]
    if total_coins < coffee_cost:
        print("Sorry that's not enough money🪙. Money refunded.")
        return False
    else:
        if total_coins == coffee_cost:
            print("You paid the exact amount. Thank you")
        else:
            change=round(total_coins-coffee_cost,2)
            print(f"\nHere is the ${change} change.")
        return True

def deduct_resources(resources,choice):
    resources["water"]=resources["water"]-MENU[choice]["ingredients"]["water"]
    resources["coffee"]=resources["coffee"]-MENU[choice]["ingredients"]["coffee"]
    if choice!="espresso":
        resources["milk"]=resources["milk"]-MENU[choice]["ingredients"]["milk"]

coffee_is_on=True
while coffee_is_on:
    choice=input("What would you like? (espresso/latte/cappuccino):​ ")
    sufficient_coins=True
    sufficient_resources=True
    if choice=="off":
         coffee_is_on=False
    elif choice=="report":
        report(resources,money)
    else:
        sufficient_resources=check_sufficiency(resources,choice)
        if sufficient_resources == True:
            print("Please insert coins.")
            quarters_inserted=int(input("How many quarters?: "))*QUARTERS
            dimes_inserted=int(input("How many dimes?: "))*DIMES
            nickels_inserted=int(input("How many nickles?: "))*NICKLES
            pennies_inserted=int(input("How many pennies: "))*PENNIES
            total_coins=quarters_inserted+dimes_inserted+nickels_inserted+pennies_inserted
            sufficient_coins=process_coins(total_coins,choice,money)
            if sufficient_coins == True:
                money+=MENU[choice]["cost"]
                deduct_resources(resources,choice)
                print(f"Here is your {choice} ☕. Enjoy!")


