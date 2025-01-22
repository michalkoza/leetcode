from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []

        def build_line(words: List[str]) -> str:
            if len(words) == 1:
                return build_last_line(words)

            stripped_len = sum(map(lambda word: len(word), words))
            spaces_required = maxWidth - stripped_len
            spaces_right = spaces_required // (len(words) - 1)
            num_spaces_left = spaces_required % (len(words) - 1)
            spaces_left = spaces_right + 1
            left = (" " * spaces_left).join(words[:num_spaces_left + 1])
            return (" " * spaces_right).join([left] + words[num_spaces_left + 1:])

        def build_last_line(words: List[str]) -> str:
            joined = " ".join(words)
            return joined + " " * (maxWidth - len(joined))

        words_for_line = []
        line_len = -1
        for i in range(len(words)):
            word = words[i]
            if line_len + (1 + len(word)) > maxWidth:
                result.append(build_line(words_for_line))
                words_for_line = []
                line_len = -1
            words_for_line.append(word)
            line_len += len(word) + 1

        result.append(build_last_line(words_for_line))

        return result
