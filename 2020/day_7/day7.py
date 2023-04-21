import pytest
from typing import List, Dict, Tuple, Set

AnswerInput = List[str]
RuleMapKey = Tuple[str, str]
RuleMapValue = Tuple[str, str, int]
RuleMap = Dict[RuleMapKey, List[RuleMapValue]]


with open("input.txt", "r") as input_data:
    string_input = input_data.read()
    parsed_data: AnswerInput = string_input.splitlines()
    rule_map: RuleMap = {}
    for rule in parsed_data:
        outer_bag, inner_bags = rule[:-1].split("contain")
        inner_bags_array = inner_bags.split(",")
        outer_adj, outer_color, *bags = outer_bag.strip().split(" ")
        outer_bag_tuple = (outer_adj, outer_color)
        for inner_bag in inner_bags_array:
            count, adj, color, *bags = inner_bag.strip().split(" ")
            inner_bag_tuple: RuleMapKey = (adj, color)
            try:
                inner_bag_count = int(count)
            except ValueError:
                inner_bag_count = 0
            rule_map_value: RuleMapValue = (*outer_bag_tuple, inner_bag_count)
            try:
                rule_map[inner_bag_tuple].append(rule_map_value)
            except KeyError:
                rule_map[inner_bag_tuple] = [rule_map_value]

def solve_day7_part1(
    rule_key: RuleMapKey, rule_map: RuleMap, visited: Set[RuleMapKey]
) -> int:
    try:
        bag_array = rule_map[rule_key]
        bag_count = 0
        for bag_adj, bag_color, count in bag_array:
            if count > 0 and (bag_adj, bag_color) not in visited:
                visited.add((bag_adj, bag_color))
                bag_count += (
                    solve_day7_part1((bag_adj, bag_color), rule_map, visited) + 1
                )
        return bag_count
    except KeyError:
        return 0


@pytest.mark.parametrize(
    "rule_key,rule_map,count",
    [
        (("", ""), {}, 0),
        (("shiny", "gold"), {("shiny", "gold"): []}, 0),
        (
            ("shiny", "gold"),
            {
                ("shiny", "gold"): [("mirrored", "indigo", 5)],
                (
                    "mirrored",
                    "indigo",
                ): [],
            },
            1,
        ),
        (
            ("shiny", "gold"),
            {
                ("shiny", "gold"): [("mirrored", "indigo", 5)],
                (
                    "mirrored",
                    "indigo",
                ): [("muted", "maroon", 1)],
                (
                    "muted",
                    "maroon",
                ): [],
            },
            2,
        ),
        (
            ("shiny", "gold"),
            {
                ("bright", "white"): [("light", "red", 1), ("dark", "orange", 3)],
                ("muted", "yellow"): [("light", "red", 2), ("dark", "orange", 4)],
                ("shiny", "gold"): [("bright", "white", 1), ("muted", "yellow", 2)],
                ("faded", "blue"): [
                    ("muted", "yellow", 9),
                    ("dark", "olive", 3),
                    ("vibrant", "plum", 5),
                ],
                ("dark", "olive"): [("shiny", "gold", 1)],
                ("vibrant", "plum"): [("shiny", "gold", 2)],
                ("dotted", "black"): [("dark", "olive", 4), ("vibrant", "plum", 6)],
                ("other", "bags"): [("faded", "blue", 0), ("dotted", "black", 0)],
            },
            4,
        ),
        (("shiny", "gold"), rule_map, 197),
    ],
)
def test_solve_day7_part1(rule_key: RuleMapKey, rule_map: RuleMap, count: int):
    result = solve_day7_part1(rule_key, rule_map, set())
    assert result == count


def transform_puzzle(rule_map: RuleMap) -> RuleMap:
    transformed_puzzle: RuleMap = {}
    for key_tuple, value_array in rule_map.items():
        for value_tuple_adj, value_tuple_color, value_tuple_count in value_array:
            key_adj, key_color = key_tuple
            try:
                transformed_puzzle[(value_tuple_adj, value_tuple_color)].append(
                    (key_adj, key_color, value_tuple_count)
                )
            except KeyError:
                transformed_puzzle[(value_tuple_adj, value_tuple_color)] = [
                    (key_adj, key_color, value_tuple_count)
                ]
    return transformed_puzzle

@pytest.mark.parametrize(
    "old_rule_map,expected_rule_map",
    [
        (
            {
                ("dark", "red"): [("shiny", "gold", 2)],
                ("dark", "orange"): [("dark", "red", 2)],
                ("dark", "yellow"): [("dark", "orange", 2)],
                ("dark", "green"): [("dark", "yellow", 2)],
                ("dark", "blue"): [("dark", "green", 2)],
                ("dark", "violet"): [("dark", "blue", 2)],
                ("other", "bags"): [("dark", "violet", 0)],
            },
            {
                ("shiny", "gold"): [("dark", "red", 2)],
                ("dark", "red"): [("dark", "orange", 2)],
                ("dark", "orange"): [("dark", "yellow", 2)],
                ("dark", "yellow"): [("dark", "green", 2)],
                ("dark", "green"): [("dark", "blue", 2)],
                ("dark", "blue"): [("dark", "violet", 2)],
                ("dark", "violet"): [("other", "bags", 0)],
            },
        )
    ],
)
def test_solve_transform_puzzle(old_rule_map: RuleMap, expected_rule_map: RuleMap):
    result = transform_puzzle(old_rule_map)
    assert result == expected_rule_map


def solve_day7_part2(
    rule_key: RuleMapKey, rule_map: RuleMap
) -> int:
    try:
        bag_array = rule_map[rule_key]
        bag_count = 0
        for bag_adj, bag_color, count in bag_array:
            if count > 0:
                bag_count += (
                    solve_day7_part2((bag_adj, bag_color), rule_map) + 1
                ) * count
        return bag_count
    except KeyError:
        return 0


@pytest.mark.parametrize(
    "rule_key,rule_map,count",
    [
        (
            ("shiny", "gold"),
            {
                ("dark", "red"): [("shiny", "gold", 2)],
                ("dark", "orange"): [("dark", "red", 2)],
                ("dark", "yellow"): [("dark", "orange", 2)],
                ("dark", "green"): [("dark", "yellow", 2)],
                ("dark", "blue"): [("dark", "green", 2)],
                ("dark", "violet"): [("dark", "blue", 2)],
                ("other", "bags"): [("dark", "violet", 0)],
            },
            126,
        ),
        (("shiny", "gold"), rule_map, 85324),
    ],
)
def test_solve_day7_part2(rule_key: RuleMapKey, rule_map: RuleMap, count: int):
    result = solve_day7_part2(rule_key, transform_puzzle(rule_map))
    assert result == count
