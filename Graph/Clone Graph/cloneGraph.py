def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew = {}
        def dfs(n):
            if n in oldToNew:
                return oldToNew[n]
            copy = Node(n.val)
            oldToNew[n] = copy
            for child in n.neighbors:
                copy.neighbors.append(dfs(child))
            return copy
        return dfs(node) if node else None
