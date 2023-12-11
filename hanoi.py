from collections import deque


def hanoi_show(height=1, start_plank=0, finnish_plank=1):
    if height < 1:
        return

    circles = deque([_ for _ in range(1, height + 1)])
    planks = [circles, deque(), deque()]

    arrangement(height, planks, start_plank, finnish_plank)
    print(planks)

def arrangement(height: int, planks, start_plank=0, finish_plank=1):
    if height == 1:
        circle = planks[start_plank].popleft()
        planks[finish_plank].appendleft(circle)
        return

    temp_plank = set([0, 1, 2]).difference(set([start_plank, finish_plank])).pop()

    # Move all circlec except last to tmp
    arrangement(height-1, planks, start_plank=start_plank, finish_plank=temp_plank)
    print(planks)

    # Move last circle to finnish plank
    second_circle = planks[start_plank].popleft()
    planks[finish_plank].appendleft(second_circle)
    print(planks)

    # Move all circles from temp plank to the finish plank
    arrangement(height-1, planks, start_plank=temp_plank, finish_plank=finish_plank)

def hanoi_times_rec(height):
    if height < 1:
        return 0

    if height == 1:
        return 1

    if height == 2:
        return 3

    return 1 + hanoi_times_rec(height - 1) + hanoi_times_rec(height - 1)

def hanoi_times_dynamic(height):
    if height < 0:
        return 0

    heights = [0, 1, 3]

    for _ in range(height - 2):
        next_height = heights[-1] + 1 + heights[-1]
        heights.append(next_height)
    
    return heights[-1]

h = 8
hanoi_show(h)
print(hanoi_times_rec(h))
print(hanoi_times_dynamic(h))
