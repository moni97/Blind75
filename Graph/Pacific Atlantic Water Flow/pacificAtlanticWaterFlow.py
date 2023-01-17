def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    ROWS, COLUMNS = len(heights), len(heights[0])
    pac, atl = set(), set()
    res = []
    def dfs(r, c, visit, prevHeight):
        if (r, c) in visit or r < 0 or r >= ROWS or c < 0 or c >= COLUMNS or heights[r][c] < prevHeight:
            return
        visit.add((r, c))
        dfs(r + 1, c, visit, heights[r][c])
        dfs(r - 1, c, visit, heights[r][c])
        dfs(r, c + 1, visit, heights[r][c])
        dfs(r, c - 1, visit, heights[r][c])

    for c in range(COLUMNS):
        dfs(0, c, pac, heights[0][c]) 
        dfs(ROWS - 1, c, atl, heights[ROWS - 1][c]) 

    for r in range(ROWS):
        dfs(r, 0, pac, heights[r][0]) 
        dfs(r, COLUMNS - 1, atl, heights[r][COLUMNS - 1])

    for r in range(ROWS):
        for c in range(COLUMNS):
            if (r, c) in pac and (r, c) in atl:
                res.append((r,c))
    return res
