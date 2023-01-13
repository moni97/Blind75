def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        k_count = 0
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            curr = stack.pop()
            k_count += 1
            if k_count == k:
                return curr.val
            node = curr.right
