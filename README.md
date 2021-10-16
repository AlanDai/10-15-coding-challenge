Developer Challenge
1. In the attached file (w_data.dat), you’ll find daily weather data. Download this text file, then write a program to output the day number (column one) with the smallest temperature spread (the maximum temperature is the second column, the minimum the third column).
2. The attached soccer.dat file contains the results from the English Premier League. The columns labeled ‘F’ and ‘A’ contain the total number of goals scored for and against each team in that season (so Arsenal scored 79 goals against opponents, and had 36 goals scored against them). Write a program to print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

Side goals:
1. No hard coding - make the solution as robust as possible
2. Relate the two solutions

Solution Specs:
1. Inputs:
  - fname - a string with the name of the file inputted; will accept any file type (.dat included) that Python's built in csv library can parse
  - col_name_1, col_name_2 - two strings that are the headers of the two columns that are compared
  - goal_col_name - a string that represents the header of the column to be returned
  * Example: fname is soccer.dat, col_name_1 and col_name_2 are 'F' and 'A', and goal_col_name is 'Team'

2. Output:
  - if error -> None paired with a print statement explaining the error
  - else -> the value in goal_col_name col in the the row with the minimum difference between the values in its compared columns (with headers col_name_1 and col_name_2)

3. Input formatting requirements:
  - column indexes need to correspond to header indexes - format alignment matters
  - columns need to be separated by spaces
  - values in compared columns do not need to be digits and may be optional but at least one set of two digits are needed to compute a minimum difference
  - table cells can either be start or end indexed (i.e. begin at the beginning index of the header or end at the ending index of the header)
  
4. Usage would look like calling `python solution.py calc_smallest_spread {fname} {colName1} {colName2} {goalColName}`
  - Running `python solution.py calc_smallest_spread 'soccer.dat' 'F' 'A' 'Team'` returns `Aston_villa`
  - Running `python solution.py calc_smallest_spread 'w_data.dat' 'MxT' 'MnT' 'Dy'` returns `14`

5. Potential sources of expansion:
  - can add a comparator function to change how the col_name_1 and col_name_2 values are compared to determine which row to select
  - better error handling
