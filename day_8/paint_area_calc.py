import math
def calculate(height,width,coverage):
    cans=math.ceil((height*width)/coverage)
    print(f"You'll need {cans} cans of paint.")
height=int(input("Height of the wall: "))
width=int(input("Width of the wall: "))
coverage=5
calculate(height,width,coverage)