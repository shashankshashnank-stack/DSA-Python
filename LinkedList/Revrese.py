# Function to reverse a singly linked list
def Reverse(head):

    # Initially, there is no previous node
    prev = None

    # Start from the first node of the linked list
    curr = head

    # Continue until all nodes have been processed
    while curr:

        # Store the next node before changing the link
        next = curr.next

        # Reverse the direction of the current node's link
        curr.next = prev

        # Move prev one step forward
        prev = curr

        # Move curr one step forward using the saved next node
        curr = next

    # Return prev, which is now the new head of the reversed list
    return prev
    
    
