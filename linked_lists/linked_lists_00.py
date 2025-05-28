print("This is an example of a linked list node.")

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

node1 = Node(10)

print("Node 1 data:", node1.data)      # Output: 10
print("Node 1 next:", node1.next)      # Output: None

node2 = Node(20)
node1.next = node2

print("Node 1:", node1)      # Output: 10
print("Node 2 data:", node2.data)      # Output: 10
print("Node 2 next:", node2.next)      # Output: None