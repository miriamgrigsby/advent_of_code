import pytest
from typing import TypedDict, List, Iterable


# [[{number: 26, marked: false},  68  3 95 59], [], [], [], []]

class BingoBoardItem(TypedDict):
    number: int
    marked: bool

BingoBoard = List[List[BingoBoardItem]]

with open("input.txt", "r") as input_data:
    string_input = input_data.read()

parsed_data: List[str] = string_input.splitlines()

bingo_numbers: List[int] = [int(entry) for entry in parsed_data[0].split(',')]

bingo_boards: List[BingoBoard] = []

prev_board: BingoBoard = []

for row in parsed_data[2:]:
    if len(row) == 0:
        bingo_boards.append(prev_board)
        prev_board = []
    else:
        row_array = row.split(' ')
        prev_board.append([{"number": int(column), "marked": False} for column in row_array if column])
else: 
    bingo_boards.append(prev_board)

def day4_part1_determine_bingo(bingo_board: BingoBoard) -> bool:
    for index in range(5):
        bingo_row = True
        for inner_index in range(5):
            if bingo_board[index][inner_index]['marked'] is False:
                bingo_row = False
                break
        if bingo_row:
            return bingo_row

    for index in range(5):
        bingo_column = True
        for inner_index in range(5):
            if bingo_board[inner_index][index]['marked'] is False:
                bingo_column = False
                break
        if bingo_column:
            return bingo_column

    return False

row_bingo: BingoBoard = [
   [ {"number": 1, "marked": True}, {"number": 2, "marked": True}, {"number": 22, "marked": True}, {"number": 24, "marked": True},  {"number": 20, "marked": True}],
 [{"number": 22, "marked": False},{"number": 23, "marked": False},{"number": 24, "marked": False},{"number": 12, "marked": False},{"number": 27, "marked": False}],
[{"number": 28, "marked": False},{"number": 12, "marked": False},{"number": 13, "marked": False},{"number": 14, "marked": False},{"number": 15, "marked": False}],
 [{"number": 56, "marked": False},{"number": 5, "marked": False},{"number": 88, "marked": False},{"number": 0, "marked": False},{"number": 3, "marked": False}],
 [{"number": 22, "marked": False},{"number": 46, "marked": False},{"number": 454, "marked": False},{"number": 45, "marked": False},{"number": 21, "marked": False}]
]

column_bingo: BingoBoard = [
   [ {"number": 2, "marked": True}, {"number": 22, "marked": False}, {"number": 23, "marked": False}, {"number": 24, "marked": False},  {"number": 25, "marked": False}],
   [ {"number": 26, "marked": True}, {"number": 27, "marked": False}, {"number": 28, "marked": False}, {"number": 29, "marked": False},  {"number": 22, "marked": False}],
   [ {"number": 1, "marked": True}, {"number": 2, "marked": False}, {"number": 22, "marked": False}, {"number": 28, "marked": False},  {"number": 26, "marked": False}],
   [ {"number": 27, "marked": True}, {"number": 28, "marked": False}, {"number": 24, "marked": False}, {"number": 23, "marked": False},  {"number": 21, "marked": False}],
   [ {"number": 20, "marked": True}, {"number": 9, "marked": False}, {"number": 8, "marked": False}, {"number": 12, "marked": False},  {"number": 12, "marked": False}],
]

fake_board_1 = [
    [ {"number": 1, "marked": False}, {"number": 2, "marked": False}, {"number": 22, "marked": False}, {"number": 24, "marked": False},  {"number": 20, "marked": False}],
 [{"number": 22, "marked": False},{"number": 23, "marked": False},{"number": 24, "marked": False},{"number": 12, "marked": False},{"number": 27, "marked": False}],
[{"number": 28, "marked": False},{"number": 12, "marked": False},{"number": 13, "marked": False},{"number": 14, "marked": False},{"number": 15, "marked": False}],
 [{"number": 56, "marked": False},{"number": 5, "marked": False},{"number": 88, "marked": False},{"number": 0, "marked": False},{"number": 3, "marked": False}],
 [{"number": 22, "marked": False},{"number": 46, "marked": False},{"number": 454, "marked": False},{"number": 45, "marked": False},{"number": 21, "marked": False}]
]

fake_board_2 = [
    [ {"number": 1, "marked": False}, {"number": 2, "marked": False}, {"number": 22, "marked": False}, {"number": 24, "marked": False},  {"number": 20, "marked": False}],
 [{"number": 22, "marked": False},{"number": 23, "marked": False},{"number": 24, "marked": False},{"number": 12, "marked": False},{"number": 27, "marked": False}],
[{"number": 28, "marked": False},{"number": 12, "marked": False},{"number": 13, "marked": False},{"number": 14, "marked": False},{"number": 15, "marked": False}],
 [{"number": 56, "marked": False},{"number": 5, "marked": True},{"number": 88, "marked": False},{"number": 0, "marked": False},{"number": 3, "marked": False}],
 [{"number": 22, "marked": False},{"number": 46, "marked": False},{"number": 454, "marked": False},{"number": 45, "marked": False},{"number": 21, "marked": False}]
]

@pytest.mark.parametrize('bingo_board', [column_bingo, row_bingo])
def test_solve_day4_part1_determine_bingo(bingo_board):
    result = day4_part1_determine_bingo(bingo_board)
    assert result is True

def day4_part1_mark_number(bingo_number: int, bingo_board: BingoBoard) -> BingoBoard:
    for index in range(5):
        for inner_index in range(5):
            if bingo_board[index][inner_index]['number'] == bingo_number:
                bingo_board[index][inner_index]['marked'] = True
                return bingo_board
    return bingo_board

@pytest.mark.parametrize('bingo_number,bingo_board,expected_result', [(5, fake_board_1, fake_board_2)])
def test_solve_day4_part1_mark_number(bingo_number: int, bingo_board: BingoBoard, expected_result: BingoBoard):
    result = day4_part1_mark_number(bingo_number, bingo_board)
    assert result == expected_result

def day4_part1_calculate_sum(bingo_board: BingoBoard) -> int:
    unmarked_total = 0

    for index in range(5):
        for inner_index in range(5):
            if bingo_board[index][inner_index]['marked']:
                continue
            else:
                unmarked_total += bingo_board[index][inner_index]['number']

    return unmarked_total

def day4_part1_play_bingo(bingo_numbers: List[int], bingo_boards: List[BingoBoard]) -> int:
    winning_number = 0
    for number in bingo_numbers:
        for board in bingo_boards:
            marked_board = day4_part1_mark_number(number, board)
            is_bingo_board = day4_part1_determine_bingo(marked_board)
            if is_bingo_board: 
                return day4_part1_calculate_sum(marked_board) * number
    return winning_number

# Did not write tests on the last two functions because it would've been *brian: heinous*

# solution for part1 but it mutates the bing_boards and breaks part two if it runs here
# print(day4_part1_play_bingo(bingo_numbers, bingo_boards))

def day4_part2(bingo_numbers: List[int], bingo_boards: List[BingoBoard]) -> Iterable[int]:
    for number in bingo_numbers:
        pop_array = []
        for index, board in enumerate(bingo_boards):
            marked_board = day4_part1_mark_number(number, board)
            is_bingo_board = day4_part1_determine_bingo(marked_board)
            if is_bingo_board: 
                yield day4_part1_calculate_sum(marked_board) * number
                pop_array.append(index)
        for i in sorted(pop_array, reverse=True):
            bingo_boards.pop(i)
    

solved_day4_part_2 = day4_part2(bingo_numbers, bingo_boards)      
finished = list(solved_day4_part_2)[-1]
print(finished)