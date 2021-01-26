from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeemaker=CoffeeMaker()
moneymachine=MoneyMachine()
coffeemenu=Menu()
coffeemachine_is_on=True
while coffeemachine_is_on:
    choice=input("What would you like? "+coffeemenu.get_items()+":​ ")
    sufficient_resources=True
    if choice=="off":
         coffeemachine_is_on=False
    elif choice=="report":
        coffeemaker.report()
        moneymachine.report()
    else:
        drink=coffeemenu.find_drink(choice)
        if drink != None:
            sufficient_resources=coffeemaker.is_resource_sufficient(drink)
            if sufficient_resources == True:
                moneymachine.make_payment(drink.cost)
                coffeemaker.make_coffee(drink)

