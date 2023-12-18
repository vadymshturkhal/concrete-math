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


h = 3
print(hanoi_restricted(h))
print(hanoi_restricted_dynamic(h))