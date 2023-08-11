import pytest
from typing import Dict, List
from dataclasses import dataclass

# @dataclass
# class Mask:
#     mask: str

# @dataclass
# class Memory:
#     address: int
#     value: int

# Instructions = List[ Mask | Memory]

# def parse_data(string_input: str) -> Instructions:
#     array_of_strings = string_input.splitlines()
#     final_instructions = []
#     for string in array_of_strings:
#         key, value = string.split(' = ')
#         if key == 'mask':
#             final_instructions.append(Mask(mask=value))
#         else:
#             final_instructions.append(Memory(address=int(key[4:-1]), value=int(value)))
#     return final_instructions
    
# with open("input.txt", "r") as input_data:
#     parsed_data = parse_data(input_data.read())

official_puzzle_input = [10,16,6,0,1,17]



def solve_day15_part1(puzzle_input: List[int], turn: int) -> int:
    puzzle_state: Dict[int, List[int]] = {0: []}

    puzzle_state.update({key:[value] for value, key  in enumerate(puzzle_input[0:-1], 1)})

    last_number_spoken: int = puzzle_input[-1]
    for current_turn in range(len(puzzle_input), turn):
        print("was spoken", last_number_spoken)
        try:
            nums = puzzle_state[last_number_spoken]
            if len(nums) == 1:
                last_number_spoken = current_turn - nums[0]
            else:
                nums.append(current_turn)
                last_number_spoken = nums[-1] - nums[-2]
            puzzle_state[last_number_spoken].append(current_turn)
            print("setting last number spken", last_number_spoken, nums[-1], nums[-2])
        except KeyError:
            print("not found last number spken", last_number_spoken)
            puzzle_state[last_number_spoken] = [current_turn]
            last_number_spoken = 0
            puzzle_state[last_number_spoken].append(current_turn + 1)

        # try:
        #     print("was spoken", puzzle_state[last_number_spoken])
        #     last_number_spoken = puzzle_state[last_number_spoken][-1] - puzzle_state[last_number_spoken][-2]
        #     puzzle_state[last_number_spoken].append(current_turn)
        # except KeyError:
        #     print("WASNT FOUND")
        #     puzzle_state[last_number_spoken] = [current_turn]
        #     last_number_spoken = 0
        #     puzzle_state[last_number_spoken].append(current_turn)
    # for current_turn in range(len(puzzle_input)+1, turn):
    #     print("last number spoken",last_number_spoken)
    #     print("puzzle state",puzzle_state)
    #     try:
    #         print("was spoken", puzzle_state[last_number_spoken])
    #         last_number_spoken = puzzle_state[last_number_spoken][-1] - puzzle_state[last_number_spoken][-2]
    #         puzzle_state[last_number_spoken].append(current_turn)
    #     except KeyError:
    #         print("WASNT FOUND")
    #         puzzle_state[last_number_spoken] = [current_turn]
    #         last_number_spoken = 0
    #         puzzle_state[last_number_spoken].append(current_turn)
        

    return last_number_spoken

@pytest.mark.parametrize("puzzle_input,turn,expected_result", [
    (
        [0,3,6],
        10, 
        0
    ),
    # (
    #     [0,3,6],
    #     2020, 
    #     436
    # ),
    # (
    #     10,16,6,0,1,17,
    #     14954914379452
    # )
   
])
def test_solve_day15_part1(puzzle_input: List[int], turn: int, expected_result: int):
    result = solve_day15_part1(puzzle_input, turn)
    assert result == expected_result
