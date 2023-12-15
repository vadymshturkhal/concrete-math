"""
    During the Jewish-Roman war, he was among a band of 41
    Jewish rebels trapped in a cave by the Romans. Preferring suicide to capture,
    the rebels decided to form a circle and, proceeding around it, to kill every
    third remaining person until no one was left. But Josephus, along with an
    unindicted co-conspirator, wanted none of this suicide nonsense; so he quickly
    calculated where he and his friend should stand in the vicious circle.

    We start with N people numbered 1 to n around a circle,
    and we eliminate every second remaining person until only one survives.

    The elimination order is 2, 4, 6, 8, 10, 3, 7, 1, 9, so 5 survives.
"""

from collections import deque
from math import log


def survivors_number_deque(people_number=1, *, eliminate=2):
    if people_number < 1:
        return 0

    if eliminate <= 1:
        return 0
    
    survivors = deque([_ for _ in range(1, people_number + 1)])

    counter = 1
    while len(survivors) > 1:
        candidate = survivors.popleft()

        if counter % eliminate != 0:
            survivors.append(candidate)

        counter += 1
    
    return survivors.pop()

def survivors_number_with_power_of_two(people_number=1, *, eliminate=2):
    if people_number < 1:
        return 0

    if eliminate <= 1:
        return 0
    
    min_power_of = log(people_number, eliminate)
    min_power_of = int(min_power_of)

    terms_between = people_number - 2**min_power_of

    survivor = 1 + terms_between * 2
    return survivor

def survivors_number_recur(people_number=1, *, eliminate=2):
    if people_number < 1:
        return 0

    if people_number == 1:
        return 1
    
    if people_number % eliminate != 0:
        return 2 * survivors_number_recur(people_number // 2) + 1
    return 2 * survivors_number_recur(people_number // 2) - 1

def survivors_number_binary(people_number=1, *, eliminate=2):
    if people_number < 1:
        return 0

    binary_people_num = deque(bin(people_number))
    binary_people_num.popleft()
    binary_people_num.popleft()
    binary_people_num.rotate(-1)

    rotated = ''.join(binary_people_num)
    rotated_num = int(rotated, 2)

    return rotated_num

people_numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
print(people_numbers)

flavuises = [survivors_number_deque, survivors_number_with_power_of_two, survivors_number_recur, survivors_number_binary]

for flavius in flavuises:
    survivors = []

    for people_number in people_numbers:
        survivor =  survivors_number_deque(people_number)
        survivors.append(survivor)
    print(survivors)
