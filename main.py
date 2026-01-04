def coin_change(amount, coins):
    #  so if the amount is 0, we need no coins.
    if amount == 0:
        return 0
    
    # dp[i] = minimum number of coins needed to make amount i
    # sstart everything as "super large" (amount + 1)
    dp = [amount + 1] * (amount + 1)

    # we know how to build o -> takes 0 coins
    dp[0] = 0

    # start from 1 up through the target amount
    for current in range(1, amount + 1):
        # try every coin
        for coin in coins:
            # only consider this coin if it doesn't overshoot
            # if i use this coin
            # that means i look at the best answer for current - coin.
            # add 1 coin (cuz i just used one)
            if current - coin >= 0:
                dp[current] = min(dp[current], 1 + dp[current - coin])
    # if this is still "super large", then we never found a solution
    return dp[amount] if dp[amount] != amount + 1 else -1


### Test Case #1

amount = 11
coins = [1,2,5]

assert coin_change(amount, coins) == 3

### Test Case #2

amount = 3
coins = [2]

assert coin_change(amount, coins) == -1

### Test Case #3

amount = 0
coins = [1]

assert coin_change(amount, coins) == 0

print("All tests passed!")
print("Discuss time & space complexity if time remains.")
