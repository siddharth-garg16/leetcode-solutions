class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return '0'
        stack=[]
        op = '+'
        num = 0
        for e,i  in enumerate(s):
            if i =="":
                continue
            if i.isdigit():
                num = num * 10 + int(i)
            if i in "+-*/" or e==len(s)-1:
                if op =='-':
                    stack.append(-num)
                elif op=='+':
                    stack.append(num)
                elif op=='*':
                    stack.append(stack.pop()*num)
                else:
                    stack.append(int(stack.pop()/num))
                op=i
                num=0
        return sum(stack)