def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data

def difference(file_name):
    diff = []
    for array in file_name:
        miniDiff = []
        for index in range(0, len(array) - 1):
            miniDiff.append(int(array[index]) - int(array[index + 1]))
        diff.append(miniDiff)
    return diff

def validity(num, sign):
    if abs(num) < 1 or abs(num) > 3:
        return False
    if sign:
        if num < 0:
            return False
    else:
        if num > 0:
            return False
    return True

def evalSign(array):
    count = 0
    for i in array:
        if i > 0:
            count += 1
        else:
            count -= 1
    if count < 0:
        return False
    return True

file_data = get_file_data("Day02Input.txt")
# you now have a list of Strings from the input file

print(file_data)

splitted = []
for i in file_data:
    splitted.append(i.split(" "))
print(splitted)

diff = difference(splitted)

print(diff)

safe = 0
unsafe = []
for array in diff:
    valid = True
    sign = evalSign(array)
    for i in array:
        if not valid:
            break
        if not validity(i, sign):
            valid = False
    if valid:
        safe += 1
    else:
        unsafe.append(array)
print(safe)
print(unsafe)
