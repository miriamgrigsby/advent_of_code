import pytest
from typing import List, Tuple, Dict

with open("input.txt", "r") as input_data:
    string_input = input_data.read()

Coordinate = Tuple[int, int]
Line = Tuple[Coordinate, Coordinate]
Plume =  List[Line]
SeaFloor = Dict[Coordinate, int]

plumes: Plume = [plume for plume in [tuple(tuple(int(coordinate) for coordinate in coordinate_set.split(',')) for coordinate_set in entry.split(" -> ")) for entry in string_input.splitlines()]
]

def day5_part1_make_coordinate_board(plumes: Plume) -> SeaFloor: 
    sea_floor = {}
    for line in plumes:
        if line[0][0] == line[1][0]:
            for y_position in range(min(line[0][1], line[1][1]), max(line[0][1], line[1][1]) + 1):
                try:
                    sea_floor[(line[0][0], y_position)] += 1
                except KeyError:
                    sea_floor[(line[0][0], y_position)] = 1
        elif line[0][1] == line[1][1]:
            for x_position in range(min(line[0][0], line[1][0]), max(line[0][0], line[1][0]) + 1):
                try:
                    sea_floor[(x_position, line[0][1])] += 1
                except KeyError:
                    sea_floor[(x_position, line[0][1])] = 1
    return sea_floor

@pytest.mark.parametrize('plumes,expected_result', [
    (
        [],
        {}
    ),
    (
        [((0, 9), (5, 9)), ((8, 0), (0, 8)), ((9, 4), (3, 4)), ((2, 2), (2, 1)), ((7, 0), (7, 4)), ((6, 4), (2, 0)), ((0, 9), (2, 9)), ((3, 4), (1, 4)), ((0, 0), (8, 8)), ((5, 5), (8, 2))],
        {
            (7, 0): 1,
            (2, 1): 1,
            (7, 1): 1,
            (2, 2): 1,
            (7, 2): 1,
            (7, 3): 1,
            (1,4): 1,
            (2,4): 1,
            (3,4): 2,
            (4,4): 1,
            (5,4): 1,
            (6,4): 1,
            (7,4): 2,
            (8,4): 1,
            (9,4): 1,
            (0,9): 2,
            (1,9): 2,
            (2,9): 2,
            (3,9): 1,
            (4,9): 1,
            (5,9): 1,
        }
    )
])
def test_solve_day5_part1_make_coordinate_board(plumes: Plume, expected_result: SeaFloor):
    result = day5_part1_make_coordinate_board(plumes)
    assert result == expected_result


def day5_part1(sea_floor: SeaFloor) -> int:
    return len([line for line in sea_floor.values() if line > 1])

@pytest.mark.parametrize('sea_floor,expected_result', [
    (
        {},
        0
    ),
    (
       {(2,9): 2},
       1
    ),
    (
        {(2,9): 2, (5,9): 1},
        1  
    ), 
    (
        {(2,9): 2, (5,9): 1, (0,9): 2,},
        2
    ),
    (
        day5_part1_make_coordinate_board(plumes),
        5092
    ),
    (
        {
            (7, 0): 1,
            (2, 1): 1,
            (7, 1): 1,
            (2, 2): 1,
            (7, 2): 1,
            (7, 3): 1,
            (1,4): 1,
            (2,4): 1,
            (3,4): 2,
            (4,4): 1,
            (5,4): 1,
            (6,4): 1,
            (7,4): 2,
            (8,4): 1,
            (9,4): 1,
            (0,9): 2,
            (1,9): 2,
            (2,9): 2,
            (3,9): 1,
            (4,9): 1,
            (5,9): 1,
        },
        5
    )
])
def test_solve_day5_part1(sea_floor: SeaFloor, expected_result: int):
    result = day5_part1(sea_floor)
    assert result == expected_result

@pytest.mark.parametrize('plumes,expected_result', [
    (
        [],
        {}
    ),
    (
        [
            ((1,1), (3,3))
        ],
        {
            (1,1): 1,
            (2,2): 1,
            (3,3): 1,
        }
    ), 
    (
        [
           ((3,0), (1,2)) 
        ],
        {
            (3,0): 1,
            (2,1): 1,
            (1,2): 1
        }
    ),
    (
        [
           ((0,3), (2,1)) 
        ],
        {
            (0,3): 1,
            (1,2): 1,
            (2,1): 1
        }
    ),
    (
        [
            ((3,3), (1,1))
        ],
        {
            (1,1): 1,
            (2,2): 1,
            (3,3): 1,
        }
    ), 
     (
        [((0, 9), (5, 9)), ((8, 0), (0, 8)), ((9, 4), (3, 4)), ((2, 2), (2, 1)), ((7, 0), (7, 4)), ((6, 4), (2, 0)), ((0, 9), (2, 9)), ((3, 4), (1, 4)), ((0, 0), (8, 8)), ((5, 5), (8, 2))],
        {
            (0,0): 1,
            (2,0): 1,
            (7,0): 1,
            (8,0): 1,

            (1,1): 1,
            (2,1): 1,
            (3,1): 1,
            (7,1): 2,

            (2,2): 2,
            (4,2): 1,
            (6,2): 1,
            (7,2): 1,
            (8,2): 1,
        
            (3,3): 1,
            (5,3): 2,
            (7,3): 2,
            
            (1,4): 1,
            (2,4): 1,
            (3,4): 2,
            (4,4): 3,
            (5,4): 1,
            (6,4): 3,
            (7,4): 2,
            (8,4): 1,
            (9,4): 1,

            (3,5): 1,
            (5,5): 2,

            (2,6): 1,
            (6,6): 1,

            (1,7): 1,
            (7,7): 1,

            (0,8): 1,
            (8,8): 1,

            (0,9): 2,
            (1,9): 2,
            (2,9): 2,
            (3,9): 1,
            (4,9): 1,
            (5,9): 1,
        }
    )
])
def test_solve_day5_part2_make_coordinate_board(plumes: Plume, expected_result: SeaFloor):
    result = day5_part2_make_coordinate_board(plumes)
    assert result == expected_result
def day5_part2_make_coordinate_board(plumes: Plume) -> SeaFloor:
    sea_floor = {}
    for line in plumes:
        if line[0][0] == line[1][0]:
            for y_position in range(min(line[0][1], line[1][1]), max(line[0][1], line[1][1]) + 1):
                try:
                    sea_floor[(line[0][0], y_position)] += 1
                except KeyError:
                    sea_floor[(line[0][0], y_position)] = 1
        elif line[0][1] == line[1][1]:
            for x_position in range(min(line[0][0], line[1][0]), max(line[0][0], line[1][0]) + 1):
                try:
                    sea_floor[(x_position, line[0][1])] += 1
                except KeyError:
                    sea_floor[(x_position, line[0][1])] = 1
        elif abs(line[0][0] - line[1][0]) == abs(line[0][1] - line[1][1]):
            magnitude = abs(line[0][0] - line[1][0])

            for counter in range(magnitude + 1):
                if  line[1][0] > line[0][0]:
                    x_position = line[0][0] + counter
                else:
                    x_position = line[0][0] + (counter*-1)
                if line[1][1] > line[0][1]:
                    y_position = line[0][1] + counter
                else:
                    y_position = line[0][1] + (counter*-1)
                try:
                    sea_floor[(x_position, y_position)] += 1
                except KeyError:
                    sea_floor[(x_position, y_position)] = 1
    return sea_floor


@pytest.mark.parametrize('sea_floor,expected_result', [
    (
        {
            (0,0): 1,
            (2,0): 1,
            (7,0): 1,
            (8,0): 1,

            (1,1): 1,
            (2,1): 1,
            (3,1): 1,
            (7,1): 2,

            (2,2): 2,
            (4,2): 1,
            (6,2): 1,
            (7,2): 1,
            (8,2): 1,
        
            (3,3): 1,
            (5,3): 2,
            (7,3): 2,
            
            (1,4): 1,
            (2,4): 1,
            (3,4): 2,
            (4,4): 3,
            (5,4): 1,
            (6,4): 3,
            (7,4): 2,
            (8,4): 1,
            (9,4): 1,

            (3,5): 1,
            (5,5): 2,

            (2,6): 1,
            (6,6): 1,

            (1,7): 1,
            (7,7): 1,

            (0,8): 1,
            (8,8): 1,

            (0,9): 2,
            (1,9): 2,
            (2,9): 2,
            (3,9): 1,
            (4,9): 1,
            (5,9): 1,
        },
        12
    ),
    (
        day5_part2_make_coordinate_board(plumes),
        20484
    )
])
def test_solve_day5_part2(sea_floor: SeaFloor, expected_result: int):
    result = day5_part1(sea_floor)
    assert result == expected_result