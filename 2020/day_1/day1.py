from re import X
import pytest
from typing import List, Tuple

PasswordWithPolicy = Tuple[int, int, str, str]

with open("input.txt", "r") as input_data:
    string_input = input_data.read()


parsed_data: List[int] = []

parsed_data = [int(s) for s in string_input.splitlines()]

def solve_day1_part1(parsed_data) -> int:
    unique_data = set(parsed_data)
    while len(unique_data):
        first_num = unique_data.pop()
        for current_num in unique_data:
            if first_num + current_num == 2020:
                return first_num * current_num
    return 0

@pytest.mark.parametrize('parsed_data,expected_result', [
    ([], 0),
    ([19], 0),
    ([1990, 10], 0),
    ([1990, 30], 59700),
    ([
        1721,
        979,
        366,
        299,
        675,
        1456,
    ], 514579),
    (parsed_data, 121396)
])
def test_solve_day1_part1(parsed_data, expected_result):
    result = solve_day1_part1(parsed_data)
    assert result == expected_result 

def solve_day1_part2(parsed_data) -> int:
    unique_data = set(parsed_data)
    while len(unique_data):
        first_num = unique_data.pop()
        shortened_list = set(list(unique_data))
        while len(shortened_list):
            second_num = shortened_list.pop()
            for current_num in shortened_list:
                if first_num + second_num + current_num == 2020:
                    return first_num * second_num * current_num 
    return 0

@pytest.mark.only()
@pytest.mark.parametrize('parsed_data,expected_result', [
    ([], 0),
    ([19], 0),
    ([1990, 10], 0),
    ([1990, 30], 0),
    ([1990, 29, 1], 57710),
    ([
        1721,
        979,
        366,
        299,
        675,
        1456,
    ], 241861950),
    (parsed_data, 73616634)
])
def test_solve_day1_part2(parsed_data, expected_result):
    result = solve_day1_part2(parsed_data)
    assert result == expected_result 
