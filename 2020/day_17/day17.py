import pytest
from typing import List

Coordinate = tuple[int, int, int]

Dimension = dict[Coordinate, bool]

Cycles = list[Dimension]

# with open("input.txt", "r") as input_data:
#     string_input = input_data.read()
#     parsed_data: List[int] = [int(line) for line in string_input.splitlines()]


def solve_day17_part1():
    pass


# 8x8x3
# 1 fn generate top and bottom layer to start using ranges
# 1 fn generate the initial coordinates using nested for loop so we can check the neighbors
# 1 fn to generate all 26 neighbors for any point ✅
# 1 fn that given coordinate, gets neighbor, then create the cycle, flip/not flip active state and returns a dimension
# 1 fn that generate list of cycles given 1st dimension (takes in initial state, 6, and spits out cycles type) (loops fn above 6x)



def get_neighbors(coordinate: Coordinate, dimension: Dimension) -> Dimension:
    dim: Dimension = {}
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            for z in [-1, 0, 1]:
                if (x, y,z) == (0,0,0):
                    continue
                coor_x, coor_y, coor_z = coordinate
                neighbor = (coor_x + x, coor_y +y, coor_z + z)

                dim[neighbor] = dimension[neighbor]
    return dim

@pytest.mark.parametrize(
    "coordinate,dimension,expected_result",
    [
        (
            (1, 1, 0),
            {
                (0, 0, 0): True,
                (1, 0, 0): True,
                (2, 0, 0): True,
                (0, 1, 0): True,
                (1, 1, 0): True,
                (2, 1, 0): True,
                (0, 2, 0): True,
                (1, 2, 0): True,
                (2, 2, 0): True,
                (0, 0, -1): True,
                (1, 0, -1): True,
                (2, 0, -1): True,
                (0, 1, -1): True,
                (1, 1, -1): True,
                (2, 1, -1): True,
                (0, 2, -1): True,
                (1, 2, -1): True,
                (2, 2, -1): True,
                (0, 0, 1): True,
                (1, 0, 1): True,
                (2, 0, 1): True,
                (0, 1, 1): True,
                (1, 1, 1): True,
                (2, 1, 1): True,
                (0, 2, 1): True,
                (1, 2, 1): True,
                (2, 2, 1): True,
            },
            {
                (0, 0, 0): True,
                (1, 0, 0): True,
                (2, 0, 0): True,
                (0, 1, 0): True,
                (2, 1, 0): True,
                (0, 2, 0): True,
                (1, 2, 0): True,
                (2, 2, 0): True,
                (0, 0, -1): True,
                (1, 0, -1): True,
                (2, 0, -1): True,
                (0, 1, -1): True,
                (1, 1, -1): True,
                (2, 1, -1): True,
                (0, 2, -1): True,
                (1, 2, -1): True,
                (2, 2, -1): True,
                (0, 0, 1): True,
                (1, 0, 1): True,
                (2, 0, 1): True,
                (0, 1, 1): True,
                (1, 1, 1): True,
                (2, 1, 1): True,
                (0, 2, 1): True,
                (1, 2, 1): True,
                (2, 2, 1): True,
            },
        ),
    ],
)
def test_get_neighbors(coordinate: Coordinate, dimension: Dimension, expected_result):
    result = get_neighbors(coordinate, dimension)
    assert result == expected_result

"""
# TODO WHERE TO START CUZ IT'S BROKEN:
# when calculating cycle, add inactive layers to z min and max
# when calculating cycle, pad each layers with an inactive square 

###
###
### 
---> 
.....
.###.
.###.
.###.
..... (this doesnt include the inactive layer in front and behind of this representation)

"""

def calculates_cycle(dimension: Dimension) -> Dimension:
    dim: Dimension = {}
    for coordinate, state in dimension.items():
        neighbors: Dimension  = get_neighbors(coordinate, dimension)
        current_cube_state: bool = state
        num_active_neighbors = sum([int(neighbor) for neighbor in neighbors.values()])
        if current_cube_state is True:
            if num_active_neighbors in (2, 3):
                current_cube_state = True
            else:
                current_cube_state = False
        else:
            if num_active_neighbors == 3:
                current_cube_state = True
            else:
                current_cube_state = False
        dim[coordinate] = current_cube_state
    return dim

@pytest.mark.parametrize(
    "dimension,expected_result",
    [
        (
            {
                (0, 0, 0): False,
                (1, 0, 0): True,
                (2, 0, 0): False,

                (0, 1, 0): False,
                (1, 1, 0): False,
                (2, 1, 0): True,

                (0, 2, 0): True,
                (1, 2, 0): True,
                (2, 2, 0): True,

                (0, 0, -1): False,
                (1, 0, -1): False,
                (2, 0, -1): False,
                (0, 1, -1): False,
                (1, 1, -1): False,
                (2, 1, -1): False,
                (0, 2, -1): False,
                (1, 2, -1): False,
                (2, 2, -1): False,
                (0, 0, 1): False,
                (1, 0, 1): False,
                (2, 0, 1): False,
                (0, 1, 1): False,
                (1, 1, 1): False,
                (2, 1, 1): False,
                (0, 2, 1): False,
                (1, 2, 1): False,
                (2, 2, 1): False,
            },
            {
                (0, 0, 0): True,
                (1, 0, 0): False,
                (2, 0, 0): True,

                (0, 1, 0): False,
                (1, 1, 0): False,
                (2, 1, 0): True,

                (0, 2, 0): False,
                (1, 2, 0): True,
                (2, 2, 0): False,
                
                (0, 0, -1): True,
                (1, 0, -1): False,
                (2, 0, -1): False,

                (0, 1, -1): False,
                (1, 1, -1): False,
                (2, 1, -1): True,

                (0, 2, -1): False,
                (1, 2, -1): True,
                (2, 2, -1): False,

                (0, 0, 1): True,
                (1, 0, 1): False,
                (2, 0, 1): False,

                (0, 1, 1): False,
                (1, 1, 1): False,
                (2, 1, 1): True,

                (0, 2, 1): False,
                (1, 2, 1): True,
                (2, 2, 1): False,
            }
        ),
    ],
)
def test_calculates_cycle(dimension: Dimension, expected_result):
    result = calculates_cycle(dimension)
    assert result == expected_result