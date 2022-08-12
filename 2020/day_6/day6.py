import pytest
from typing import List
from functools import reduce

SlopeInput = List[str]

with open("input.txt", "r") as input_data:
    string_input = input_data.read()
    parsed_data: SlopeInput = string_input.splitlines()


# def determine_is_tree(slope_row: str, horizontal_position: int) -> int:
#     if slope_row[horizontal_position%len(slope_row)] == '.':
#         return 0
#     return 1

# @pytest.mark.parametrize()
# def test_determine_is_tree(slope_row,horizontal_position,expected_result):
#     result = determine_is_tree(slope_row, horizontal_position)
#     assert result == expected_result 


def solve_day6_part1():
    pass

# @pytest.mark.parametrize()
# def test_solve_day6_part1(parsed_data, expected_result: int, slope_int: int, vertical_step: int):
#     result = solve_day3_part1(parsed_data, slope_int, vertical_step)
#     assert result == expected_result 


