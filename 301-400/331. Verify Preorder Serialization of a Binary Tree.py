# Runtime: 48 ms, faster than 40.91% of Python3 online submissions
# Memory Usage: 14.1 MB, less than 5.00% of Python3 online submissions


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        node_stack = []

        def append_sharp():
            if len(node_stack) >= 2 and node_stack[-1] == '#' and node_stack[-2] != '#':
                node_stack.pop()
                node_stack.pop()
                append_sharp()
            else:
                node_stack.append('#')

        tmp = ''
        for c in preorder + ',':
            if c == ',':
                if tmp == '#':
                    append_sharp()
                else:
                    node_stack.append(tmp)
                tmp = ''
            else:
                tmp += c

        if len(node_stack) == 1 and node_stack[0] == '#':
            return True
        return False
