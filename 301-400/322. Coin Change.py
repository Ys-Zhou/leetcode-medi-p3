class Solution:
    def coinChange(self, coins: list, amount: int) -> int:
        if amount == 0:
            return 0
        if not coins:
            return -1
        coins.sort()
        combinations = []
        used_coins = [len(coins) - 1]
        used_amount = coins[-1]
        while True:
            if used_amount < amount:
                used_coins.append(used_coins[-1])
                used_amount += coins[used_coins[-1]]
            else:
                if used_amount == amount:
                    combinations.append(len(used_coins))
                pop_coin = used_coins.pop()
                used_amount -= coins[pop_coin]
                while pop_coin == 0:
                    if not used_coins:
                        break
                    pop_coin = used_coins.pop()
                    used_amount -= coins[pop_coin]
                if not used_coins:
                    break
                used_coins.append(pop_coin - 1)
                used_amount += coins[pop_coin - 1]
        if not combinations:
            return -1
        return min(combinations)
