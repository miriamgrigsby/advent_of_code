import pytest
from collections import Counter
from typing import List, Tuple

PasswordWithPolicy = Tuple[int, int, str, str]

with open("input.txt", "r") as input_data:
    string_input = input_data.read()

parsed_data: List[PasswordWithPolicy] = []

for s in string_input.splitlines():
    char_range, char, password = s.split(' ')
    start_range_string, end_range_string = char_range.split('-')
    char_string = char[0]
    parsed_data.append((int(start_range_string), int(end_range_string), char_string, password))

def is_valid(password_policy: PasswordWithPolicy) -> int: 
    start_range, end_range, char, password = password_policy
    
    counter = Counter(password)

    if counter.get(char, 0) >= start_range and counter.get(char, 0) <= end_range:
        return 1

    return 0

@pytest.mark.parametrize('parsed_data,expected_result', [((1, 3, "b", "cdefg"), 0), ((1, 3, "a", "abcde"), 1), ((1, 3, "a", "aacde"), 1), ((1, 3, "a", "aaaaa"), 0)])
def test_is_valid(parsed_data, expected_result):
    result = is_valid(parsed_data)
    assert result == expected_result    

def solve_day2_part1(password_policies: List[PasswordWithPolicy]) -> int:
    return sum([is_valid(password_policy) for password_policy in password_policies])

@pytest.mark.parametrize('parsed_data,expected_result', [([(1, 3, "b", "cdefg")], 0), ([(1, 3, "a", "abcde")], 1), ([(1, 3, "a", "abcde"), (2, 9, "c", "ccccccccc")], 2),
(parsed_data, 467)
])
def test_solve_day2_part1(parsed_data, expected_result):
    result = solve_day2_part1(parsed_data)
    assert result == expected_result 

def solve_day2_is_valid(password_policy: PasswordWithPolicy) -> int:
    start_range, end_range, char, password = password_policy

    start_char = password[start_range - 1]
    end_char = password[end_range - 1]
    if start_char != end_char and (start_char == char or end_char == char):
        return 1
    return 0

@pytest.mark.parametrize('parsed_data,expected_result', [((1, 3, "a", "abcde"), 1), ((1, 3, "b", "cdefg"), 0), ((2, 9, "c", "ccccccccc"), 0)])
def test_solve_day2_is_valid(parsed_data, expected_result):
    result = solve_day2_is_valid(parsed_data)
    assert result == expected_result 


def solve_day2_part2(password_policies: List[PasswordWithPolicy]) -> int:
    return sum([solve_day2_is_valid(password_policy) for password_policy in password_policies])

@pytest.mark.parametrize('parsed_data,expected_result', [([(1, 3, "b", "cdefg")], 0), ([(1, 3, "a", "abcde")], 1), ([(1, 3, "a", "abcde"), (2, 9, "c", "ccccccccc")], 1),
(parsed_data, 441)
])
def test_solve_day2_part2(parsed_data, expected_result):
    result = solve_day2_part2(parsed_data)
    assert result == expected_result 