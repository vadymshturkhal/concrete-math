"""
    Josephus had a friend who was saved by getting into the next-to-last
    position. What is I(n), the number of the penultimate survivor when
    every second person is executed?
"""

from collections import deque


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


people_numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)

friends = []
for people_number in people_numbers:
    friend =  flavius_friend(people_number)
    friends.append(friend)

print(friends)
