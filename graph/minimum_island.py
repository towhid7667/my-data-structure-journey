def minimum_island(grid):
  visited = set()
  min_size = float('inf')
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      size = explore(grid, r , c , visited)
      if 0 < size and size < min_size:
          min_size = size
  return min_size  
def explore(grid, r , c , visited):
    row_inbounds = 0 <= r < len(grid)
    col_inbounds = 0 <= c < len(grid[0])

    if not row_inbounds or not col_inbounds:
        return False
    if grid[r][c] == 'W':
        return False
    if (r, c) in visited:
        return False
    visited.add((r, c))
    size = 1
    size += explore(grid, r + 1, c , visited)
    size += explore(grid, r - 1, c , visited)
    size += explore(grid, r, c + 1 , visited)    
    size += explore(grid, r, c - 1, visited)
    return size              