# Function to find the middle node of a linked list
def middle_linked_list(head):

    # Initialize slow and fast pointers at the head
    slow = head
    fast = head

    # Move slow one step and fast two steps at a time
    # until fast reaches the end of the linked list
    while fast is not None and fast.next is not None:

        # Move slow pointer one node forward
        slow = slow.next

        # Move fast pointer two nodes forward
        fast = fast.next.next

    # When fast reaches the end,
    # slow will be pointing to the middle node
    return slow
