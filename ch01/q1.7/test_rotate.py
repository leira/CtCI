#!/usr/bin/env python3

def rotatedIndex(i, j, dem):
    return j, dem-1-j

def rotate(matrix):
    dem = len(matrix)
    if dem < 2:
        return matrix

    for i in range(dem//2):
        for j in range(i, dem-1-i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[dem-1-j][i]
            matrix[dem-1-j][i] = matrix[dem-1-i][dem-1-j]
            matrix[dem-1-i][dem-1-j] = matrix[j][dem-1-i]
            matrix[j][dem-1-i] = temp

    return matrix

def test_rotate():
    assert [] == rotate([])
    assert [1] == rotate([1])

    assert [[3, 1], [4, 2]] == rotate([[1, 2], [3, 4]])

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

