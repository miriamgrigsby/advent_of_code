import pytest
from typing import TypedDict, List, Iterable


# class BingoBoardItem(TypedDict):
#     number: int
#     marked: bool

# BingoBoard = List[List[BingoBoardItem]]

with open("input.txt", "r") as input_data:
    string_input = input_data.read()

# parsed_data: List[str] = string_input.splitlines()

# bingo_numbers: List[int] = [int(entry) for entry in parsed_data[0].split(',')]

def day5_part1():
    raise NotImplementedError()

# @pytest.mark.parametrize('bingo_number,bingo_board,expected_result', [(5, fake_board_1, fake_board_2)])
# def test_solve_day5_part1(bingo_number: int, bingo_board: BingoBoard, expected_result: BingoBoard):
#     result = day4_part1_mark_number(bingo_number, bingo_board)
#     assert result == expected_result

