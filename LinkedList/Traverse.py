# Create a Node class
class Node:

    # Constructor to create a new node
    def __init__(self, data):

        # Store the data inside the node
        self.data = data

        # Initially, the node does not point to anything
        self.next = None

    # Function to traverse and display the linked list
    def Traverse(head):

        # Start from the first node
        current = head

        # Continue until we reach the end of the linked list
        while current is not None:

            # Print the data of the current node
            print(current.data, end="->")

            # Move to the next node
            current = current.next

        # Print None to show the end of the linked list
        print("None")


# Create the first node
head = Node(10)

# Create the second node
second = Node(20)

# Create the third node
third = Node(30)


# Link the first node to the second node
head.next = second

# Link the second node to the third node
second.next = third


# Traverse the linked list
Node.Traverse(head)
