def isValidBST(self, root: Optional[TreeNode]) -> bool:
        minV = -math.inf
        maxV = math.inf
        stack = [(root, minV, maxV)]
        while stack:
            node, mini, maxi = stack.pop()
            if node:
                if mini < node.val < maxi:
                    stack.append((node.left, mini, node.val))
                    stack.append((node.right, node.val, maxi))
                else:
                    return False
            else:
                continue
        return True
