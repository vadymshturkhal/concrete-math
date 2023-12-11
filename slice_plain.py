def slice_plane(lines=1):
    if lines <= 0:
        return 1

    intersection_points = lines - 1
    return slice_plane(lines - 1) + intersection_points + 1


lines = (1, 2, 3, 4)
for line in lines:
    print(slice_plane(line))