def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    move = head
    array = []
    newHead, prevHead = None, None
    while move and move != None:
        if newHead == None:
            newHead = ListNode(move.val)
        else:
            prevHead = newHead
            newHead = ListNode(move.val)
            newHead.next = prevHead
        move = move.next
    return newHead
