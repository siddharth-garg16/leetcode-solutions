class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)

        last_word_length = 0

        for i in range((n - 1), -1, -1):
            if s[i] != " ":
                last_word_length += 1

            if last_word_length != 0 and s[i] == " ":
                break

        return last_word_length