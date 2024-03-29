"""
    A Double Tower of Hanoi contains 2n disks of n different sizes, two of
    each size. As usual, we’re required to move only one disk at a time,
    without putting a larger one over a smaller one.
    
    a)  How many moves does it take to transfer a double tower from one
        peg to another, if disks of equal size are indistinguishable from each
        other?
"""


from collections import deque


def hanoi_show(height=1, start_plank=0, finnish_plank=1):
    if height < 1:
        return

    circles = []
    
    for i in range(1, height + 1):
        circles.append(i)
        circles.append(i)
    
    circles = deque(circles)
    planks = [circles, deque(), deque()]

    print(planks)
    arrangement(len(circles), planks, start_plank, finnish_plank)
    print(planks)

def arrangement(height: int, planks, start_plank=0, finish_plank=1):
    if height == 2:
        circle = planks[start_plank].popleft()
        planks[finish_plank].appendleft(circle)
        print(planks)

        circle = planks[start_plank].popleft()
        planks[finish_plank].appendleft(circle)
        return

    temp_plank = set([0, 1, 2]).difference(set([start_plank, finish_plank])).pop()

    # Move next two discs to temp plank
    arrangement(height-2, planks, start_plank=start_plank, finish_plank=temp_plank)
    print(planks)

    # Move last disc to finish plank
    second_circle = planks[start_plank].popleft()
    planks[finish_plank].appendleft(second_circle)
    print(planks)

    second_circle = planks[start_plank].popleft()
    planks[finish_plank].appendleft(second_circle)
    print(planks)

    # Move all discs from temp plank to the finish plank
    arrangement(height-2, planks, start_plank=temp_plank, finish_plank=finish_plank)


h = 3
hanoi_show(h)
