import pytest
import typing

with open("input.txt", "r") as input_data:
    string_input = input_data.read()

parsed_data: typing.List[typing.Tuple[str, int]] = []

for s in string_input.splitlines():
    direction, magnitude = s.split(' ') 
    parsed_data.append((direction, int(magnitude)))

# we have read in a tuple (direction, magnitude(int))
