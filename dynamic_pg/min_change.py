# time runout bruteforce solution
def min_change(amount, coins):
    if amount < 0:
        return float("inf")
    if amount == 0:
        return 0
    min_coins = float("inf")

    for coin in coins:
        num_coins = 1 + min_change(amount - coin, coins)
        if num_coins < min_coins:
            min_coins = num_coins
    return min_coins                


# with memoization
def min_change(amount, coins):
  result = _min_change(amount, coins, {})
  if result == float('inf'):
    return -1
  else: 
    return result  
def _min_change(amount, coins, memo):
    if amount in memo:
      return memo[amount]
    if amount < 0:
        return float('inf')
    if amount == 0:
        return 0
    min_coins = float('inf')

    for coin in coins:
        num_coins = 1 + _min_change(amount - coin, coins, memo)
        if num_coins < min_coins:
            min_coins = num_coins
    memo[amount] = min_coins      
    return min_coins  
