import pytest
from typing import Tuple, List
    
Ticket = Tuple[str, str]
AllTickets = List[Ticket]

parsed_data: AllTickets = []

with open("input.txt", "r") as input_data:
    string_input = input_data.read()
    split_data = string_input.splitlines()
    for line in split_data:
        row = line[:7]
        column = line[7:]
        ticket:Ticket = (row, column)
        parsed_data.append(ticket)

def compute_range_and_column_or_row(input_str: str, upper_bound: str, lower_bound: str) -> int:
    running_total = 0
    for index, char in enumerate(input_str):
        if char == upper_bound:
            bit = 1
        elif char == lower_bound:
            bit = 0
        else:
            raise RuntimeError()
        running_total += bit*2**(len(input_str) - index-1)
    return running_total

@pytest.mark.parametrize('input_str,upper_bound,lower_bound,expected_result', [
    ("RLR", "R", "L", 5),
    ("FBFBBFF", "B", "F", 44)
])
def test_compute_range_and_column_or_row(input_str, upper_bound, lower_bound, expected_result):
    result = compute_range_and_column_or_row(input_str, upper_bound, lower_bound)
    assert result == expected_result 

def solve_day5_part1(parsed_data) -> int:
    totals_array = []
    for row, column in parsed_data:
        row_number = compute_range_and_column_or_row(row, "B", "F")
        column_number = compute_range_and_column_or_row(column, "R", "L")
        totals_array.append( (row_number*8) + column_number)
    return max(totals_array)

@pytest.mark.parametrize('parsed_data,expected_result', [
    (
        [("FBFBBFF", "RLR")], 
        357
    ),
    (
        [("BFFFBBF", "RRR")], 
        567
    ),
    (
        [("FFFBBBF", "RRR")], 
        119
    ),
    (
        [("BBFFBBF", "RLL")], 
        820
    ),
    (
        parsed_data, 
        801
    ),
])
def test_solve_day5_part1(parsed_data, expected_result):
    result = solve_day5_part1(parsed_data)
    assert result == expected_result 

def solve_day5_part2(parsed_data) -> int:
    totals_array = []
    for row, column in parsed_data:
        row_number = compute_range_and_column_or_row(row, "B", "F")
        column_number = compute_range_and_column_or_row(column, "R", "L")
        totals_array.append( (row_number*8) + column_number)
    sorted_totals = list(sorted(totals_array))
    for seat in range(1, len(sorted_totals)):
        prev_seat = sorted_totals[seat-1]
        next_seat = sorted_totals[seat]
        if (next_seat - prev_seat) == 2:
            return prev_seat + 1
    return 0

@pytest.mark.parametrize('parsed_data,expected_result', [
    (
        parsed_data, 
        597
    ),
])
def test_solve_day5_part2(parsed_data, expected_result):
    result = solve_day5_part2(parsed_data)
    assert result == expected_result 
