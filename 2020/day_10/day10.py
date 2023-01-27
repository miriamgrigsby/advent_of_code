import pytest
from typing import List, Optional

Preamble = List[int]

with open("input.txt", "r") as input_data:
    string_input = input_data.read()
    parsed_data: List[int] = [int(line) for line in string_input.splitlines()]
    
    
def solve_day10_part1(adapter_array: List[int]) -> int:
    total_min_changes = 1 #this is TRASH but it works 🤷‍♀️
    total_max_changes = 1 #this is TRASH but it works 🤷‍♀️

    sorted_adapter_array = list(sorted(adapter_array))
    counter = 0
    while counter <= len(sorted_adapter_array):
        for index in range(counter + 1, len(sorted_adapter_array)):
            difference = sorted_adapter_array[index]  - sorted_adapter_array[counter]
            if difference <= 3:
                counter += 1
                if difference == 1:
                    total_min_changes += 1
                if difference == 3:
                    total_max_changes += 1
            else:
                break
        counter += 1
    return total_min_changes * total_max_changes

@pytest.mark.parametrize(
    "adapter_array,expected_result", [
        (
            [
                16,
                10,
                15,
                5,
                1,
                11,
                7,
                19,
                6,
                12,
                4
            ],
            35
        ),
        (
            [
                28,
                33,
                18,
                42,
                31,
                14,
                46,
                20,
                48,
                47,
                24,
                23,
                49,
                45,
                19,
                38,
                39,
                11,
                1,
                32,
                25,
                35,
                8,
                17,
                7,
                9,
                4,
                2,
                34,
                10,
                3
            ],
            220,
        ),
        (
            parsed_data,
            2232 
        )
    ]
)
def test_solve_day10_part1(adapter_array: List[int], expected_result):
    result = solve_day10_part1(adapter_array)
    assert result == expected_result

# this technically works, but the recursion is so slow that it never resolves
def solve_day10_part2(sorted_adapter_array: List[int], counter: Optional[int] = None):
    permutations = [sorted_adapter_array]

    counter = len(sorted_adapter_array) if counter is None else counter
    while True:
        if len(sorted_adapter_array[counter-3:counter]) < 3:
            break
        left_bound, _, right_bound = sorted_adapter_array[counter-3:counter]
        if (right_bound - left_bound) <= 3:
            new_sorted_adapter_array = sorted_adapter_array[0:counter - 2] + sorted_adapter_array[counter - 1:]
            permutations.extend(solve_day10_part2(new_sorted_adapter_array, counter - 1))
        counter -= 1
    return permutations

@pytest.mark.parametrize(
    "adapter_array,expected_result", [
        (
            [
                16,
                10,
                15,
                5,
                1,
                11,
                7,
                19,
                6,
                12,
                4
            ],
            8
        ),
        (
            [
                28,
                33,
                18,
                42,
                31,
                14,
                46,
                20,
                48,
                47,
                24,
                23,
                49,
                45,
                19,
                38,
                39,
                11,
                1,
                32,
                25,
                35,
                8,
                17,
                7,
                9,
                4,
                2,
                34,
                10,
                3
            ],
            19208,
        ),
        (
            parsed_data,
            2232 
        )
    ]
)
def test_solve_day10_part2(adapter_array: List[int], expected_result):
    result = solve_day10_part2([0] + list(sorted(adapter_array)) + [max(adapter_array) + 3])
    assert len(set([tuple(r) for r in result])) == expected_result
