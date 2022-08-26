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
