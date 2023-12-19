"""
    Josephus had a friend who was saved by getting into the next-to-last
    position. What is I(n), the number of the penultimate survivor when
    every second person is executed?
"""

from collections import deque
from math import log


def flavius_friend(people_number=1, *, eliminate=2):
    if people_number < 2:
        return 0

    survivors = deque([_ for _ in range(1, people_number + 1)])

    counter = 1
    while len(survivors) > 2:
        candidate = survivors.popleft()

        if counter % eliminate != 0:
            survivors.append(candidate)

        counter += 1
    
    return survivors.pop()

def get_circle(people_number=1,  *, eliminate=2):
    max_power_of_two = int(log(people_number, 2))

    circle = people_number + 1
    while circle > people_number:
        first_term = 2**max_power_of_two
        second_term = 2**(max_power_of_two - 1)

        circle = first_term + second_term - 1

        max_power_of_two -= 1
    return circle

def flavius_friend_formula(people_number=1, *, eliminate=2):
    correct_circle = get_circle(people_number)


    return correct_circle

people_numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)

print(flavius_friend_formula(44))

# friends = []
# for people_number in people_numbers:
#     friend = flavius_friend(people_number)
#     friends.append(friend)

# print(friends)

(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
[1, 1, 3, 1, 3, 5, 7, 1, 3, 5,  7,  9,  11, 13, 15, 1]
[0, 2, 1, 3, 5, 1, 3, 5, 7, 9,  11, 1,  3,  5,  7,  9]
