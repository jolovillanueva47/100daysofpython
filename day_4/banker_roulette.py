import random
names = input("Enter everybody's names separated by comma: ")
name_list = names.split(',')
num_of_names = len(name_list)-1
person=name_list[random.randint(0,num_of_names)]
print(f"{person} is going to buy the meal today!")
