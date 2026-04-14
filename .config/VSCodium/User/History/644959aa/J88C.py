from random import randint

ints = [] # Two dimensionnal array to have multiple tests stored in

test = int(input("How many tests do you want to do : "))
start = int(input("Enter the starting int : "))
end = int(input("Enter the ending int : "))

for i in range(test):
    temp = []
    for j in range(start, end, 1):
        temp.append(randint(start, end))
    
    ints.append(temp)

groups = {}

for int_l in ints:
    for num in int_l:
        if num not in groups:
            groups[num] = []
        groups[num].append(num)

final_list = sorted(groups.values(), key=lambda x: x[0])

for i in range(len(final_list)):
    print(final_list[i])

total_elements = start * test

percentages = []
for group in final_list:
    count = len(group)
    percentage = (count / total_elements) * 100
    percentages.append((groupe[0], count, round(percentage, 2)))

