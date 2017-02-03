#!/usr/bin/env python3

def rotate(matrix):
    dem = len(matrix)
    if dem < 2:
        return matrix

    rotated = [[0]*dem for _ in range(dem)]

    for i in range(dem):
        for j in range(dem):
            rotated[j][dem-1-i] = matrix[i][j]
    return rotated

def test_rotate():
    assert [[13, 9, 5, 1],
            [14, 10, 6, 2],
            [15, 11, 7, 3],
            [16, 12, 8, 4]] \
            == \
            rotate([[1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12],
                    [13, 14, 15, 16]])

    assert [[21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5]] \
            == \
            rotate([[1, 2, 3, 4, 5],
                    [6, 7, 8, 9, 10],
                    [11, 12, 13, 14, 15],
                    [16, 17, 18, 19, 20],
                    [21, 22, 23, 24, 25]])

