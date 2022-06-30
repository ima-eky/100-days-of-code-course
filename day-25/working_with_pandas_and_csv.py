# Generates data from weather_data.csv file
# using file methods
with open('weather_data.csv') as read_file:
    data = read_file.readlines()
    print(data)

# using csv library
import csv
with open('weather_data.csv') as data_file:
    data=csv.reader(data_file)
    temperatures=[]
    for row in data:
        if row[1] != 'temp':
            temperature=int(row[1])
            temperatures.append(temperature)
    print(temperatures)

# using the pandas library
import pandas
data=pandas.read_csv("weather_data.csv")

print(type(data))
print(type(data['temp']))

data_to_dict= data.to_dict()
print(data_to_dict)

data_to_list= data['temp'].to_list()
print(len(data_to_list))

data['temp'].mean()
data['temp'].max()

# Get data in columns
print(data.condition)
print(data['condition'])

# Get data in row
print(data[data.day =='Monday'] )
print(data[data.temp == data.temp.max()])

# Get row data value

monday=data[data.day == 'Monday']
temperature=int(monday.temp)
temperature= temperature *9/5 +32
print(temperature)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data=pandas.DataFrame(data_dict)
data.to_csv('new_file.csv')

#Central Park Squirrel Data Analysis

data_1= pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
squirrel_color=data_1["Primary Fur Color"]
gray_squirrels_count=len(data_1[squirrel_color == 'Gray'])
red_squirrels_count=len(data_1[squirrel_color == 'Cinnamon'])
black_squirrels_count=len(data_1[squirrel_color == 'Black'])


new_dict={
    'Fur color':['Gray','Black','Red'],
    'Count': [gray_squirrels_count,black_squirrels_count,red_squirrels_count]
}

new_data = pandas.DataFrame(new_dict)
new_data.to_csv("squirrel_count.csv")