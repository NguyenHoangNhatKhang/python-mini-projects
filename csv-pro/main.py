# # import csv 
# # with open("weather_data.csv") as csv_file:
# #     data = csv.reader(csv_file)
# #     temperature = []
# #     day,temp,condition = 0,1,2
# #     for index,row in enumerate(data):
# #         if row[temp] == "temp":
# #             pass
# #         else:
# #             temperature.append(int(row[temp]))
# #     print(temperature)

import pandas 
# data = pandas.read_csv("weather_data.csv")
# # print(type(data))
# # print(data["temp"])
# # data_dict = data.to_dict()
# # temp_list = data["temp"].to_list()

# # print(data["temp"].mean())
# # # print(data["temp"].max())
# # # #có thể dùng 
# # print(data.temp)
# # #cách lấy row  
# print(data[data.temp==data.temp.max()])
# monday = data[data.day == "Monday"]
# farentheit = int(monday.temp.iloc[0])*9/5 +32
# print(farentheit)

data_dict = {
    "students": ["Amy","James","Angela"],
    "scores": [76,56,65]
}

data = pandas.DataFrame(data_dict)
