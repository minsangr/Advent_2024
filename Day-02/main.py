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

