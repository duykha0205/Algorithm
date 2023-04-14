from collections import deque
import math
import os
import random
import re
import sys

def knightlOnAChessboard(n):
    # Create an n x n board
    board = [[0 for _ in range(n)] for _ in range(n)]
    
    
    
    # Define BFS function to find shortest path from (0,0) to (n-1,n-1)
    def bfs(x, y):
        queue = deque([(0, 0, 0)])
        visited = set([(0, 0)])
        
        # Define possible moves of the knight
        moves = [(x,y), (y,x), (-x,y), (-y,x), (x,-y), (y,-x), (-x,-y), (-y,-x)]
        
        while queue:
            a, b, steps = queue.popleft()
            if a == n-1 and b == n-1:
                return steps
            for dx, dy in moves:
                nx, ny = a + dx, b + dy
                
                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, steps+1))
                    
        return -1
    
    # Fill the board with the number of steps needed to reach each cell
    for i in range(1, n):
        for j in range(1, n):
            board[i][j] = bfs(i, j)
            
    
    # Return the board except for the bottom-right cell
    return [row[1:] for row in board[1:]]

print("-----Main-----")
res = knightlOnAChessboard(5)

for i in res:
    print(i)