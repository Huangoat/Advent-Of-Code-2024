grid = [list(i.strip()) for i in open("day6.in","r").readlines()]
from copy import deepcopy
import sys
sys.setrecursionlimit(9999)
x, y = 0,0
for i,v in enumerate(grid):
    for ii,vv in enumerate(v):
        if vv=="^": x,y = i,ii; break
from collections import deque

direction = (-1,0)
directions = [(-1,0),(0,1),(1,0),(0,-1)]

def right(direction, directions):
    return directions[(directions.index(direction)+1)%4]

print(right(direction, directions))
visited = set()
queue = deque([(x, y, 0)])
nx, ny = x, y
def rec(nx, ny, grid, direction, c, visited):

    if (nx,ny, direction) in visited: return False
    else: c = 0
    visited.add((nx,ny, direction))
    if nx<0 or nx>len(grid)-1 or ny<0 or ny>len(grid[0])-1:
        return True
    nextx, nexty = nx + direction[0], ny + direction[1]
    if 0<=nextx<=len(grid)-1 and 0<=nexty<=len(grid)-1:
        if grid[nextx][nexty] == "#":
            direction = right(direction, directions)
            return rec(nx, ny, grid, direction, c+1, visited)
        else:
            nx, ny = nextx, nexty 
            return rec(nx, ny, grid, direction, c+1, visited)
    else:
        return True

a = 0
for i,v in enumerate(grid):
    print(i)
    for ii,vv in enumerate(v):
        if vv!="#":

            dgrid = deepcopy(grid)
            dgrid[i][ii] = "#"
            if not rec(nx, ny, dgrid, direction, 0, set()):
                a += 1

print(a)






        
