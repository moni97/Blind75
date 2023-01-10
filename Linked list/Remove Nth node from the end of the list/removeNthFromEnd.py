def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        newNode = ListNode(0)
        newNode.next = head
        left = right = newNode
        # print(left)
        while n >= 0:
            right = right.next
            n -= 1
        while right:
            left = left.next
            right = right.next
        # print(left, right)
        left.next = left.next.next
        return newNode.next
