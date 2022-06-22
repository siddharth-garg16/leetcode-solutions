class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0

        s = 0
        n = len(needle)

        while n <= len(haystack):
            if haystack[s:n] == needle:
                return s
            s += 1
            n += 1

        return -1