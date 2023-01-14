def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        column = len(grid[0])
        visited = {}
        stack = []
        islandCount = 0
        def getChildren(node):
            children = []
            if node[0] - 1 >= 0:
                children.append((node[0] - 1, node[1]))
            if node[0] + 1 < rows:
                children.append((node[0] + 1, node[1]))
            if node[1] - 1 >= 0:
                children.append((node[0], node[1] - 1))
            if node[1] + 1 < column:
                children.append((node[0], node[1] + 1))
            return children
        for i in range(rows):
            for j in range(column):
                if (i,j) not in visited and grid[i][j] is "1":
                    # print('added in stack ', i, j)
                    stack.append((i,j))
                    islandCount += 1
                while stack:
                    node = stack.pop()
                    # print('node', node)
                    if node not in visited:
                        visited[node] = 1
                        children = getChildren(node)
                        for child in children:
                            if child not in visited and grid[child[0]][child[1]] is "1":
                                stack.append(child)
                              
        return islandCount
