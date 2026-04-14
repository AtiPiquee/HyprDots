#!/bin/python3

from random import randint
from typing import List, Tuple, Dict
from args import parser_args
from graph import create_graph

"""
test = int(input("How many tests do you want to do : "))
start = int(input("Enter the starting int : "))
end = int(input("Enter the ending int : "))
"""

def generate_nums(test: int, start: int, end: int) -> List[List[int]]:
    ints = []
    for i in range(test):
        temp = []
        for j in range(start, end, 1):
            temp.append(randint(start, end))

        ints.append(temp)

    return ints # Two dimensionnal array to have multiple tests stored in


def value_sorting(ints: List[List[int]]) -> List[List[int]]:
    groups = {}

    for int_l in ints:
        for num in int_l:
            if num not in groups:
                groups[num] = []
            groups[num].append(num)

    return sorted(groups.values(), key=lambda x: x[0])


def stats(end: int, test: int, final_list: List[List[int]]) -> List[Tuple[int, int, float]]:
    total_elements = end * test

    percentages = []
    for group in final_list:
        count = len(group)
        percentage = (count / total_elements) * 100
        percentages.append((group[0], count, round(percentage, 2)))
    
    return percentages

def show_results(statistics: List[Tuple[int, int, float]]) -> None:
    for valeur, count, pct in statistics:
        print(f"Valeur {valeur} : {count} fois, soit {pct}%")

def main() -> None:
    tests, start, end = parser_args()
    values = generate_nums(tests, start, end)
    final_values = value_sorting(values)
    statistics = stats(end, tests, final_values)

    show_results(statistics)

if __name__ == "__main__":
    main()



