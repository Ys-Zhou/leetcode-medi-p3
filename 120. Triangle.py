# Runtime: 56 ms, faster than 32.78% of Python3 online submissions


class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle) == 1:
            return triangle[0][0]
        last_path = triangle[0]
        for row in range(1, len(triangle)):
            now_path = []
            now_row = triangle[row]
            for idx in range(row + 1):
                if idx == 0:
                    now_path.append(last_path[0] + now_row[0])
                elif idx == row:
                    now_path.append(last_path[idx - 1] + now_row[idx])
                else:
                    now_path.append(min(last_path[idx - 1], last_path[idx]) + now_row[idx])
            last_path = now_path
        return min(last_path)
