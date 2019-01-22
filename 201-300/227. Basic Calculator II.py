# Runtime: 192 ms, faster than 22.60% of Python3 online submissions


class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = ''
        num_stack = []
        opt_stack = []
        for c in s + '#':
            if c == ' ':
                continue
            if c == '+' or c == '-' or c == '#':
                num_stack.append(int(num))
                num = ''
                while opt_stack:
                    opt = opt_stack.pop()
                    num_b = num_stack.pop()
                    num_a = num_stack.pop()
                    if opt == '*':
                        num_stack.append(num_a * num_b)
                    elif opt == '/':
                        num_stack.append(num_a // num_b)
                    elif opt == '+':
                        num_stack.append(num_a + num_b)
                    elif opt == '-':
                        num_stack.append(num_a - num_b)
                opt_stack.append(c)
                continue
            if c == '*' or c == '/':
                num_stack.append(int(num))
                num = ''
                while opt_stack and (opt_stack[-1] == '*' or opt_stack[-1] == '/'):
                    opt = opt_stack.pop()
                    num_b = num_stack.pop()
                    num_a = num_stack.pop()
                    if opt == '*':
                        num_stack.append(num_a * num_b)
                    elif opt == '/':
                        num_stack.append(num_a // num_b)
                opt_stack.append(c)
                continue
            num += c
        return num_stack[0]
