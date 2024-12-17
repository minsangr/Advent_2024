def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data

def checkPos(update, rule):
    if rule[0:2] not in update and rule[3:5] not in update:
        return True
    index1 = 0
    index2 = 0
    for i in range(0, len(update)):
        if update[i] == rule[0:2]:
            index1 = i
        if update[i] == rule[3:5]:
            index2 = i
    if index1 < index2:
        return True
    return False

file_data = get_file_data("Day05Input.txt")

switch = False
rules = []
rawUpdates = []

for i in file_data:
    if i == '':
        switch = True
    if switch:
        rawUpdates.append(i)
    else:
        rules.append(i)

rawUpdates.pop(0)
print(rules)
updates = []

for update in rawUpdates:
    updates.append(update.split(","))

print(updates)

sum = 0
valUpdates = []

for update in updates:
    valid = True
    print("Update: " + str(update))
    for i in update:
        thisRules = []
        print("Element in Update: " + i)
        for rule in rules:
            if i in rule:
                thisRules.append(rule)
        print("Rules for this element: " + str(thisRules))
        for rule in thisRules:
            if not checkPos(update, rule):
                valid = False
    if valid:
        valUpdates.append(update)

print(valUpdates)