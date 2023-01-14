def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        def dfs(r, c, index):
            if index == len(word):
                return True
            if index > len(word) or r <0  or r >= row or c < 0 or c >= col or word[index] != board[r][c] or board[r][c] == '#':
                return False
            tmp = board[r][c]
            board[r][c] = '#'
            res = (dfs(r + 1, c, index + 1) or dfs(r - 1, c, index + 1) or dfs(r, c + 1, index + 1) or dfs(r, c-1, index + 1))
            board[r][c] = tmp
            return res
        for i in range(row):
            for j in range(col):
                if dfs(i, j, 0):
                    return True
        return False
