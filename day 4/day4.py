import parse
from collections import deque
import numpy as np
input = open("in.txt", "r")

matrix = []
for line in input.readlines():
    stripped_line = line.strip("\n")
    char_list = [char for char in stripped_line]
    matrix.append(char_list)

print(matrix)

def check_all_directions(matrix):
    count = 0
    count2 = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'X':
                neighbors = get_neighbors(matrix,i,j)
                for neighbor in neighbors:
                    if neighbor == ['X','M','A','S']:
                        count += 1
            if matrix[i][j] == 'A':
                neighbors = get_neighbors_mas(matrix,i,j)
                valid_patterns = [
                    [['M', 'S'],
                     ['M', 'S']],
                    [['M', 'M'],
                     ['S', 'S']],
                    [['S', 'M'],
                     ['S', 'M']],
                    [['S', 'S'],
                     ['M', 'M']],
                ]
                print(neighbors)
                if neighbors in valid_patterns:
                    count2 += 1
    return count, count2


def get_safe(matrix,x,y):
    try:
        if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]):
            return matrix[x][y]
        else:
            return None
    except:
        return None


def get_neighbors(matrix,x,y):

    directions = [
        [(x + j, y - j) for j in range(4)],
        [(x + j, y + j) for j in range(4)],
        [(x - j, y - j) for j in range(4)],
        [(x - j, y + j) for j in range(4)],
        [(x, y - j) for j in range(4)],
        [(x, y + j) for j in range(4)],
        [(x - j, y) for j in range(4)],
        [(x + j, y) for j in range(4)]
    ]

    result = []
    for direction in directions:
        chars = []
        for posx, posy in direction:
            char = get_safe(matrix, posx, posy)
            chars.append(char)
        if len(chars) == 4:
            result.append(chars)

    return result

def get_neighbors_mas(matrix,x,y):
    directions = [
        (x - 1, y - 1),
        (x + 1, y - 1),
        (x - 1, y + 1),
        (x + 1, y + 1),
    ]

    neighbors = [get_safe(matrix, px, py) for px, py in directions]

    if None in neighbors or len(neighbors) != 4:
        return None

    return [
        [neighbors[0], neighbors[1]],
        [neighbors[2], neighbors[3]]
    ]


print(check_all_directions(matrix))