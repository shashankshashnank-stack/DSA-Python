# ------------------------------------------------------------
# Data Structure : Singly Linked List
# Operation      : Insert at Beginning
# Time           : O(1)
# Space          : O(1)
# ------------------------------------------------------------

class Node:
    """Represents a node in a singly linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Singly Linked List implementation."""

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        """Insert a new node at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        """Display the linked list."""
        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


if __name__ == "__main__":
    linked_list = LinkedList()

    linked_list.insert_at_beginning(10)
    linked_list.insert_at_beginning(20)
    linked_list.insert_at_beginning(30)
    linked_list.insert_at_beginning(40)

    linked_list.display()
