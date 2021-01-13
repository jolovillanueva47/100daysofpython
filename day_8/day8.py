def greet():
    print("Hello")
    print("Hi")
    print("How are you")

greet()

#Functions that allows for input
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}")

greet_with_name("Jolo")
#Functions with more than 1 input
def greet_with(name="Kobe",location="Los Angeles"):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with("Jolo","Manila")
greet_with()
greet_with(location="Oakland",name="Steph")