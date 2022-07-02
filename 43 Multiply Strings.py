class Solution:
    def stoi(self, n: str) -> int:
        d = {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9
        }

        p = len(n) - 1
        ans = 0
        for i in n:
            ans += d[i] * (10 ** p)
            p -= 1
        return ans

    def itos(self, n: int):
        d = {
            0: '0',
            1: '1',
            2: '2',
            3: '3',
            4: '4',
            5: '5',
            6: '6',
            7: '7',
            8: '8',
            9: '9',
        }
        s = ''
        if n == 0: return '0'
        while (n != 0):
            s += d[n % 10]
            n //= 10

        return s[::-1]

    def multiply(self, num1: str, num2: str) -> str:
        return self.itos(self.stoi(num1) * self.stoi(num2))