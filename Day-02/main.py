def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data


file_data = get_file_data("Day02Input.txt")
# you now have a list of Strings from the input file

print(file_data)

safe = 0
for i in file_data:
    first = i[0]
    second = i[1]
    if first < second:
        for j in range(0,len(i)):
            if not i[j] <
    for j in i:
