class Solution:
    def calculate(self, s: str) -> int:
        result = 0
        stack = []
        number = 0
        sign = 1
        i = 0
        while i < len(s):

            if s[i].isdigit():
                number = 0
                while i < len(s) and s[i].isdigit():
                    number = number * 10 + int(s[i])
                    i = i + 1
                i = i - 1
                result += number * sign

            elif s[i] == '+':
                sign = 1

            elif s[i] == '-':
                sign = -1

            # start of new expression
            elif s[i] == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1

            elif s[i] == ')':
                result = result * stack.pop()
                result += stack.pop()
            i = i + 1
        return result