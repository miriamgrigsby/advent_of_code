import pytest
from typing_extensions import NotRequired
from typing import List, TypedDict
import re

class Passport(TypedDict):
    byr: NotRequired[str]
    iyr: NotRequired[str]
    eyr: NotRequired[str]
    hgt: NotRequired[str]
    hcl: NotRequired[str]
    ecl: NotRequired[str]
    pid: NotRequired[str]
    cid: NotRequired[str]

AllPassports = List[Passport]

parsed_data: AllPassports = []

with open("input.txt", "r") as input_data:
    string_input = input_data.read()
    split_data = string_input.splitlines()
    passport_dict: Passport = {}
    for line in split_data:
        if len(line):
            list_key_value_pairs = line.split(' ')
            for key_value_pairs in list_key_value_pairs:
                key, value = key_value_pairs.split(":")
                passport_dict[key] = value
        else:
            parsed_data.append(passport_dict)
            passport_dict = {}
    parsed_data.append(passport_dict)
        
def solve_day4_part1(parsed_data) -> int:
    official_dict = [
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid"
    ]

    valid_passports = 0
    for passport in parsed_data:
        for official_key in official_dict:
            try:
                passport[official_key]
            except KeyError:
                break
        else: 
            valid_passports += 1

    return valid_passports

@pytest.mark.parametrize('parsed_data,expected_result', [
    (
        [{'ecl': 'gry', 'pid': '860033327', 'eyr': '2020', 'hcl': '#fffffd', 'byr': '1937', 'iyr': '2017', 'cid': '147', 'hgt': '183cm'}, {'iyr': '2013', 'ecl': 'amb', 'cid': '350', 'eyr': '2023', 'pid': '028048884', 'hcl': '#cfa07d', 'byr': '1929'}, {'hcl': '#ae17e1', 'iyr': '2013', 'eyr': '2024', 'ecl': 'brn', 'pid': '760753108', 'byr': '1931', 'hgt': '179cm'}, {'hcl': '#cfa07d', 'eyr': '2025', 'pid': '166559648', 'iyr': '2011', 'ecl': 'brn', 'hgt': '59in'}],
        2
    ),
    (
        [],
        0
    ),
    (
        [{'ecl': 'gry', 'pid': '860033327', 'eyr': '2020', 'hcl': '#fffffd'}],
        0
    ),
    (
        [{'ecl': 'gry', 'pid': '860033327', 'eyr': '2020', 'hcl': '#fffffd', 'byr': '1937', 'iyr': '2017', 'hgt': '183cm'}],
        1
    ),
    (
       parsed_data,
        208
    )
])
def test_solve_day4_part1(parsed_data, expected_result):
    result = solve_day4_part1(parsed_data)
    assert result == expected_result 

def solve_day4_part2(parsed_data) -> int:
    official_dict = [
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid"
    ]
    valid_eye_color = [
        "amb", "blu", "brn", "gry", "grn", "hzl", "oth"
    ]

    valid_passports = 0
    hgt_cm_regex = re.compile('^[\\d]{3}cm$')
    hgt_in_regex = re.compile('^[\\d]{2}in$')
    hcl_regex = re.compile('^#[0-9a-f]{6}$')
    pid_regex = re.compile('^[0-9]{9}$')

    for passport in parsed_data:
        for official_key in official_dict:
            try:
                passport[official_key]
            except KeyError:
                break
        else: 
            passport_byr = int(passport['byr'])
            passport_iyr = int(passport['iyr'])
            passport_eyr = int(passport['eyr'])
            if passport_byr < 1920 or passport_byr > 2002:
                continue
            if passport_iyr < 2010 or passport_iyr > 2020:
                continue
            if passport_eyr < 2020 or passport_eyr > 2030:
                continue
            if passport['ecl'] not in valid_eye_color:
                continue
            if hgt_cm_regex.match(passport['hgt']):
                hgt_int = int(passport['hgt'].replace("cm", ""))
                if hgt_int < 150 or hgt_int > 193:
                    continue
            elif hgt_in_regex.match(passport['hgt']):
                hgt_int = int(passport['hgt'].replace("in", ""))
                if hgt_int < 59 or hgt_int > 76:
                    continue
            else:
                continue
            if not hcl_regex.match(passport['hcl']):
                continue
            if not pid_regex.match(passport['pid']):
                continue
            valid_passports += 1

    return valid_passports

@pytest.mark.parametrize('parsed_data,expected_result', [
    (
        [parsed_data, 167]
    ),
    (
        [{'pid': '087499704', 'hgt': '74in', 'ecl': 'grn', 'iyr': '2012', 'eyr': '2030', 'byr': '1980', 'hcl': '#623a2f'}, {'eyr': '2029', 'ecl': 'blu', 'cid': '129', 'byr': '1989', 'iyr': '2014', 'pid': '896056539', 'hcl': '#a97842', 'hgt': '165cm'}, {'hcl': '#888785', 'hgt': '164cm', 'byr': '2001', 'iyr': '2015', 'cid': '88', 'pid': '545766238', 'ecl': 'hzl', 'eyr': '2022'}, {'iyr': '2010', 'hgt': '158cm', 'hcl': '#b6652a', 'ecl': 'blu', 'byr': '1944', 'eyr': '2021', 'pid': '093154719'}],
        4
    ),
    (
        [{'eyr': '1972', 'cid': '100', 'hcl': '#18171d', 'ecl': 'amb', 'hgt': '170', 'pid': '186cm', 'iyr': '2018', 'byr': '1926'}, {'iyr': '2019', 'hcl': '#602927', 'eyr': '1967', 'hgt': '170cm', 'ecl': 'grn', 'pid': '012533040', 'byr': '1946'}, {'hcl': 'dab227', 'iyr': '2012', 'ecl': 'brn', 'hgt': '182cm', 'pid': '021572410', 'eyr': '2020', 'byr': '1992', 'cid': '277'}, {'hgt': '59cm', 'ecl': 'zzz', 'eyr': '2038', 'hcl': '74454a', 'iyr': '2023', 'pid': '3556412378', 'byr': '2007'}],
        0
    )
])
def test_solve_day4_part2(parsed_data, expected_result):
    result = solve_day4_part2(parsed_data)
    assert result == expected_result 
