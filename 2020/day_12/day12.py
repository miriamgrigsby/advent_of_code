import pytest
from typing import List, Literal, Tuple
from dataclasses import dataclass
import math

Action = Literal['N', 'E', 'S', 'W', 'F', 'L', 'R']

@dataclass
class Instruction:
    action: Action
    value: int

def parse_data(string_input: str) -> List[Instruction]:
    instructions: List[Instruction] = []
    for instruction in string_input.splitlines():
        for action, *value in instruction.split():
            if action =='N' or action == 'E' or action == 'S' or action ==  'W' or action ==  'F' or action ==  'L' or action ==  'R':
                actual_value = int("".join(value))
                instructions.append(Instruction(action=action, value=actual_value))
            else:
                raise RuntimeError
    return instructions
    
with open("input.txt", "r") as input_data:
    parsed_data = parse_data(input_data.read())

def solve_day12_part1(instructions) -> Tuple[int, int]:
    previous_position: Tuple[int, int] = (0, 0)
    facing_direction = 0

    for instruction in instructions:
        # Instruction(action='F', value=24)
        match instruction.action:
            case 'N':
                previous_position = (previous_position[0], previous_position[1] + instruction.value)
            case 'E':
                previous_position = (previous_position[0] + instruction.value, previous_position[1])
            case 'W':
                previous_position = (previous_position[0] - instruction.value, previous_position[1])
            case 'S':
                previous_position = (previous_position[0], previous_position[1] - instruction.value)
            case 'L':
                facing_direction -= instruction.value
            case 'R':
                facing_direction += instruction.value
            case 'F':
                match facing_direction % 360:
                    case 0:
                        # east
                        previous_position = (previous_position[0] + instruction.value, previous_position[1])
                    case 90:
                        # south
                        previous_position = (previous_position[0], previous_position[1] - instruction.value)
                    case 180:
                        # west
                        previous_position = (previous_position[0] - instruction.value, previous_position[1])
                    case 270:
                        # north
                        previous_position = (previous_position[0], previous_position[1] + instruction.value)
                    case _:
                        raise RuntimeError
            case _:
                raise RuntimeError
    return previous_position

@pytest.mark.parametrize("instructions, expected_result", [
    (
        [],
        (0,0)
    ),
    (
        [
            Instruction(action='F', value=10),
        ],
        (10,0)
    ),
    (
        [
            Instruction(action='N', value=3),
        ],
        (0,3)
    ),
    (
        [
            Instruction(action='E', value=5),
        ],
        (5,0)
    ),
    (
        [
            Instruction(action='W', value=5),
        ],
        (-5, 0)
    ),
    (
        [
            Instruction(action='S', value=5),
        ],
        (0, -5)
    ),
    (
        [
            Instruction(action='L', value=270), Instruction(action='F', value=10)
        ],
        (0, -10)
    ),
    (
        [
            Instruction(action='R', value=90), Instruction(action='F', value=10)
        ],
        (0, -10)
    ),
    (
        [
            Instruction(action='F', value=10),
            Instruction(action='N', value=3),
        ],
        (10,3)
    ),
    (
        [
            Instruction(action='F', value=10),
            Instruction(action='N', value=3),
            Instruction(action='F', value=7),
        ],
        (17,3)
    ),
    (
        [
            Instruction(action='F', value=10),
            Instruction(action='N', value=3),
            Instruction(action='F', value=7),
            Instruction(action='R', value=90),
        ],
        (17,3)
    ),
    (
        [
            Instruction(action='F', value=10),
            Instruction(action='N', value=3),
            Instruction(action='F', value=7),
            Instruction(action='R', value=90),
            Instruction(action='F', value=11)
        ],
        (17,-8)
    )
])
def test_solve_day12_part1(instructions, expected_result):
    result = solve_day12_part1(instructions)
    assert result == expected_result

@pytest.mark.parametrize("instructions, expected_result", [
    (
        [
            Instruction(action='F', value=10),
            Instruction(action='N', value=3),
            Instruction(action='F', value=7),
            Instruction(action='R', value=90),
            Instruction(action='F', value=11)
        ],
        25  
    ),
    (
        parsed_data,
        845
    )
])
def test_solve_day12_part1_with_puzzle_input(instructions, expected_result):
    x, y = solve_day12_part1(instructions)
    assert abs(x)+abs(y)== expected_result


def matrix_multiplication(theta: float, way_point: Tuple[int, int]) -> Tuple[int, int]:
    transform_matrix = [[math.cos(theta), -math.sin(theta)], [math.sin(theta), math.cos(theta)]]

    unrounded_way_point: List[float] = [sum(a*b for a,b in zip(way_point, B_col)) for B_col in zip(*transform_matrix)]

    return round(unrounded_way_point[0]), round(unrounded_way_point[1])

def solve_day12_part2(instructions) -> Tuple[int, int]:
    ships_position: Tuple[int, int] = (0, 0)
    way_point: Tuple[int, int] = (10, 1)

    for instruction in instructions:
        # Instruction(action='F', value=24)
        # 180 = math.pi
        # 90 = math.pi*0.5
        # 270 = math.pi*1.5
        # 0 = 0
        match instruction.action:
            case 'N':
                way_point = (way_point[0], way_point[1] + instruction.value)
            case 'E':
                way_point = (way_point[0] + instruction.value, way_point[1])
            case 'W':
                way_point = (way_point[0] - instruction.value, way_point[1])
            case 'S':
                way_point = (way_point[0], way_point[1] - instruction.value)
            case 'L':
                theta = math.pi*(instruction.value/90*0.5*-1)
                way_point = matrix_multiplication(theta, way_point)
            case 'R':
                theta = math.pi*(instruction.value/90*0.5)
                way_point = matrix_multiplication(theta, way_point)
            case 'F':
                ships_position = (ships_position[0] + way_point[0]*instruction.value, ships_position[1] + way_point[1]*instruction.value)
            case _:
                raise RuntimeError
    return ships_position

@pytest.mark.parametrize("instructions, expected_result", [
    (
        [],
        (0,0)
    ),
    (
        [
            Instruction(action='F', value=10),
        ],
        (100,10)
    ),
    (
        [
            Instruction(action='N', value=3),
        ],
        (0,0)
    ),
    (
        [
            Instruction(action='E', value=5),
        ],
        (0,0)
    ),
    (
        [
            Instruction(action='W', value=5),
        ],
        (0,0)
    ),
    (
        [
            Instruction(action='S', value=5),
        ],
        (0,0)
    ),
    (
        [
            Instruction(action='L', value=270), Instruction(action='F', value=10)
        ],
        (10, -100)
    ),
    (
        [
            Instruction(action='R', value=90), Instruction(action='F', value=10)
        ],
        (10, -100)
    ),
    (
        [
            Instruction(action='F', value=10),
            Instruction(action='N', value=3),
            Instruction(action='F', value=7),
        ],
        (170,38)
    ),
    (
        [
            Instruction(action='F', value=10),
            Instruction(action='N', value=3),
            Instruction(action='F', value=7),
            Instruction(action='R', value=90),
            Instruction(action='F', value=11)
        ],
        (214,-72)
    )
])
def test_solve_day12_part2(instructions, expected_result):
    result = solve_day12_part2(instructions)
    assert result == expected_result

@pytest.mark.parametrize("instructions, expected_result", [
    (
        [
            Instruction(action='F', value=10),
            Instruction(action='N', value=3),
            Instruction(action='F', value=7),
            Instruction(action='R', value=90),
            Instruction(action='F', value=11)
        ],
        286  
    ),
    (
        parsed_data,
        27016
    )
])
def test_solve_day12_part2_with_puzzle_input(instructions, expected_result):
    x, y = solve_day12_part2(instructions)
    assert abs(x)+abs(y)== expected_result