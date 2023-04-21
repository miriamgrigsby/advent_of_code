import pytest
from typing import List
from dataclasses import dataclass

@dataclass
class Mask:
    mask: str

@dataclass
class Memory:
    address: int
    value: int

Instructions = List[ Mask | Memory]

def parse_data(string_input: str) -> Instructions:
    array_of_strings = string_input.splitlines()
    final_instructions = []
    for string in array_of_strings:
        key, value = string.split(' = ')
        if key == 'mask':
            final_instructions.append(Mask(mask=value))
        else:
            final_instructions.append(Memory(address=int(key[4:-1]), value=int(value)))
    return final_instructions
    
with open("input.txt", "r") as input_data:
    parsed_data = parse_data(input_data.read())

def create_bitwise_result(mask: str, value: int) -> int:
    reverse_mask = mask[::-1]
    result = value
    for index, char in enumerate(reverse_mask):
        if char == 'X':
            continue
        bit = int(char) #0 or 1
        int_value = 2**index
        negated_int = ~int_value
        mew = negated_int & result
        result = (int_value * bit) | mew
    return result

@pytest.mark.parametrize("mask,value,expected_result", [
    (
        'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX1',
        0,
        1
    ),
    (
        '1XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX1',
        0,
        (1+2**35)
    ),
    (
        'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX00',
        1,
        0
    ),
    (
        'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X',
        11,                         # 0001011
        73
    ),
    (
        'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X',
        101,
        101
    ),
    (
        'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X',
        0,
        64
    ),
])
def test_solve_create_bitwise_result(mask: str, value: int, expected_result: int):
    result = create_bitwise_result(mask, value)
    assert result == expected_result

def solve_day14_part1(instructions: Instructions) -> int:
    shared_memory = {}
    mask = ''
    for instruction in instructions:
        if isinstance(instruction, Mask):
            mask = instruction.mask
        elif isinstance(instruction, Memory):
            address = instruction.address
            memory_value = instruction.value
            value_to_store = create_bitwise_result(mask, memory_value)
            shared_memory[address] = value_to_store
    return sum(shared_memory.values())

@pytest.mark.parametrize("instructions,expected_result", [
    (
        [Mask(mask='XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X'), Memory(address=8, value=11), Memory(address=7, value=101), Memory(address=8, value=0)],
        165
    ),
    (
        parsed_data,
        14954914379452
    )
   
])
def test_solve_day14_part1(instructions: Instructions, expected_result: int):
    result = solve_day14_part1(instructions)
    assert result == expected_result