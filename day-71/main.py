import pandas as pd
pd.options.display.float_format = '{:,.2f}'.format


# Reads csv file with pandas library
df=pd.read_csv('salaries_by_college_major.csv')

#Gets the 1st 5 records
first_five_records = df.head()

#Gets the last 5 records
last_five_records=df.tail()
# print(last_five_records)

# Counts the number of rows, columns in dataframe
count=df.shape
print(f'There are {count[0]} rows and {count[1]} columns in this dataframe')
print('')

# Access  column names
name_of_columns=df.columns
print(f'The names of all the columns present are:')
print(f'{name_of_columns}')
print('')

# Check for missing value or junk data
invalid_cells=df.isna()
# print(invalid_cells)

# Created a new dataframe without the last row
clean_df = df.dropna()
print(f'These are the last five records of the new dataframe:')
print(clean_df.tail())

#Accessing particular column
starting_median_salary=clean_df['Starting Median Salary']
print(f'The maximum starting median salary recorded is ${starting_median_salary.max()}')

# .idxmax() method will give us index for the row with the largest value.
index_of_major=clean_df['Starting Median Salary'].idxmax()

# You can use the .loc property to retrieve an entire row(without specify the particular column)
name_of_major=clean_df['Undergraduate Major'].loc[index_of_major]
print(f'The name of major with the largest starting median salary is {name_of_major}')

# The Highest Mid-Career Salary
max_mid_career_salary_index =clean_df['Mid-Career Median Salary'].idxmax()
name_of_major=clean_df['Undergraduate Major'].loc[max_mid_career_salary_index]
print('')
print(f'The name of major with the highest mid-career median  salary is {name_of_major}')


# The Lowest Starting Salary
min_starting_career_salary_index =clean_df['Starting Median Salary'].idxmin()
name_of_major=clean_df['Undergraduate Major'].loc[min_starting_career_salary_index]
print('')
print(f'The name of major with the lowest starting median salary is {name_of_major}')
print('')


# The Lowest Mid-Career Salary
min_mid_career_salary_index =clean_df['Mid-Career Median Salary'].idxmin()
name_of_major=clean_df['Undergraduate Major'].loc[min_mid_career_salary_index]
print('')
print(f'The name of major with the lowest mid-career median salary is {name_of_major}')
print('')


# Difference in Earnings
difference=clean_df['Mid-Career 90th Percentile Salary'].subtract(clean_df['Mid-Career 10th Percentile Salary'])

#Inserting a new column in dataframe
clean_df.insert(1,'Spread',difference)
clean_df.head()
# print(clean_df.head())

# Sorting by the Lowest Spread
low_risk = clean_df.sort_values('Spread')
# print(low_risk[['Undergraduate Major', 'Spread']].head())

# Majors with the Highest Potential
highest_potential = clean_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)
# print(highest_potential[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head())

#Majors with the Greatest Spread in Salaries
highest_spread = clean_df.sort_values('Spread', ascending=False)
print(f"5 majors with the highest spread in salaries:\n{highest_spread[['Undergraduate Major', 'Spread']].head()}")

# highest_spread = clean_df.sort_values('Mid-Career Median Salary', ascending=False)
# print(highest_spread[['Undergraduate Major', 'Mid-Career Median Salary']].head())

# grouping  data by category
print('')
print(f"An overview of how many majors there are in each category:\n{clean_df.groupby('Group').count()}")
print(f"The average salary by group:\n {clean_df.groupby('Group').mean()}")



