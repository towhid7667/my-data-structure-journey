# time runout 
def count_paths(grid):
  return _count_paths(grid, 0 , 0)

def _count_paths(grid, r , c):
  if r == len(grid) or c == len(grid[0]) or grid[r][c] == 'X':
    return 0
  if r == len(grid) - 1 and c == len(grid[0]) - 1:
    return 1

  down_count = _count_paths(grid, r + 1, c)
  right_count = _count_paths(grid, r, c + 1)
  return down_count + right_count
  

# with memoization
def count_paths(grid):
  return _count_paths(grid, 0 , 0, {})

def _count_paths(grid, r , c, memo):
  pos = (r, c)
  if pos in memo:
    return memo[pos]
  if r == len(grid) or c == len(grid[0]) or grid[r][c] == 'X':
    return 0
  if r == len(grid) - 1 and c == len(grid[0]) - 1:
    return 1

  down_count = _count_paths(grid, r + 1, c, memo)
  right_count = _count_paths(grid, r, c + 1, memo)
  memo[pos] = down_count + right_count
  return memo[pos]
  
    