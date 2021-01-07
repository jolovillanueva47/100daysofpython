print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1_lowered=name1.lower()
name2_lowered=name2.lower()
combined_name=name1_lowered+name2_lowered

count_true=0
count_love=0

count_true+=(combined_name.count('t') + combined_name.count('r') + combined_name.count('u') + combined_name.count('e'))
count_love+=(combined_name.count('l') + combined_name.count('o') + combined_name.count('v') + combined_name.count('e'))

total=str(count_true)+str(count_love)
int_total=int(total)

if  int_total < 10 or int_total > 90:
    print(f"Your score is {int_total}, you go together like coke and mentos.")
elif int_total <= 50 and int_total >= 40:
    print(f"Your score is {int_total}, you are alright together.")
else:
    print(f"Your score is {int_total}.")
