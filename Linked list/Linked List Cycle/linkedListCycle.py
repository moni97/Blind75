def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = nextptr = head
        while nextptr and nextptr.next:
            curr = curr.next
            nextptr = nextptr.next.next
            if curr == nextptr:
                return True
        return False
