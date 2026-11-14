class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        seen = set()
        longest = 0

        def bfs(r, c) -> int:
            q = collections.deque()
            seen.add((r,c))
            q.append((r,c))
            count = 1

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [0,1], [-1,0], [0,-1]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if(r in range(rows) and c in range(cols) and grid[r][c] == 1 and (r,c) not in seen):
                        q.append((r,c))
                        seen.add((r,c))
                        count+=1
            return count



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in seen:
                    longest = max(bfs(r,c), longest)
        return longest