class Solution:
    def strongPasswordCheckerII(self, s: str) -> bool:
        n = len(s)
        special_chars = "!@#$%^&*()-+"
        lc, uc, sc, dc = 0, 0, 0, 0

        if n < 8:
            return False

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                return False

        for i in range(n):
            if s[i] >= 'a' and s[i] <= 'z':
                lc += 1
            if s[i] >= 'A' and s[i] <= 'Z':
                uc += 1
            if s[i] >= '0' and s[i] <= '9':
                dc += 1
            if s[i] in special_chars:
                sc += 1

        return (lc and uc and sc and dc)