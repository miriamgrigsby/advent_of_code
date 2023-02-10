from pickle import TUPLE
import pytest
from typing import List, Literal, Dict, Tuple

Position = Tuple[int, int]
Seat = Literal['.', '#', 'L']
Seats = Dict[Position, Seat]

def parse_data(string_input: str) -> Seats:
    seats: Seats = {}
    for x_coordinate, row in enumerate(string_input.splitlines()):
        for y_coordinate, char in enumerate(row):
            if char == '.' or char == '#' or char == 'L':
                seats[(x_coordinate,y_coordinate)] = char 
            else:
                raise RuntimeError
    return seats
    
with open("input.txt", "r") as input_data:
    parsed_data = parse_data(input_data.read())

# fn that takes in position and all seats and tells if that position is L or #   
def determines_type_of_seat(current_position: Position, seats: Seats) -> Seat:
    # generate all possible positions
    possible_positions: List[Position] = [
        # (0,0) (middle)
        (0,1), #right
        (1,0), #down
        (0, -1), #(left)
        (-1, 0), #(up)
        (-1, -1), #(up, left)
        (-1, 1), #(up right)
        (1, -1), #(down left)
        (1, 1), #(down right)
    ]

    # loop over possible positions (starts at 0), then have statements on the rules
    occupied_adjacent_seats = 0
    for possible_position in possible_positions:
        current_x, current_y = current_position 
        possible_x, possible_y = possible_position 
        new_x = current_x + possible_x
        new_y = current_y + possible_y
        try:
            if seats[(new_x, new_y)] == '#':
                occupied_adjacent_seats += 1    
        except KeyError:
            pass

    if seats[current_position] == '#' and occupied_adjacent_seats >= 4:
        return 'L'

    if seats[current_position] == 'L' and occupied_adjacent_seats == 0:
        return '#'
    
    return seats[current_position]

@pytest.mark.parametrize(
    "position,seats,expected_result", [
        (
            (0,0),
            parse_data("."),
            "."
        ),
        (
            (0,0),
            parse_data("L"),
            "#"
        ),
        (
            (0,0),
            parse_data("#"),
            "#"
        ),
        (
            (1,1),
            parse_data("LLL\nLLL\nLLL"),
            "#"
        ),
        (
            (1,1),
            parse_data("###\n###\n###"),
            "L"
        ),
        (
            (1,1),
            parse_data("...\n...\n..."),
            "."
        ),
        (
            (1,1),
            parse_data("#LL\nL#L\n###"),
            "L"
        )
    ]
)
def test_determines_type_of_seat(position: Position, seats: Seats, expected_result: Seat):
    result = determines_type_of_seat(position, seats)
    assert result == expected_result

# loop over all seats and call first fn and returns new seats obj
def calculate_entire_seat_grid(seats: Seats) -> Seats:
    new_seats: Seats = {}
    for position in seats.keys():
        new_seats[position] = determines_type_of_seat(position, seats)
    return new_seats

@pytest.mark.parametrize(
    "seats,expected_result", [
        (
           parse_data(
"""L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""
            ),
        parse_data(
"""#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##"""
            ),
        ),
        (
            parse_data(
"""#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##"""
            ),
        parse_data(
"""#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##"""
            ),
        ),
        (
            parse_data(
"""#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##"""
            ),
            parse_data(
"""#.##.L#.##
#L###LL.L#
L.#.#..#..
#L##.##.L#
#.##.LL.LL
#.###L#.##
..#.#.....
#L######L#
#.LL###L.L
#.#L###.##"""
            ),
        ),
        (
           parse_data(
"""#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##"""
            ), 
            parse_data(
"""#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##"""
            ), 
        )
    ]
)
def test_calculate_entire_seat_grid(seats: Seats, expected_result: Seat):
    result = calculate_entire_seat_grid(seats)
    assert result == expected_result

# fn that calls previous fn until the outputs from that previous fn are the same twice 
def solve_day11_part1(seats:Seats) -> int:
    previous = calculate_entire_seat_grid(seats)
    while True:
        current = calculate_entire_seat_grid(previous)
        if previous != current:
            previous = current
        else:
            break
    return len([seat for seat in previous.values() if seat == '#'])

@pytest.mark.parametrize(
    "seats,expected_result", [
        
        (
            parse_data(
"""L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""
            ), 
            37
        ),
        (
           parsed_data, 2483 
        )
    ]
)
def test_solve_day11_part1(seats: Seats, expected_result):
    result = solve_day11_part1(seats)
    assert result == expected_result


# fn that takes in position and all seats and tells if that position is L or #   
def determines_type_of_seat_part_2(current_position: Position, seats: Seats) -> Seat:
    occupied_adjacent_seats = 0
    sees_open_seat = False
    max_x = max(key[0] for key in seats.keys())
    max_y = max(key[1] for key in seats.keys())
    
    for x in range(current_position[0] + 1, max_x + 1): #down
        try:
            if seats[(x, current_position[1])] == '#':
                occupied_adjacent_seats += 1
                break
            elif seats[(x, current_position[1])] == 'L':
                sees_open_seat = True
        except KeyError:
            pass
    for y in range(current_position[1] + 1, max_y + 1): #right
        try:
            if seats[(current_position[0], y)] == '#':
                occupied_adjacent_seats += 1
                break
            elif seats[(current_position[0], y)] == 'L':
                sees_open_seat = True
        except KeyError:
            pass
    for x in range(current_position[0] -1, -1, -1): #up
        try:
            if seats[(x, current_position[1])] == '#':
                occupied_adjacent_seats += 1
                break
            elif seats[(x, current_position[1])] ==  'L':
                sees_open_seat = True
        except KeyError:
            pass
    for y in range(current_position[1] - 1, -1, -1): #left
        try:
            if seats[(current_position[0], y)] == '#':
                occupied_adjacent_seats += 1
                break
            elif seats[(current_position[0], y)] ==  'L':
                sees_open_seat = True
        except KeyError:
            pass
    for index, x in enumerate(range(current_position[0] -1, -1, -1)): #up right
        y = current_position[1] + 1 + index
        try:
            if seats[(x, y)] == '#':
                occupied_adjacent_seats += 1
                break
            elif seats[(x, y)] ==  'L':
                sees_open_seat = True
        except KeyError:
            pass
    for index, x in enumerate(range(current_position[0] - 1, -1, -1)): #up left
        y = current_position[1] -1 - index
        try:
            if seats[(x, y)] == '#':
                occupied_adjacent_seats += 1
                break
            elif seats[(x, y)] ==  'L':
                sees_open_seat = True
        except KeyError:
            pass
    for index, x in enumerate(range(current_position[0] + 1 , max_x + 1)): #down right
        y = current_position[1] + 1 + index
        try:
            if seats[(x, y)] == '#':
                occupied_adjacent_seats += 1
                break
            elif seats[(x, y)] ==  'L':
                sees_open_seat = True
        except KeyError:
            pass
    for index, x in enumerate(range(current_position[0] +  1, max_x + 1)): #down left
        y = current_position[1] - 1 - index
        try:
            if seats[(x, y)] == '#':
                occupied_adjacent_seats += 1
                break
            elif seats[(x, y)] ==  'L':
                sees_open_seat = True
        except KeyError:
            pass

    if seats[current_position] == 'L' and sees_open_seat:
        return '#'

    if seats[current_position] == '#' and occupied_adjacent_seats >= 5:
        return 'L'

    return seats[current_position]

@pytest.mark.parametrize(
    "position,seats,expected_result", [
        (
            (1,1),
            parse_data(
""".............
.L.L.#.#.#.#.
............."""
            ),
            "#"
        ),
        (
            (4,3),
            parse_data(
""".......#.
...#.....
.#.......
.........
..##....#
....#....
.........
#........
...#....."""
            ),
            "L"

        ),
        (
            (7,9),
            parse_data(
"""#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##"""
            ),
            "#"
        ),
        (
            (1,9),
            parse_data(
"""#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##"""
            ),
            "L"
        ),
        (
            (0, 8),
            parse_data(
"""#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##"""
            ),
            "L"
        )
       
    ]
)
def test_determines_type_of_seat_part_2(position: Position, seats: Seats, expected_result: Seat):
    result = determines_type_of_seat_part_2(position, seats)
    assert result == expected_result

def calculate_entire_seat_grid_part_2(seats: Seats) -> Seats:
    new_seats: Seats = {}
    for position in seats.keys():
        new_seats[position] = determines_type_of_seat_part_2(position, seats)
    return new_seats

@pytest.mark.parametrize(
    "seats,expected_result", [
        (
           parse_data(
"""L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""
            ),
           parse_data(
"""#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##"""
            ),
 
        ),
        (
            parse_data(
"""#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##"""
            ),
            parse_data(
"""#.LL.LL.L#
#LLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLLL.L
#.LLLLL.L#"""
            ),
        )
    ]
)
def test_calculate_entire_seat_grid_part2(seats: Seats, expected_result: Seat):
    result = calculate_entire_seat_grid_part_2(seats)
    assert result == expected_result

# def solve_day11_part2(seats:Seats) -> int:
#     previous = calculate_entire_seat_grid_part_2(seats)
#     while True:
#         current = calculate_entire_seat_grid_part_2(previous)
#         if previous != current:
#             previous = current
#         else:
#             break
#     return len([seat for seat in previous.values() if seat == '#'])
# @pytest.mark.only
# @pytest.mark.parametrize(
#     "seats,expected_result", [
        
#         (
#             parse_data(
# """L.LL.LL.LL
# LLLLLLL.LL
# L.L.L..L..
# LLLL.LL.LL
# L.LL.LL.LL
# L.LLLLL.LL
# ..L.L.....
# LLLLLLLLLL
# L.LLLLLL.L
# L.LLLLL.LL"""
#             ), 
#             26
#         ),
#         # (
#         #    parsed_data, 2483 
#         # )
#     ]
# )
# def test_solve_day11_part2(seats: Seats, expected_result):
#     result = solve_day11_part2(seats)
#     assert result == expected_result
