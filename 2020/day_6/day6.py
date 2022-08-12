import pytest
from typing import List
from collections import Counter

AnswerInput = List[str]
PersonalAnswers = List[str]
GroupAnswers = List[PersonalAnswers]
AllAnswers = List[GroupAnswers]

with open("input.txt", "r") as input_data:
    string_input = input_data.read()
    parsed_data: AnswerInput = string_input.splitlines()
    all_answers = []
    group_answers = []
    for personal_answer in parsed_data:
        personal_answers = list(personal_answer)
        if len(personal_answers) > 0:
            group_answers.append(personal_answers)
        else:
            all_answers.append(group_answers)
            group_answers = []
    else:
        if len(group_answers) > 0:
            all_answers.append(group_answers)

def calculate_group_answers(group_answers: GroupAnswers) -> int:
    return len(set([personal_answer for group_answer in group_answers for personal_answer in group_answer]))

@pytest.mark.parametrize('group_answers,expected_result', 
    [
        (
            [["a","b","c"]],
            3
        ),
        (
            [["a"], ["b"], ["c"]],
            3
        ),
        (
            [["a","b"], ["a", "c"]],
            3
        ),
        (
            [["a"], ["a"], ["a"]],
            1
        ),
        
    ]
)
def test_solve_calculate_group_answers(group_answers: GroupAnswers, expected_result: int):
    result = calculate_group_answers(group_answers)
    assert result == expected_result

def solve_day6_part1(all_answers: AllAnswers) -> int:
    return sum([calculate_group_answers(group_answer) for group_answer in all_answers])

@pytest.mark.parametrize('all_answers,expected_result', 
    [
        (
            [
                [["a","b","c"]],
                [["a"], ["b"], ["c"]],
                [["a", "b"], ["a", "c"]],
                [["a"], ["a"], ["a"], ["a"]],
                [["b"]]
            ],
            11
        ),  
        (
            all_answers,
            6565
        )
    ]
)
def test_solve_day6_part1(all_answers: AllAnswers, expected_result: int):
    result = solve_day6_part1(all_answers)
    assert result == expected_result

def calculate_group_answers_with_filter(group_answers: GroupAnswers) -> int:
    flattened_array = [personal_answer for group_answer in group_answers for personal_answer in group_answer]

    return len([key for key, value in Counter(flattened_array).items() if value == len(group_answers)])


@pytest.mark.parametrize('group_answers,expected_result', 
    [
        (
            [["a","b","c"]],
            3
        ),
        (
            [["a"], ["b"], ["c"]],
            0
        ),
        (
            [["a","b"], ["a", "c"]],
            1
        ),
        (
            [["a"], ["a"], ["a"]],
            1
        ),
        (
            [["b"]],
            1
        )
    ]
)
def test_solve_calculate_group_answers_with_filter(group_answers: GroupAnswers, expected_result: int):
    result = calculate_group_answers_with_filter(group_answers)
    assert result == expected_result


def solve_day6_part2(all_answers: AllAnswers) -> int:
    return sum([calculate_group_answers_with_filter(group_answer) for group_answer in all_answers])


@pytest.mark.parametrize('all_answers,expected_result', 
    [
        (
            [
                [["a","b","c"]],
                [["a"], ["b"], ["c"]],
                [["a", "b"], ["a", "c"]],
                [["a"], ["a"], ["a"], ["a"]],
                [["b"]]
            ],
            6
        ),  
        (
            all_answers,
            3137
        )
    ]
)
def test_solve_day6_part2(all_answers: AllAnswers, expected_result: int):
    result = solve_day6_part2(all_answers)
    assert result == expected_result
