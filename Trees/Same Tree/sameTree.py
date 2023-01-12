def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]
        while stack:
            n1, n2 = stack.pop()
            if n1 and n2 and n1.val == n2.val:
                stack.append((n1.left, n2.left))
                stack.append((n1.right, n2.right))
            elif not n1 and not n2:
                continue
            else:
                return False
        return True
