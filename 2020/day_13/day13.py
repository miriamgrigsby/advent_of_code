import pytest
from typing import List, Literal, Tuple, final
from dataclasses import dataclass
import math
from collections import Counter


@dataclass
class BusInfo:
    earliest_departure: int
    bus_ids: List[int]

def parse_data(string_input: str) -> BusInfo:
    earliest_departure, bus_ids = string_input.splitlines()
    filtered_bus_ids = [int(id) for id in bus_ids.split(',') if id != 'x']
    
    return BusInfo(earliest_departure=int(earliest_departure), bus_ids=filtered_bus_ids)
    
with open("input.txt", "r") as input_data:
    parsed_data = parse_data(input_data.read())

def solve_day13_part1(bus_info: BusInfo) -> int:
    counter = Counter()
    for bus_id in bus_info.bus_ids:
        counter.update({bus_id: bus_id * (math.ceil(bus_info.earliest_departure / bus_id))})
    final_bus_id, minimum_difference = counter.most_common()[-1]
    total_time_difference = minimum_difference - bus_info.earliest_departure
    return total_time_difference * final_bus_id

@pytest.mark.parametrize("bus_info,expected_result", [
    (
        BusInfo(earliest_departure=24, bus_ids=[7,20]),
        28
    ),
    (
        BusInfo(earliest_departure=939, bus_ids=[7,13,59,31,19]),
        295
    ),
    (
        parsed_data,
        5946
    ),
   
])
def test_solve_day13_part1(bus_info: BusInfo, expected_result: int):
    result = solve_day13_part1(bus_info)
    assert result == expected_result


def solve_day13_part2(bus_info: BusInfo):
    pass
    # NOTE: This is stupid, it requires mathematics, probably the extended euclidian algo or chinese remainder theorem
