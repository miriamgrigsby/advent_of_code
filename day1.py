import pytest
import typing

# DAY 1

example_input = [199,
200,
208,
210,
200,
207,
240,
269,
260,
263]

with open("input.txt", "r") as input_data:
    string_input = input_data.read()

parsed_data: typing.List[int] = [int(s) for s in string_input.splitlines()]

def solve_day_1(readings: typing.List[int]) -> int:
    total_sum = 0
    if len(readings) <= 1:
        return total_sum
    readings_itr = iter(readings)
    prev_reading = next(readings_itr)
    for reading in readings_itr:
        if reading > prev_reading:
            total_sum += 1
        prev_reading = reading
    return total_sum

@pytest.mark.parametrize("readings, expected_result", [([], 0), ([100, 101], 1), ([100, 101, 102], 2), ([103, 101, 102], 1), ([100], 0), (example_input, 7), (parsed_data, 1462)])    
def test_solve_day_1_handles_inputs_and_updates_total(readings,expected_result ):
    result = solve_day_1(readings)
    assert result == expected_result

def solve_day1_part2(readings: typing.List[int]) -> int: 
    total_sum = 0

    if len(readings) <= 3:
        return total_sum

    window_tuple: typing.List[int] = readings[0:3]

    for index, _ in enumerate(readings, 1):
        current_window = readings[index:index+3]
        if sum(window_tuple) < sum(current_window):
           total_sum += 1 
        window_tuple = current_window

    return total_sum

@pytest.mark.parametrize("readings, expected_result", [
    ([], 0),
    ([100], 0),
    ([100, 101], 0),
    ([100, 101, 102], 0),
    ([100, 101, 102, 103], 1),
    ([100, 110, 50, 3], 0),
    ([100, 199, 208, 210, 200, 207, 240, 269, 260, 263], 6),
    ([607, 618, 618, 617, 647, 716, 769, 792], 5),
    (parsed_data, 1497)
])
def test_solve_day1_part2_handles_inputs_and_updates_total(readings,expected_result ):
    result = solve_day1_part2(readings)
    assert result == expected_result