# https://leetcode.com/problems/evaluate-reverse-polish-notation/

from collections import deque

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = deque()
        operators = ["+", "-", "/", "*"]
        for token in tokens:
            if token in operators:
                val1 = stack.pop()
                val2 = stack.pop()
                if token == "+":
                    val = val + val2
                elif token == "-":
                    val = val2 - val1
                elif token =="/":
                    val = int(val2 / val1)
                else:
                    val = val1 * val2
            else:
                val = int(token)

            stack.append(val)

        return stack.pop()