import re

def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data

file_data = get_file_data("Day03Input.txt")
print(file_data)

regex = "mul\\([1-9]{1,3},[1-9]{1,3}\\)"
matches = re.findall(regex, file_data[0])
print(matches)

sum = 0
for pair in matches:
    nums = pair[4:int(len(pair) - 1)]
    num = nums.split(",")
    sum += (int(num[0]) * int(num[1]))

print(sum)
