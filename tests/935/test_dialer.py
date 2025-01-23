import pytest

from _935_KnightDialer.KnightDialer import Solution

test_cases = [
    (1, 10),
    (2, 20),
    (3, 46),
    (3131, 136006598),
]


@pytest.mark.parametrize("n, exp", test_cases)
def test_find_judges(n, exp):
    assert Solution().knightDialer(n) == exp
