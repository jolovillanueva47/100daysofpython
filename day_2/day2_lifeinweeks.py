# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
daysFrom90=365*90
weeksFrom90=52*90
monthsFrom90=12*90

ageInDays=int(age)*365
ageInWeeks=int(age)*52
ageInMonths=int(age)*12

daysOutput = daysFrom90 - ageInDays 
weeksOutput = weeksFrom90 -  ageInWeeks
monthsOutput =  monthsFrom90 - ageInMonths
print(f"You have {daysOutput} days, {weeksOutput} weeks, and {monthsOutput} months left")