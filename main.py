def coin_change(amount, coins):
    pass


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
