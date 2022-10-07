import enum
import pytest
from typing import List, Dict, Tuple, Set
from enum import Enum

class InstructionEnum(str, Enum):
    accumulate = 'acc'
    noop = 'nop'
    jump = 'jmp'

Instruction = Tuple[InstructionEnum, int, int]
Instructions = List[Instruction]

with open("input.txt", "r") as input_data:
    string_input = input_data.read()
    parsed_data: List[str] = string_input.splitlines()
    instructions_array: Instructions = []
    for index, line in enumerate(parsed_data):
        command, amount = line.split(" ")
        instructions_array.append((InstructionEnum(command), int(amount), index))
    
# print([(enu.value, amount, index )for enu, amount, index in instructions_array])

def solve_day8_part1(instruction_array: Instructions, visited: set, start_position: int) -> int:
   for instruction_enum, instruction_count, instruction_index in instruction_array[start_position:]:
        if instruction_index not in visited:
            visited.add(instruction_index)
            match instruction_enum:
                case InstructionEnum.accumulate:
                    return solve_day8_part1(instruction_array, visited, start_position+1) + instruction_count
                case InstructionEnum.noop:
                    return solve_day8_part1(instruction_array, visited, start_position+1)
                case InstructionEnum.jump:
                    return solve_day8_part1(instruction_array, visited, start_position + instruction_count)
                case _:
                    raise RuntimeError
        else:
            return 0

   return 0


@pytest.mark.parametrize(
    "instruction_array,acc", [
        (
            [],
            0
        ),
        (
            [("nop", +0, 1)],
            0,
        ),
        (
            [("acc", +1, 2)],
            1,
        ),
        (
            [('nop', 0, 0), ('acc', 1, 1), ('jmp', 4, 2), ('acc', 3, 3), ('jmp', -3, 4), ('acc', -99, 5), ('acc', 1, 6), ('jmp', -4, 7), ('acc', 6, 8)],
            5
        ),
        (
          instructions_array,
          1753  
        )
    ]
)
def test_solve_day8_part1(instruction_array: Instructions, acc: int):
    result = solve_day8_part1(instruction_array, set(), 0)
    assert result == acc

def solve_day8_determine_if_infinite_loop(instruction_array: Instructions, visited: set, start_position: int) -> Tuple[int, bool]:
    for instruction_enum, instruction_count, instruction_index in instruction_array[start_position:]:
        if instruction_index not in visited:
            visited.add(instruction_index)
            match instruction_enum:
                case InstructionEnum.accumulate:
                    running_total, is_infinite_loop = solve_day8_determine_if_infinite_loop(instruction_array, visited, start_position+1) 
                    return (running_total + instruction_count, is_infinite_loop)
                case InstructionEnum.noop:
                    return solve_day8_determine_if_infinite_loop(instruction_array, visited, start_position+1)
                case InstructionEnum.jump:
                    return solve_day8_determine_if_infinite_loop(instruction_array, visited, start_position + instruction_count)
                case _:
                    raise RuntimeError
        else:
            return (0, True)
    return (0, False)

@pytest.mark.parametrize(
    "instruction_array,acc", [
        (
            [("jmp", +1, 1), ("jmp", -1, 2)],
            (0, True)
        ),
        (
            [],
            (0, False)
        ),
        (
            [('nop', 0, 0), ('acc', 1, 1), ('jmp', 4, 2), ('acc', 3, 3), ('jmp', -3, 4), ('acc', -99, 5), ('acc', 1, 6), ('jmp', -4, 7), ('acc', 6, 8)],
            (5, True)
        ),
        (
            [('nop', 0, 0), ('acc', 1, 1), ('jmp', 4, 2), ('acc', 3, 3), ('jmp', -3, 4), ('acc', -99, 5), ('acc', 1, 6), ('nop', -4, 7), ('acc', 6, 8)],
            (8, False)
        ),
    ]
)
def test_solve_day8_determine_if_infinite_loop(instruction_array: Instructions, acc: int):
    result = solve_day8_determine_if_infinite_loop(instruction_array, set(), 0)
    assert result == acc

def solve_day8_solve_part_2(instruction_array: Instructions) -> int:
    for instruction_enum, instruction_count, instruction_index in instruction_array:
        match instruction_enum:
            case InstructionEnum.noop:
                instruction_array_items_preceding = instruction_array[0:instruction_index]
                instruction_array_items_following = instruction_array[instruction_index + 1:]
                new_array_instruction: Instruction = (InstructionEnum.jump, instruction_count, instruction_index)
                new_instruction_array = instruction_array_items_preceding + [new_array_instruction] + instruction_array_items_following
            case InstructionEnum.jump:
                instruction_array_items_preceding = instruction_array[0:instruction_index]
                instruction_array_items_following = instruction_array[instruction_index + 1:]
                new_array_instruction: Instruction = (InstructionEnum.noop, instruction_count, instruction_index)
                new_instruction_array = instruction_array_items_preceding + [new_array_instruction] + instruction_array_items_following
            case _:
                new_instruction_array = instruction_array
        running_total, is_infinite_loop = solve_day8_determine_if_infinite_loop(new_instruction_array, set(), 0)
        if not is_infinite_loop:
            return running_total
    return 0

@pytest.mark.parametrize(
    "instruction_array,acc", [
        (
            [(InstructionEnum.jump, +1, 1), (InstructionEnum.jump, -1, 2)],
            0
        ),
        (
            [(InstructionEnum.noop, 0, 0), (InstructionEnum.accumulate, 1, 1)],
            1
        ),
        (
            [(InstructionEnum.noop, 0, 0), (InstructionEnum.accumulate, 1, 1), (InstructionEnum.jump, 4, 2), (InstructionEnum.accumulate, 3, 3), (InstructionEnum.jump, -3, 4), (InstructionEnum.accumulate, -99, 5), (InstructionEnum.accumulate, 1, 6), (InstructionEnum.jump, -4, 7), (InstructionEnum.accumulate, 6, 8)],
            8
        ),
        (
          instructions_array,
          733  
        )
    ]
)
def test_solve_day8_part2(instruction_array: Instructions, acc: int):
    result = solve_day8_solve_part_2(instruction_array)
    assert result == acc
