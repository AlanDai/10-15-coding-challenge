import csv
import sys

def calcSmallestSpread(fname, colName1, colName2, goalColName):
    with open(fname, 'rb') as data:
        table  = csv.reader(data)
        
        # find header row and the indexes of the specified columns
        col1Index = col2Index = headerRow = None
        for i, row in enumerate(table):
            if not row: continue
            row = row[0]
            if row.find(colName1) != -1 and row.find(colName2) != -1 and row.find(goalColName) != -1:
                col1Index, col2Index, goalIndex, headerRow = row.find(colName1), row.find(colName2), row.find(goalColName), i
                break

        # error #1: any of the specified columns not found
        if col1Index == None or col2Index == None or goalIndex == None:
            print('The table does not have all three of the headers %s, %s and %s' %(colName1, colName2, goalColName))
            return

        # check through table rows for the values in the same index range as the specified columns
        minRowLen = max(col1Index + len(colName1), col2Index + len(colName2), goalIndex + len(goalColName))
        goalValue, smallestDiff = '', float("inf")
        for row in table:
            if not row: continue
            row = row[0]

            # error #2: row not long enough to contain both specified columns
            if len(row) < minRowLen: continue

            # error #3: no space separation for cell - case for both start and end indexed
            if row[col1Index - 1] != ' ' and row[col1Index + len(colName1)] != ' ': continue
            if row[col2Index - 1] != ' ' and row[col2Index + len(colName2)] != ' ': continue

            # start indexed
            if row[col1Index - 1] == ' ' and row[col1Index] != ' ':
                item1 = row[col1Index:].split(' ')[0]
                item2 = row[col2Index:].split(' ')[0]
                curGoalColValue = row[goalIndex:].split(' ')[0]
            # end indexed
            else:
                item1 = row[:col1Index + len(colName1)].split(' ')[-1]
                item2 = row[:col2Index + len(colName2)].split(' ')[-1]
                curGoalColValue = row[:goalIndex + len(goalColName)].split(' ')[-1]

            # error #4: the value in the cell is not a digit
            if not item1.isdigit() or not item2.isdigit(): continue

            diff = abs(int(item1) - int(item2))
            if smallestDiff > diff:
                smallestDiff, goalValue = diff, curGoalColValue
    
        # error #5: every row hit an error (#2, #3, and #4) such that no diff can be computed
        if not goalValue:
            print('There were no suitable values to compare in the two headers (%s and %s) such that a minimum difference could be found' (colName1, colName2))
        else:
            print(goalValue)
        
        return

if __name__ == '__main__':
    args = sys.argv
    globals()[args[1]](*args[2:])