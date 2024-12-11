import re

def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data

file_data = get_file_data("Day03Input.txt")

regex = "mul\\([0-9]+,[0-9]+\\)|do\\(\\)|don't\\(\\)"

sum = 0
do = True

for i in file_data:
    matches = re.findall(regex, i)
    print(matches)
    for pair in matches:
        if pair == "do()":
            do = True
        elif pair == "don't()":
            do = False
        else:
            if do:
                nums = pair[4:int(len(pair) - 1)]
                num = nums.split(",")
                sum += (int(num[0]) * int(num[1]))

print(sum)
