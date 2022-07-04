class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ""

        while n > 0:
            c = chr(ord('A') + (n - 1) % 26)
            res = c + res
            n = (n - 1) // 26

        return res