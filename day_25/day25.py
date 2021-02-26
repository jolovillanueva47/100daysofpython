#import csv
import pandas
# with open("weather_data.csv") as data:
#     #lines=data.readlines()
#     obj=csv.reader(data)
#     temperatures=[]
#     for row in obj:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#         print(row)
#     print(temperatures)

# print(lines)
# data=pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])
# data_dict=data.to_dict()
# print(data_dict)
# temp_list=data["temp"].to_list()
# print(temp_list)
# print(round(sum(temp_list)/len(temp_list),2))
# print(data["temp"].mean())
# print(data["temp"].max())

# #Get data in columns
# print(data.condition)

#Get data in row
# print(data[data.day=="Monday"])
# print(data[data.temp==data.temp.max()])

# monday=data[data.day=="Monday"]
# print(int(monday.temp)*1.8+32)

# #Create a dataframe from scratch
# data_dict={
#     "students": ["Jolo","Kobe","Lebron"],
#     "scores": [76,65,56]
# }
# grades=pandas.DataFrame(data_dict)
# print(grades)
# grades.to_csv("grades.csv")

