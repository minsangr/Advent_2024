def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data

file_data = get_file_data("Day04Input.txt")
#print(file_data)

puzzle = []
for row in file_data:
    array = []
    for char in row:
        array.append(char)
    puzzle.append(array)

#print(puzzle)

"""
def horizontalStraight(row):
    count = 0
    for i in range(0, len(row) - 3):
        if row[i] == "X" and row[i + 1] == "M" and row[i + 2] == "A" and row[i + 3] == "S":
            count += 1
    return count

def horizontalReverse(row):
    count = 0
    for i in range(3, len(row)):
        if row[i] == "X" and row[i - 1] == "M" and row[i - 2] == "A" and row[i - 3] == "S":
            count += 1
    return count

def verticalStraight(col):
    count = 0
    for i in range(0, len(col) - 3):
        if col[i] == "X" and col[i + 1] == "M" and col[i + 2] == "A" and col[i + 3] == "S":
            count += 1
    return count

def verticalReverse(col):
    count = 0
    for i in range(3, len(col)):
        if col[i] == "X" and col[i - 1] == "M" and col[i - 2] == "A" and col[i - 3] == "S":
            count += 1
    return count
"""

def diagonalStraightRight(grid):
    for row in range(0, len(grid) - 2):
        for col in range(0, len(grid[row]) - 2):
            if grid[row][col] == "M" and grid[row + 1][col + 1] == "A" and grid[row + 2][col + 2] == "S":
                return True
    return False

def diagonalReverseLeft(grid):
    for row in range(2, len(grid)):
        for col in range(2, len(grid[row])):
            if grid[row][col] == "M" and grid[row - 1][col - 1] == "A" and grid[row - 2][col - 2] == "S":
                return True
    return False

def diagonalStraightLeft(grid):
    for row in range(0, len(grid) - 2):
        for col in range(2, len(grid[row])):
            if grid[row][col] == "M" and grid[row + 1][col - 1] == "A" and grid[row + 2][col - 2] == "S":
                return True
    return False

def diagonalReverseRight(grid):
    for row in range(2, len(grid)):
        for col in range(0, len(grid[row]) - 2):
            if grid[row][col] == "M" and grid[row - 1][col + 1] == "A" and grid[row - 2][col + 2] == "S":
                return True
    return False

def findX(grid):
    if (diagonalStraightRight(grid) or diagonalReverseLeft(grid)) and (diagonalStraightLeft(grid) or diagonalReverseRight(grid)):
        return True
    return False


"""
singleRow = get_file_data("singleRowTest.txt")
print(singleRow)
print(horizontalStraight(singleRow[0]))

singleRow2 = get_file_data("singleRowTest2.txt")
print(singleRow2)
print(horizontalReverse(singleRow2[0]))

singleCol = get_file_data("singleColTest.txt")
print(singleCol)
print(verticalStraight(singleCol))

singleCol2 = get_file_data("singleColTest2.txt")
print(singleCol2)
print(verticalReverse(singleCol2))

quadCol = get_file_data("quadColTest.txt")
print(quadCol)
print(diagonalStraightRight(quadCol))

quadCol2 = get_file_data("quadColTest2.txt")
print(quadCol2)
print(diagonalReverseLeft(quadCol2))

quadCol3 = get_file_data("quadColTest3.txt")
print(quadCol3)
print(diagonalStraightLeft(quadCol3))

quadCol4 = get_file_data("quadColTest4.txt")
print(quadCol4)
print(diagonalReverseRight(quadCol4))

for row in file_data:
    sum += horizontalStraight(row)
    sum += horizontalReverse(row)

for i in range(0, len(file_data)):
    col = [row[i] for row in file_data]
    sum += verticalStraight(col)
    sum += verticalReverse(col)
"""

print(puzzle)

sum = 0
for row in range(0, len(puzzle) - 2):
    for col in range(0, len(puzzle[row]) - 2):
        print([row[col:col+3] for row in puzzle[row:row+3]])
        if findX([row[col:col+3] for row in puzzle[row:row+3]]):
            sum += 1
print(sum)