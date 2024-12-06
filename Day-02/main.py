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

def checkNum(num, sign):
    if abs(num) < 1 or abs(num) > 3:
        return False
    if sign:
        if num < 0:
            return False
    else:
        if num > 0:
            return False
    return True

def checkArray(array):
    valid = True
    sign = evalSign(array)
    for i in array:
        if not valid:
            break
        if not checkNum(i, sign):
            valid = False
    if valid:
        return True
    return False

def getInvalidIndex(array):
    sign = evalSign(array)
    for i in range(0, len(array)):
        if not checkNum(array[i], sign):
            return i
    return -1

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

def removeIndex(array, index):
    if index == 0 or index == (len(array) - 1):
        array.pop(index)
    else:
        array[index - 1] += array[index]
    return array

file_data = get_file_data("Day02Input.txt")
# you now have a list of Strings from the input file

print(file_data)

splitted = []
for i in file_data:
    splitted.append(i.split(" "))
print(splitted)

diff = difference(splitted)

print(diff)

safeCount = 0
unsafe = []

for array in diff:
    if checkArray(array):
        safeCount += 1
    else:
        unsafe.append(array)

print(safeCount)
print(unsafe)
print(len(unsafe))

secondSafeCount = 0
secondUnsafe = []
for array in unsafe:
    invalid = getInvalidIndex(array)
    if invalid >= 0:
        newArray = removeIndex(array, invalid)
        if checkArray(newArray):
            secondSafeCount += 1
        else:
            secondUnsafe.append(newArray)
    else:
        if checkArray(array):
            secondSafeCount += 1
        else:
            secondUnsafe.append(array)

print(secondSafeCount)
print(secondUnsafe)