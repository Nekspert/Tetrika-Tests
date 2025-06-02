from string import ascii_uppercase

import pytest

from solution import Parser, base_url


@pytest.fixture(scope='module')
def parser():
    p = Parser(base_url)
    p.parsing()
    return p


def test_not_empty_res(parser: Parser):
    assert len(parser.res) != 0
    for letter in ascii_uppercase:
        assert letter in parser.res
    print(parser.res)
    russian_letters = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ'
    for letter in russian_letters:
        assert letter in parser.res


def test_csv_result(parser: Parser):
    russian_letters = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ'
    with open('beasts.csv', encoding='utf-8') as file:
        result = file.readlines()
    print(result)
    assert len(result) == len(russian_letters) + len(ascii_uppercase)
