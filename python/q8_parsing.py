# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import pandas as pd
#Read football.csv into a pandas dataframes
df = pd.read_csv('https://raw.githubusercontent.com/AngieLiang/dsp/c93e9ed0e0850adb6215b8b09c367447cd046645/python/football.csv')
#Create a new column with goal difference
df['Difference'] = df['Goals'] - df['Goals Allowed']
#Find the index with smallest goal difference
small_diff = df['Difference'].abs().idxmin()
#identify the team with smallest goal difference, which is Aston Villa
print(df.iloc[small_diff])
