from random import randint

test = int(input("How many tests do you want to do : "))
start = int(input("Enter the starting int : "))
end = int(input("Enter the ending int : "))

def generate_nums(test, start, end):
    ints = []
    for i in range(test):
        temp = []
        for j in range(start, end, 1):
            temp.append(randint(start, end))

        ints.append(temp)

    return ints # Two dimensionnal array to have multiple tests stored in


def value_sorting(ints):
    groups = {}

    for int_l in ints:
        for num in int_l:
            if num not in groups:
                groups[num] = []
            groups[num].append(num)

    return sorted(groups.values(), key=lambda x: x[0])


def stats(end, test, final_list): 
    total_elements = end * test

    percentages = []
    for group in final_list:
        count = len(group)
        percentage = (count / total_elements) * 100
        percentages.append((group[0], count, round(percentage, 2)))
    
    return percentages

for valeur, count, pct in percentages:
    print(f"Valeur {valeur} : {count} fois, soit {pct}%")
