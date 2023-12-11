"""
    How many max pieces of pizza we can take, when we cut pizza N times?

    If plane has no lines it has 1 plane.
    If plane intersected by 1 line it has 2 planes.
    If plane intersected by 2 lins it has 4 planes.

    slice_plane(0) = 1
    slice_plane(1) = 2
    slice_plane(2) = 4
"""


def slice_plane_recursive(lines=1):
    if lines <= 0:
        return 1

    intersection_points = lines - 1
    return slice_plane_recursive(lines - 1) + intersection_points + 1


lines = (1, 2, 3, 4)
for line in lines:
    print(slice_plane_recursive(line))