import pytest

from solution import appearance


@pytest.fixture(scope='module')
def basic_intervals():
    return {
        'lesson': [1594663200, 1594666800],
        'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
        'tutor': [1594663290, 1594663430, 1594663443, 1594666473],
    }


@pytest.fixture(scope='module')
def no_overlap_intervals():
    return {
        'lesson': [1600000000, 1600003600],
        'pupil': [1600000000, 1600001000, 1600002000, 1600002500],
        'tutor': [1600003000, 1600003500],
    }


@pytest.fixture(scope='module')
def full_overlap_intervals():
    return {
        'lesson': [1610000000, 1610003600],
        'pupil': [1610000000, 1610003600],
        'tutor': [1610000000, 1610003600],
    }


def test_basic_overlap(basic_intervals):
    assert appearance(basic_intervals) == 3117


def test_no_overlap(no_overlap_intervals):
    assert appearance(no_overlap_intervals) == 0


def test_full_overlap(full_overlap_intervals):
    assert appearance(full_overlap_intervals) == 3600
