
# time runout
def sum_possible(amount, numbers):
    if amount < 0:
        return False
    if amount == 0:
        return True
    for num in numbers:
        if sum_possible(amount - num, numbers) is True:
            return True
    return False


# corrected one with memoization
def sum_possible(amount, numbers):
  return _sum_possible(amount, numbers, {})
def _sum_possible(amount, numbers, memo):
  if amount in memo:
    return memo[amount]
  if amount < 0:
    return False
  if amount == 0:
    return True
  for num in numbers:
    if _sum_possible(amount - num, numbers, memo) is True:
      memo[amount] = True
      return True
  memo[amount] = False
  return False