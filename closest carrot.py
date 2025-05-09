closest carrot
Write a function, closest_carrot, that takes in a grid, a starting row, and a starting column. In the grid, 'X's are walls, 'O's are open spaces, and 'C's are carrots. The function should return a number representing the length of the shortest path from the starting position to a carrot. You may move up, down, left, or right, but cannot pass through walls (X). If there is no possible path to a carrot, then return -1.

grid = [
  ['O', 'O', 'O', 'O', 'O'],
  ['O', 'X', 'O', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['O', 'X', 'C', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['C', 'O', 'O', 'O', 'O'],
]

closest_carrot(grid, 1, 2) # -> 4


grid = [
  ['O', 'O', 'X', 'C', 'O'],
  ['O', 'X', 'X', 'X', 'O'],
  ['C', 'X', 'O', 'O', 'O'],
];

closest_carrot(grid, 2, 2) # -> 5


grid = [
  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'X'],
  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'C'],
]

closest_carrot(grid, 0, 0) # -> -1



Solution |


from collections import deque

def closest_carrot(grid, starting_row, starting_col):
  visited =set([(starting_row, starting_col) ])
  qu = deque([(starting_row, starting_col, 0)])
  while qu:
    ro, col, dist = qu.popleft()
    if grid[ro][col] == "C":
      return dist

    deltas = [(1,0), (-1,0), (0,1), (0, -1)]
    for delta in deltas:
      delrow, delcol = delta
      nerow = ro + delrow
      necol = col + delcol
      roin = 0<= nerow < len(grid)
      colin = 0<= necol <len(grid[0])
      pos =(nerow, necol)
      if roin and colin and grid[nerow][necol] != "X" and pos not in visited:
        qu.append((nerow, necol, dist+1))
        visited.add(pos)
      

  
  return -1
