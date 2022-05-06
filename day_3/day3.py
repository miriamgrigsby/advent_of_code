import pytest
import typing

with open("input.txt", "r") as input_data:
    string_input = input_data.read()


parsed_data: typing.List[str] = string_input.splitlines()

def solve_day3_part1(parsed_data: typing.List[str]) -> int:
    # python counter for collections
    # power consumption = gamma * epsilon
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
