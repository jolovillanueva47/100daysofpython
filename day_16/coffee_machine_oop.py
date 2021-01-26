from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker=CoffeeMaker()
money_machine=MoneyMachine()
coffee_menu=Menu()
coffeemachine_is_on=True
while coffeemachine_is_on:
    choice=input("What would you like? "+coffee_menu.get_items()+":​ ")
    sufficient_resources=True
    if choice=="off":
         coffeemachine_is_on=False
    elif choice=="report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink=coffee_menu.find_drink(choice)
        if drink != None:
            sufficient_resources=coffee_maker.is_resource_sufficient(drink)
            if sufficient_resources == True:
                money_machine.make_payment(drink.cost)
                coffee_maker.make_coffee(drink)

