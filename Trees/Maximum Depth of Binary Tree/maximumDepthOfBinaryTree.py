 def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        queue = [[root, 1]]
        while queue:
            node, val = queue.pop()
            if node:
                res = max(res, val)
                queue.append([node.left, val + 1])
                queue.append([node.right, val + 1])
        return res
