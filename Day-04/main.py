def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data

file_data = get_file_data("Day04Input.txt")
print(file_data)

puzzle = []
for row in file_data:
    array = []
    for char in row:
        array.append(char)
    puzzle.append(array)

print(puzzle)

def horizontalStraight(row):
    count = 0
    for i in range(0, len(row) - 3):
        if row[i] == "X" and row[i + 1] == "M" and row[i + 2] == "A" and row[i + 3] == "S":
            count += 1
    return count

def horizontalReverse(row):
    count = 0
    for i in range(3, len(row)):
        if row[i] == "S" and row[i - 1] == "A" and row[i - 2] == "M" and row[i - 3] == "X":
            count += 1
    return count

singleRow = get_file_data("singleRowTest.txt")
print(singleRow)
print(horizontalStraight(singleRow[0]))

singleRow2 = get_file_data("singleRowTest2.txt")
print(singleRow2)
print(horizontalReverse(singleRow2[0]))
