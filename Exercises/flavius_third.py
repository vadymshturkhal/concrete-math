"""
    During the Jewish-Roman war, he was among a band of 41
    Jewish rebels trapped in a cave by the Romans. Preferring suicide to capture,
    the rebels decided to form a circle and, proceeding around it, to kill every
    third remaining person until no one was left. But Josephus, along with an
    unindicted co-conspirator, wanted none of this suicide nonsense; so he quickly
    calculated where he and his friend should stand in the vicious circle.

    Examples:
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16
        1, 2, 2, 1, 4, 1, 4, 7, 1,  4, 7,  10, 13, 2,  5,  8

        17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32
        11, 14, 17, 20, 2,  5,  8,  11, 14, 17, 20, 23, 26, 29, 1,  4

        31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46
        1,  4,  7,  10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46

        47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70
        2,  5,  8,  11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50, 53, 56, 59, 62, 65, 68, 1
"""

from collections import deque


def survivors_number_deque(people_number=1, eliminate=2):
    if people_number < 1:
        return 0

    if eliminate <= 1:
        return 0
    
    survivors = deque([_ for _ in range(1, people_number + 1)])

    counter = 1
    while len(survivors) > eliminate - 1:
        candidate = survivors.popleft()

        if counter % eliminate != 0:
            survivors.append(candidate)

        counter += 1

    return survivors.pop()

def flavius_third_list(people_number=1, *, eliminate=3):
    if people_number < 0:
        return

    survivors = [0, 1, 2]

    for i in range(2, people_number):
        if survivors[i] == i:
            survivors.append(2)
        elif survivors[i] == i - 1:
            survivors.append(1)
        else:
            survivors.append(survivors[i] + 3)

    return survivors[people_number]

def flavius_third_in_place(people_number=1, *, eliminate=3):
    if people_number < 0:
        return 0

    if people_number < 2:
        return people_number

    current_survivor = 2
    next_survivor = 2

    for i in range(2, people_number):
        if current_survivor == i:
            next_survivor = 2
        elif current_survivor == i - 1:
            next_survivor = 1
        else:
            next_survivor += 3

        current_survivor = next_survivor

    return next_survivor

people_numbers = [_ for _ in range(1, 16 + 1)]
print(people_numbers)

survivors = []
for people_number in people_numbers:
    survivor = survivors_number_deque(people_number, eliminate=3)
    survivors.append(survivor)
print(survivors)

survivors = []
for people_number in people_numbers:
    survivor = flavius_third_list(people_number, eliminate=3)
    survivors.append(survivor)
print(survivors)

survivors = []
for people_number in people_numbers:
    survivor = flavius_third_in_place(people_number, eliminate=3)
    survivors.append(survivor)
print(survivors)
