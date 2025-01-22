class Solution:
    def isNumber(self, s: str) -> bool:
        i = 0
        n = len(s)

        def match_single(options):
            nonlocal i
            if i < n and s[i] in options:
                i += 1
                return True
            return False

        def match_digits():
            nonlocal i
            digits_found = i < n and s[i].isdigit()
            while i < n and s[i].isdigit():
                i += 1
            return digits_found

        def match_number():
            digits_found = match_digits()
            match_single(["."])
            digits_found |= match_digits()
            return digits_found

        def match_exponent():
            if match_single(["e", "E"]):
                match_single(["+", "-"])
                return match_digits()
            return True

        match_single(["+", "-"])
        if match_number():
            if match_exponent():
                return i == len(s)

        return False
