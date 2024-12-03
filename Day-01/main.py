def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data


file_data = get_file_data("Day01Input.txt")
# you now have a list of Strings from the input file

splitted = []
for i in file_data:
    splitted.append(i.split("   "))

list1 = []
list2 = []

for i in splitted:
    list1.append(i[0])
    list2.append(i[1])

list1.sort()
list2.sort()

sum = 0
for i in range(0, len(list1)):
    sum += abs(int(list1[i]) - int(list2[i]))
print(sum)