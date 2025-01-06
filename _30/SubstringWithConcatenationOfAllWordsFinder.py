from collections import defaultdict, deque
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])
        words_count = len(words)
        N = len(s)
        pattern_len = word_len * words_count
        word_counter = defaultdict(int)

        final_hits = []

        for word in words:
            word_counter[word] += 1

        for offset in range(word_len):
            local_counter = word_counter.copy()
            buffer = deque()
            for i in range(offset, N - word_len + 1, word_len):
                if (word := s[i:i + word_len]) in word_counter:
                    buffer.append(word)
                    local_counter[word] -= 1
                    if local_counter[word] < 0:
                        while len(buffer):
                            word_to_drop = buffer.popleft()
                            local_counter[word_to_drop] += 1
                            if word_to_drop == word:
                                break
                    if len(buffer) == words_count:
                        if all(count == 0 for count in local_counter.values()):
                            final_hits.append(i - pattern_len + word_len)
                        word_to_drop = buffer.popleft()
                        local_counter[word_to_drop] += 1
                else:
                    if i > N - pattern_len:
                        break
                    while len(buffer):
                        word_to_drop = buffer.popleft()
                        local_counter[word_to_drop] += 1

        return final_hits
