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

def slice_plane_dynamic(lines=1):
    if lines < 0:
        return 1

    slices = [1, 2]

    for i in range(2, lines + 1):
        planes = i + slices[i - 1]
        slices.append(planes)

    return slices[lines]

def slice_plane_closed_form(lines=1):
    triangle_numbers = (lines + 1) * lines // 2
    return triangle_numbers + 1


lines = (1, 2, 3, 4)
for line in lines:
    print(slice_plane_recursive(line))

print()

for line in lines:
    print(slice_plane_dynamic(line))

print()

for line in lines:
    print(slice_plane_closed_form(line))