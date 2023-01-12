def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = [root]
        while queue:
            nodes = []
            for i in range(len(queue)):
                node = queue.pop(0)
                if node:
                    nodes.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if len(nodes) > 0:
                res.append(nodes)
        return res
