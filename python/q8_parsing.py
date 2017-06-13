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

#if not using pandas
# Following functions will be called like this:
#   footballTable = read_data('football.csv')
#   minRow = get_index_with_min_abs_score_difference(footballTable)
#   print str(get_team(minRow, footballTable))




def read_data(filename):
    """Returns a list of lists representing the rows of the csv file data.

    Arguments: filename is the name of a csv file (as a string)
    Returns: list of lists of strings, where every line is split into a list of values. 
        ex: ['Arsenal', 38, 26, 9, 3, 79, 36, 87]
    """
    with open(filename, 'r') as f:
        data = [row for row in csv.reader(f.read().splitlines())]
    return data


def get_index_with_min_abs_score_difference(goals):
    """Returns the index of the team with the smallest difference
    between 'for' and 'against' goals, in terms of absolute value.

    Arguments: parsed_data is a list of lists of cleaned strings
    Returns: integer row index
    """
    goals.pop(0)
    goal = [x[5] for x in goals]
    goal_allowed = [x[6]for x in goals]
    abs_diff = [abs(float(x) - float(y)) for x, y in zip(goal, goal_allowed)]
    return abs_diff.index(min(abs_diff))
    
def get_team(index_value, parsed_data):
    """Returns the team name at a given index.
    
    Arguments: index_value is an integer row index
               parsed_data is the output of `read_data` above
               
    Returns: the team name
    """
    teams = [x[0] for x in parsed_data]
    return teams[index_value]
