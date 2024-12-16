def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data

file_data = get_file_data("Day05Input.txt")

switch = False
rules = []
updates = []

for i in file_data:
    if i == '':
        switch = True
    if switch:
        updates.append(i)
    else:
        rules.append(i)

updates.pop(0)
print(rules)
print(updates)

for update  in updates: