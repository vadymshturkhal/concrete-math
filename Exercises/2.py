"""
    Find the shortest sequence of moves that transfers a tower of n disks
    from the left peg A to the right peg B, if direct moves between A and B
    are disallowed. (Each move must be to or from the middle peg. As usual,
    a larger disk must never appear above a smaller one.)
"""

def hanoi_restricted(height=1):
    """
        1: height - 1 to temp, height - 1 to finish, last to temp
        2: height - 1 to temp, height - 1 to start, last to finish
        3: height - 1 to temp, height - 1 to finish.

        Example:
            heigh 1 => 2
            heigh 2 => 8
            height 3 = 26
    """
    if height < 1:
        return 0

    if height == 1:
        return 2

    return 3 * hanoi_restricted(height - 1) + 2

def hanoi_restricted_dynamic(height=1):
    if height < 0:
        return 0

    heights = [0, 2]

    for i in range(1, height + 1):
        moves = 2 + 3 * heights[i]
        heights.append(moves)

    return heights[height]

from collections import deque


def hanoi_restricted_show(discs=1, start_plank=0, finnish_plank=2):
    if discs < 1:
        return

    circles = []
    
    for i in range(1, discs + 1):
        circles.append(i)
    
    circles = deque(circles)
    planks = [circles, deque(), deque()]

    print(planks)
    arrangement(len(circles), planks, start_plank, finnish_plank)
    print(planks)

def arrangement(height: int, planks, start_plank=0, finish_plank=2):
    if height < 1:
        return

    if height == 1:
        temp_plank = 1
        circle = planks[start_plank].popleft()
        planks[temp_plank].appendleft(circle)
        print(planks)

        circle = planks[temp_plank].popleft()
        planks[finish_plank].appendleft(circle)
        return

    temp_plank = 1

    # Move next two discs to temp plank
    arrangement(height-1, planks, start_plank=start_plank, finish_plank=finish_plank)
    print(planks)

    # Move last disc to temp plank
    second_circle = planks[start_plank].popleft()
    planks[temp_plank].appendleft(second_circle)
    print(planks)

    arrangement(height-1, planks, start_plank=finish_plank, finish_plank=start_plank)
    print(planks)

    second_circle = planks[temp_plank].popleft()
    planks[finish_plank].appendleft(second_circle)
    print(planks)

    # Move all discs from temp plank to the finish plank
    arrangement(height-1, planks, start_plank=start_plank, finish_plank=finish_plank)


h = 3
print(hanoi_restricted(h))
print(hanoi_restricted_dynamic(h))
hanoi_restricted_show(h)
