# Coins Problem

Problem belonging to the post-classroom Mock Interview Question Repository.

## Problem Statement

We are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`.

Assume that there is an infinite number of each kind of coin.

For example, given a `coins` list of `[1, 2, 5]` and an `amount` of `11`, the function should return `3` because we can make `11` with `5`, `5`, and `1` coins. Notice that `5` is used twice. There are other ways to make `11`, but all require more coins.

## Examples

### Example 1

```py
amount = 11
coins = [1,2,5]
coin_change(amount, coins)
```

Produces

```py
3
```

### Example 2

```py
amount = 3
coins = [2]
coin_change(amount, coins)
```

Produces

```py
-1
```

### Example 3

```py
amount = 0
coins = [1]
coin_change(amount, coins)
```

Produces

```py
0
```
