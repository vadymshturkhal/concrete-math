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


def survivors_number_deque(people_number=1, eliminate=2):
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


eliminate = 2
people_numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25)

survivors = []
for people_number in people_numbers:
    survivor =  survivors_number_deque(people_number, eliminate)
    survivors.append(survivor)

print(f"{eliminate = }")
print(people_numbers)
print(survivors)
