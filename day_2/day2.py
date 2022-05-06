import pytest
import typing

with open("input.txt", "r") as input_data:
    string_input = input_data.read()

parsed_data: typing.List[typing.Tuple[str, int]] = []

for s in string_input.splitlines():
    direction, magnitude = s.split(' ') 
    parsed_data.append((direction, int(magnitude)))

def solve_day2_part1(parsed_data: typing.List[typing.Tuple[str, int]]) -> int:
    total_depth = 0
    total_horizontal = 0

    for (direction, magnitude) in parsed_data:
        match direction:
            case 'up':
                total_depth -= magnitude
            case 'down':
                total_depth += magnitude
            case 'forward':
                total_horizontal += magnitude
            case _:
                raise ValueError(direction) #Not going to cover this testcase, pytest.raises       
    return total_depth * total_horizontal

@pytest.mark.parametrize('parsed_data,expected_result', [([], 0), ([('forward',1)], 0), ([('up', 1)], 0), ([('down', 1)], 0), ([('down', 1), ('forward', 2)], 2), ([('forward', 5), ('down', 5), ('forward', 8), ('up', 3), ('down', 8), ('forward', 2)], 150), (parsed_data, 1580000)])
def test_solve_day2_part1_updates_running_totals(parsed_data, expected_result):
    result = solve_day2_part1(parsed_data)
    assert result == expected_result 

def solve_day2_part2(parsed_data: typing.List[typing.Tuple[str, int]]) -> int:
    total_depth = 0
    total_horizontal = 0
    aim = 0


    for (direction, magnitude) in parsed_data:
        match direction:
            case 'up':
                aim -= magnitude
            case 'down':
                aim += magnitude
            case 'forward':
                total_horizontal += magnitude
                total_depth += (aim * magnitude)
            case _:
                raise ValueError(direction) #Not going to cover this testcase, pytest.raises       
    return total_depth * total_horizontal

@pytest.mark.parametrize('parsed_data,expected_result', [
    ([], 0),
    ([('forward',1)], 0), 
    ([('up', 1)], 0), 
    ([('down', 1)], 0),
    ([('forward', 5), ('down', 5), ('forward', 8), ('up', 3), ('down', 8), ('forward', 2)], 900),
    (parsed_data, 1251263225)
])
def test_solve_day2_part2_updates_running_totals(parsed_data: typing.List[typing.Tuple[str, int]], expected_result: int):
    result = solve_day2_part2(parsed_data)
    assert result == expected_result 
