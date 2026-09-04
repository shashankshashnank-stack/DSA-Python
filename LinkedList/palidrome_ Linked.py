def isPalindrome(head):

    if head is None or head.next is None:
        return True

    # Find the end of the first half
    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse the second half
    second = reverse(slow.next)

    first = head

    # Compare both halves
    while second:
        if first.data != second.data:
            return False

        first = first.next
        second = second.next

    return True


def reverse(head):

    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev