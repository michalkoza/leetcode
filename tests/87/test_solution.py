import pytest

from _87_Scramble.Scramble import Solution

test_cases = [
    ("eebaacbcbcadaaedceaaacadccd", "eadcaacabaddaceacbceaabeccd", False),
    ("great", "rgeat", True),
    ("abcde", "caebd", False),
    ("a", "a", True),
    ("a", "b", False),
]

@pytest.mark.parametrize("s1, s2, expectation", test_cases)
def test_solution(s1, s2, expectation):
    assert Solution().isScramble(s1, s2) == expectation

def generate_permutations(s):
    permutations = set()

    def inner(prefix, remaining):
        if len(remaining) == 1:
            permutations.add(prefix + remaining)
        for i in range(len(remaining)):
            inner(prefix + remaining[i], remaining[:i] + remaining[i + 1:])

    inner("", s)
    return permutations


def generate_scrambles(input):
    def scramble(s):
        if not s:
            return set()
        if len(s) == 1:
            return set(s)
        scrambles = set()
        for i in range(1, len(s)):
            sub_scrambles1 = scramble(s[:i])
            sub_scrambles2 = scramble(s[i:])
            for s1 in sub_scrambles1:
                for s2 in sub_scrambles2:
                    scrambles.add(s1 + s2)
                    scrambles.add(s2 + s1)
        return scrambles

    return scramble(input)


test_word = "abcdefg"
permutations = generate_permutations(test_word)
scrambles = sorted(generate_scrambles(test_word))
non_scrambles = sorted(permutations.difference(scrambles))



@pytest.mark.parametrize("non_scramble", non_scrambles)
def test_solution_false(non_scramble):
    assert Solution().isScramble(test_word, non_scramble) == False, non_scramble


@pytest.mark.parametrize("scramble", scrambles)
def test_solution_true(scramble):
    assert Solution().isScramble(test_word, scramble) == True, scramble

