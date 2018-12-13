# Runtime: 48 ms, faster than 53.62% of Python3 online submissions


class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            if token == '+':
                stack.append(stack.pop() + stack.pop())
                continue
            if token == '-':
                second = stack.pop()
                first = stack.pop()
                stack.append(first - second)
                continue
            if token == '*':
                stack.append(stack.pop() * stack.pop())
                continue
            if token == '/':
                second = stack.pop()
                first = stack.pop()
                stack.append(int(first / second))
                continue
            stack.append(int(token))
        return stack
