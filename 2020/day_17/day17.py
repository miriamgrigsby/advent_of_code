import pytest
from typing import List

Preamble = List[int]

with open("input.txt", "r") as input_data:
    string_input = input_data.read()
    parsed_data: List[int] = [int(line) for line in string_input.splitlines()]
    
    
def solve_day17_part1():
    pass

# @pytest.mark.parametrize(
#     "input,expected_result", [
#         (
#             [
                
#             ],
#             5,
#         ),
#     ]
# )
# def test_solve_day17_part1(input: List[int], preamble: int, expected_result):
#     result = solve_day17_part1(input, preamble)
#     assert result == expected_result
