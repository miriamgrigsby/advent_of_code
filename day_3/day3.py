import pytest
from typing import Literal, List
from itertools import groupby

with open("input.txt", "r") as input_data:
    string_input = input_data.read()

parsed_data: List[str] = string_input.splitlines()

def solve_day3_part1(parsed_data: List[str]) -> int:
    total_gamma = 0 
    total_epsilon = 0 

    common_bits = {}

    for data in parsed_data:
        for index, value in enumerate(data):
            try:
                common_bits[index][int(value)] += 1
            except KeyError:
                common_bits[index] = {0: 0, 1:0, int(value): 1}

    # for loop would be better but brian wants me to fail
    last_index = len(common_bits.keys()) - 1
    for bit_key in sorted(common_bits.keys()):
        if (common_bits[bit_key][0] > common_bits[bit_key][1]):
            total_gamma |= 2**(last_index - bit_key)
        elif (common_bits[bit_key][0] < common_bits[bit_key][1]):
            total_epsilon |= 2**(last_index - bit_key)

    return total_gamma * total_epsilon

@pytest.mark.parametrize('parsed_data,expected_result', [
    (['111', '110', '101'], 0),
    ([
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ], 198),
    (parsed_data, 841526)
])
def test_solve_day3_part1_calculate_power_consumption(parsed_data, expected_result):
    result = solve_day3_part1(parsed_data)
    assert result == expected_result 

def convert_bit_string_to_number(bit_string: str) -> int:
    bit_number = 0
    for index in range(len(bit_string)):
        bit_number |= int(bit_string[len(bit_string) - index - 1])* (2**(index))
    return bit_number

def find_common_bit(current_data, comparison: Literal['greater', 'less'] ):

    iterating_length = len(current_data[0])

    for index in range(iterating_length):
        grouped_data = groupby(current_data, lambda x:x[index])
        grouped_data_array = [(key, list(value)) for key, value in grouped_data]
        final_object = {}

        if len(current_data) == 1:
            break 

        for bit, bit_array in grouped_data_array:
            try:
                final_object[bit].extend(bit_array)
            except KeyError:
                final_object[bit] = bit_array
        if comparison == 'greater':
            if len(final_object.get('0', [])) > len(final_object.get('1', [])):
                current_data = final_object['0']
            else:
                current_data = final_object['1']
        else:
            if len(final_object.get('1', [])) < len(final_object.get('0', [])):
                current_data = final_object['1']
            else:
                current_data = final_object['0']
    return current_data

def solve_day3_part2(parsed_data: List[str]):
    if not parsed_data:
        return 0

    most_common_bit = find_common_bit(parsed_data, 'greater')
    least_common_bit = find_common_bit(parsed_data, 'less')

    oxygen_generator = convert_bit_string_to_number(most_common_bit[0])
    co2_scrubber_rating = convert_bit_string_to_number(least_common_bit[0])

    return oxygen_generator * co2_scrubber_rating

@pytest.mark.parametrize('parsed_data,expected_result', [
    ([], 0),
    (['011010010110'], 2842596),
    ([
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ], 230),
    (parsed_data, 4790390)
])
def test_solve_day3_part2_calculate_life_support(parsed_data, expected_result):
    result = solve_day3_part2(parsed_data)
    assert result == expected_result 

@pytest.mark.parametrize('bit_string,expected_result', [
    ('', 0),
    ('011010010110', 1686),
    ('10110', 22)
])
def test_convert_bit_string_to_number(bit_string: str, expected_result: int):
    result = convert_bit_string_to_number(bit_string)
    assert result == expected_result 
