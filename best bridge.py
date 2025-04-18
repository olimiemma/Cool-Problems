best bridge
Write a function, best_bridge, that takes in a grid as an argument. The grid contains water (W) and land (L). There are exactly two islands in the grid. An island is a vertically or horizontally connected region of land. Return the minimum length bridge needed to connect the two islands. A bridge does not need to form a straight line.


grid = [
  ["W", "W", "W", "L", "L"],
  ["L", "L", "W", "W", "L"],
  ["L", "L", "L", "W", "L"],
  ["W", "L", "W", "W", "W"],
  ["W", "W", "W", "W", "W"],
  ["W", "W", "W", "W", "W"],
]
best_bridge(grid) # -> 1




grid = [
  ["W", "W", "W", "W", "W", "W", "W", "W"],
  ["W", "W", "W", "W", "W", "W", "W", "W"],
  ["W", "W", "W", "W", "W", "W", "W", "W"],
  ["W", "W", "W", "W", "W", "L", "W", "W"],
  ["W", "W", "W", "W", "L", "L", "W", "W"],
  ["W", "W", "W", "W", "L", "L", "L", "W"],
  ["W", "W", "W", "W", "W", "L", "L", "L"],
  ["L", "W", "W", "W", "W", "L", "L", "L"],
  ["L", "L", "L", "W", "W", "W", "W", "W"],
  ["W", "W", "W", "W", "W", "W", "W", "W"],
]
best_bridge(grid) # -> 3


grid = [
  ["W", "L", "W", "W", "W", "W", "W", "W"],
  ["W", "L", "W", "W", "W", "W", "W", "W"],
  ["W", "W", "W", "W", "W", "W", "W", "W"],
  ["W", "W", "W", "W", "W", "W", "W", "W"],
  ["W", "W", "W", "W", "W", "W", "W", "W"],
  ["W", "W", "W", "W", "W", "W", "L", "W"],
  ["W", "W", "W", "W", "W", "W", "L", "L"],
  ["W", "W", "W", "W", "W", "W", "W", "L"],
]
best_bridge(grid) # -> 8




#sol


from collections import deque

def best_bridge(grid):
  main_island = None
  for r in range(len(grid)): #iterating thru evry row and column
    for c in range(len(grid[0])):
      potential_island = traverse_island(grid, r, c, set()) #some traversal
      if len(potential_island) > 0:
        main_island = potential_island
  
  visited = set(main_island) #breadth first to go from one insaldn to another
  queue = deque([ ])
  for pos in main_island:
    r, c = pos
    queue.append((r, c, 0))
  
  while queue:
    row, col, distance = queue.popleft() #grabs item of qu, positiona dn sitance
    if grid[row][col] == 'L' and (row, col) not in main_island:   #checking if position is equal to land 
      return distance - 1
    
    deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)] #going thru neighboirs
    for delta in deltas:
      delta_row, delta_col = delta
      neighbor_row = row + delta_row
      neighbor_col = col + delta_col
      neighbor_pos = (neighbor_row, neighbor_col)
      if inbounds(grid, neighbor_row, neighbor_col) and neighbor_pos not in visited: #checking is neighboirsis in bound and not yet visted, then viste them
        visited.add(neighbor_pos)
        queue.append((neighbor_row, neighbor_col, distance + 1))
  
def inbounds(grid, row, col): #checkibg if we are checking if you have right and down neighbor but no up and left neighbor
  row_inbounds = 0 <= row < len(grid)
  col_inbounds = 0 <= col < len(grid[0])
  return row_inbounds and col_inbounds
  
def traverse_island(grid, row, col, visited): #depth traversing thru the grid
  if not inbounds(grid, row, col) or grid[row][col] == 'W': #makimg it only go through land
    return visited
  
  pos = (row, col) #checking of ee visited
  if pos in visited:
    return visited
  
  visited.add(pos) #if its 1st time, add to visited 
  
   #traversing thru all neighbors of this piece of land
  traverse_island(grid, row - 1, col, visited)
  traverse_island(grid, row + 1, col, visited)
  traverse_island(grid, row, col - 1, visited)
  traverse_island(grid, row, col + 1, visited)
  return visited # rteurns a set of all memebrs in the island
