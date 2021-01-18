from art import logo

def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}
def calculator():
    print(logo)
    num1=float(input("What's the first number: "))
    for operation in operations:
        print(operation)
    operation_symbol=input("Pick an operation from the line above: ")
    num2=float(input("What's the second number: "))
    operation=operations[operation_symbol]
    first_answer=operation(num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {first_answer}")

    continue_calculating=True
    while continue_calculating:
        choice=input(f"Type 'y' to continue calculating with {first_answer}, type 'n' to start a new calculation or any other letter if you want to exit: ")
        if choice=="y":
            operation_symbol=input("Pick another operation: ")
            num3=float(input("What's the next number: "))
            operation=operations[operation_symbol]
            second_answer=operation(first_answer,num3)
            print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
            first_answer=second_answer
        elif choice=="n":
            continue_calculating=False
            calculator()
        else:
            continue_calculating=False

calculator()