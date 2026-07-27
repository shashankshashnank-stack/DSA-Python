"""
Detect Cycle in a Linked List using Floyd's Cycle Detection Algorithm
---------------------------------------------------------------
Algorithm:
1. Initialize two pointers:
   - slow: moves one node at a time.
   - fast: moves two nodes at a time.
2. Traverse the linked list.
3. If slow and fast meet, a cycle exists.
4. If fast reaches the end (None), no cycle exists.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def detect_cycle(head):
    """
    Detects whether a linked list contains a cycle.

    Args:
        head (Node): Head node of the linked list.

    Returns:
        bool: True if a cycle exists, otherwise False.
    """

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next          # Move one step
        fast = fast.next.next     # Move two steps

        if slow == fast:
            return True

    return False


# ---------------- Example Usage ---------------- #

# Create Linked List:
# 10 -> 20 -> 30 -> 40
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

# Create a cycle:
# 40 -> 20
head.next.next.next.next = head.next

if detect_cycle(head):
    print("Cycle Detected")
else:
    print("No Cycle Detected")
