def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data


file_data = get_file_data("Day01Input.txt")
# you now have a list of Strings from the input file
print(file_data)

sample = "1-3 a: abcde"

split_sample = sample.split(" ")

for i in file_data:
    print(i.split("   "))

print(split_sample[0])
print(split_sample[1])
print(split_sample[2])