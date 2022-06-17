# #Generates data from weather_data.csv file as a list of all the values
# with open('weather_data.csv') as read_file:
#     data=read_file.readlines()

import csv
with open('weather_data.csv') as data_file:
    data=csv.reader(data_file)
    temperatures=[]
    for row in data:
        temperature=int(row[1])
        temperatures.append(temperature)
    print(temperatures)
