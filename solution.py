import csv
import sys

def calc_smallest_spread(fname, col_name_1, col_name_2, goal_col_name):
    with open(fname, 'rb') as data:
        table  = filter(lambda row: len(row) > 0, csv.reader(data))
        # find header row and the indexes of the specified columns
        col_index_1 = col_index_2 = None
        for row in table:
            row = row[0]
            if (row.find(col_name_1) != -1 and row.find(col_name_2) != -1 and
                row.find(goal_col_name) != -1):
                col_index_1 = row.find(col_name_1)
                col_index_2 = row.find(col_name_2)
                goal_index = row.find(goal_col_name)
                break
        if col_index_1 is None or col_index_2 is None or goal_index is None:
            print('The table does not have all three of the inputted headers')
            return None
        # check rows for the values that overlap the index of the specified column headers
        min_row_len = max(col_index_1 + len(col_name_1) + 1,
            col_index_2 + len(col_name_2) + 1,
            goal_index + len(goal_col_name) + 1)
        goal_val, smallest_diff = '', float("inf")
        for row in table:
            row = row[0]
            if len(row) < min_row_len:
                continue
            # error: no space separation for cell - case for both start and end indexed
            if ((row[col_index_1 - 1] != ' ' and row[col_index_1 + len(col_name_1)] != ' ') or
                (row[col_index_2 - 1] != ' ' and row[col_index_2 + len(col_name_2)] != ' ')):
                continue
            # start indexed - e.g. soccer.dat
            if row[col_index_1 - 1] == ' ' and row[col_index_1] != ' ':
                item1 = row[col_index_1:].split(' ')[0]
                item2 = row[col_index_2:].split(' ')[0]
                cur_goal_val = row[goal_index:].split(' ')[0]
            # end indexed - e.g. w_data.dat
            else:
                item1 = row[:col_index_1 + len(col_name_1)].split(' ')[-1]
                item2 = row[:col_index_2 + len(col_name_2)].split(' ')[-1]
                cur_goal_val = row[:goal_index + len(goal_col_name)].split(' ')[-1]
            if not item1.isdigit() or not item2.isdigit():
                continue
            diff = abs(int(item1) - int(item2))
            if smallest_diff > diff:
                smallest_diff, goal_val = diff, cur_goal_val
        if not goal_val:
            print('There were no suitable values to compare')
        print(goal_val)
        return goal_val

if __name__ == '__main__':
    args = sys.argv
    globals()[args[1]](*args[2:])
