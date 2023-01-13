import pytest
from typing import List

Preamble = List[int]

with open("input.txt", "r") as input_data:
    string_input = input_data.read()
    parsed_data: List[int] = [int(line) for line in string_input.splitlines()]
    
    
def solve_day9_part1(input: List[int], preamble: int) -> int:
    for index, number in enumerate(input[preamble:]):
        number_matches = False
        preamble_array = input[index:preamble+index]
        for preamble_number in preamble_array:
            for inner_preamble_number in preamble_array:
                if preamble_number == inner_preamble_number:
                    continue
                if preamble_number + inner_preamble_number == number:
                    number_matches = True
        if not number_matches:
            return number
    return 0

@pytest.mark.parametrize(
    "input, preamble ,expected_result", [
        (
            [
                35,
                20,
                15,
                25,
                47,
                40,
                62,
                55,
                65,
                95,
                102,
                117,
                150,
                182,
                127,
                219,
                299,
                277,
                309,
                576
            ],
            5,
            127
        ),
        (
            parsed_data,
            25,
            25918798 
        )
    ]
)
def test_solve_day9_part1(input: List[int], preamble: int, expected_result):
    result = solve_day9_part1(input, preamble)
    assert result == expected_result

def solve_day9_part2(num_array: List[int], incorrect_number: int,) -> int:
    for start_index in range(len(num_array)):
        for end_index in range(len(num_array) - start_index):
            if sum(num_array[start_index:start_index+end_index]) == incorrect_number:
                return min(num_array[start_index:start_index+end_index]) + max(num_array[start_index:start_index+end_index])
    return 0

@pytest.mark.parametrize("num_array,expected_result,preamble", [
    (
      [
                35,
                20,
                15,
                25,
                47,
                40,
                62,
                55,
                65,
                95,
                102,
                117,
                150,
                182,
                127,
                219,
                299,
                277,
                309,
                576
            ],
            62 ,
            5
    ),
    (
        parsed_data,
        3340942, 25
    )
])
def test_solve_day9_part2(num_array: List[int], expected_result, preamble):
    incorrect_number = solve_day9_part1(num_array, preamble)
    result = solve_day9_part2(num_array, incorrect_number)
    assert result == expected_result