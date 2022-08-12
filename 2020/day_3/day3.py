import pytest
from typing import List
from functools import reduce

SlopeInput = List[str]

with open("input.txt", "r") as input_data:
    string_input = input_data.read()
    parsed_data: SlopeInput = string_input.splitlines()


def determine_is_tree(slope_row: str, horizontal_position: int) -> int:
    if slope_row[horizontal_position%len(slope_row)] == '.':
        return 0
    return 1

@pytest.mark.parametrize('slope_row,horizontal_position,expected_result', [
    (
        "..##.........##.......",
        3,
        1
    ), 
    (
        "#...#...#..#...#...#..",
        6, 
        0
    ),
    (
        "#...#...#..#...#...#..",
        28, 
        0
    ),
    (
        "..##.........##.......",
        25,
        1
    ),
])
def test_determine_is_tree(slope_row,horizontal_position,expected_result):
    result = determine_is_tree(slope_row, horizontal_position)
    assert result == expected_result 


def solve_day3_part1(slope_input_array: SlopeInput, slope_int: int, vertical_step: int) -> int:
    total_trees = 0
    for index in range(len(slope_input_array) - 1):
        horizontal_position = (index + 1)*slope_int
        if (index + 1) * vertical_step  > len(slope_input_array) - 1:
            break
        is_tree = determine_is_tree(slope_input_array[(index + 1) * vertical_step ], horizontal_position)
        total_trees += is_tree
    return total_trees

@pytest.mark.parametrize('parsed_data,expected_result,slope_int, vertical_step', [
    (
        [
            "....",
            "...#"
        ],
        1,
        3,
        1
    ),
    (
        [
            "....",
            "...."
        ],
        0,
        3,
        1
    ),
    (
        [
            ".......",
            "...#..#" ,
            "......#",
        ],
        2,
        3,
        1
    ),
    (
        parsed_data,
        276,
        3,
        1
    )
])
def test_solve_day3_part1(parsed_data, expected_result: int, slope_int: int, vertical_step: int):
    result = solve_day3_part1(parsed_data, slope_int, vertical_step)
    assert result == expected_result 


def solve_day3_part2(slope_input_array):
    arboreal_tuple = [
        (1,1),
        (3,1),
        (5,1),
        (7,1),
        (1,2)
    ]

    total_trees_array = [solve_day3_part1(slope_input_array, slope_int, vertical_step) for slope_int, vertical_step in arboreal_tuple]

    return reduce(lambda acc, total_tree: acc * total_tree, total_trees_array, 1)

@pytest.mark.parametrize('parsed_data,expected_result', [
    (
        [
            "..##.......",
            "#...#...#..",
            ".#....#..#.",
            "..#.#...#.#",
            ".#...##..#.",
            "..#.##.....",
            ".#.#.#....#",
            ".#........#",
            "#.##...#...",
            "#...##....#",
            ".#..#...#.#"
        ], 
        336
    ),
    (
        parsed_data,
        7812180000
    )
])
def test_solve_day3_part2(parsed_data, expected_result):
    result = solve_day3_part2(parsed_data)
    assert result == expected_result 