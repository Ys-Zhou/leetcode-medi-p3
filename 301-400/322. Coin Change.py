# Runtime: 1288 ms, faster than 67.29% of Python3 online submissions
# Memory Usage: 13.9 MB, less than 20.46% of Python3 online submissions


class Solution:
    # DP
    def coinChange(self, coins: list, amount: int) -> int:
        coins.sort()
        dp = [0] + [amount + 1] * amount
        for i in range(1, amount + 1):
            for coin in coins:
                if i < coin:
                    break
                dp[i] = min(dp[i], dp[i - coin] + 1)
        if dp[-1] == amount + 1:
            return -1
        return dp[-1]

    # BFS but TLE
    def coinChange_(self, coins: list, amount: int) -> int:
        if amount == 0:
            return 0
        if amount in coins:
            return 1
        coins.sort()
        dep = 1
        current = [(x, coins[x]) for x in range(len(coins))]  # (index, sum)
        while current:
            dep += 1
            next_ = list()
            for node in current:
                for i in range(node[0] + 1):
                    sum_ = node[1] + coins[i]
                    if sum_ == amount:
                        return dep
                    if sum_ < amount:
                        next_.append((i, sum_))
            current = next_
        return -1
