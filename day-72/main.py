import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate

# Raed the csv file and store it in a pandas dataframe


df= pd.read_csv('QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)

column_names=df.columns
# print(column_names)

#Checks dimension of dataframe (how many rows and column there are)
rows_and_column_count=df.shape
# print(rows_and_column_count)

# counts the number of entries in each column
count=df.count()
# print(count)

# Analysis by Programming Language
 #Calculate the total number of post per language
tag_count=df.groupby('TAG').sum()

# Gives how many month of entries exist per language
max_tag_mentioned=df.groupby('TAG').max()
# print(tag_count)

# Working with Time Stamps
#Coverts the entire column
df.DATE=pd.to_datetime(df.DATE)
# print(df.head())

# pivots the df DataFrame so that each row is a date and each column is a programming language
reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')

# substitutes the number 0 for each NaN value in the DataFrame
reshaped_df.fillna(0, inplace=True)
print(tabulate(reshaped_df, headers='keys'))

# checks if there are any NaN values left in the entire DataFrame
print(reshaped_df.isna().values.any())

# Data Visualisation with Matplotlib

# The window is number of observations that are averaged
roll_df = reshaped_df.rolling(window=6).mean()
# plt.figure(figsize=(16,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

#Labels
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)

# 0 lower bound
plt.ylim(0, 35000)
for column in reshaped_df.columns:
    plt.plot(reshaped_df.index, reshaped_df[column],linewidth=3,label=reshaped_df[column].name)
plt.legend(fontsize=7)
plt.show()