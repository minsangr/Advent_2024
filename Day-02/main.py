def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data


file_data = get_file_data("Day02Input.txt")
# you now have a list of Strings from the input file

print(file_data)

splitted = []
for i in file_data:
    splitted.append(i.split(" "))
print(splitted)

diff = []
for array in splitted:
    miniDiff = []
    for index in range(0, len(array) - 1):
        miniDiff.append(int(array[index]) - int(array[index + 1]))
    diff.append(miniDiff)
print(diff)

safe = 0
for array in diff:
    valid = True
    if array[0] > 0:
        pos = True
    else:
        pos = False
    for i in array:
        if not valid:
            break
        if abs(i) < 1 or abs(i) > 3:
            valid = False
        if pos and i < 0:
            valid = False
        if not pos and i > 0:
            valid = False
    if valid:
        safe += 1

print(safe)
