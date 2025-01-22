import pytest

from _65_ValidNumber.ValidNumber import Solution

test_cases = [

    ("1e", False),
    ("2e10", True),
    ("-90E3", True),
    ("3e+7", True),
    ("+6e-1", True),
    ("53.5e93", True),
    ("0", True),
    ("e", False),
    (".", False),
    ("-123.456e789", True),
    ("abc", False),
    ("1a", False),

    ("e3", False),
    ("99e2.5", False),
    ("--6", False),
    ("-+3", False),
    ("95a54e53", False),
    ("2", True),
    ("0089", True),
    ("-0.1", True),
    ("+3.14", True),
    ("4.", True),
    ("-.9", True),
]


@pytest.mark.parametrize("n,expectation", test_cases)
def test_solution(n, expectation):
    assert Solution().isNumber(n) == expectation
