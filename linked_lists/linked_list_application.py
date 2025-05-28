class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)

        if(self.head == None):
            self.head = new_node
            return
        
        current = self.head

        while current.next:
            current = current.next


        current.next = new_node

    def print_list(self):
        current = self.head
    
        print("Current Linked List : ",end=" ")
        while current:
            print(current.data,end = "->")
            current = current.next

        print(None)

    def reverse_list(self):
        prev = None
        current = None

        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev
        print("Linked List Reversed...")

    def print_reverse(self):
        def print_rev(node):

            if(node is None):
                return None
            
            print_rev(node.next)
            print(node.data,end="->")

        print_rev(self.head)    
        print(None)

def start_application_linked_list():
    ll = linked_list()
    while True:
        print("1. Add Node.")
        print("2. Print List")
        print("3. Reverse List")
        print("4. Only Print Reversed List")
        print("5. Exit...")
        ch = int(input("Enter Your choice...(1-3) : "))

        match(ch):
            case 1:
                data = input("Enter your data : ")
                ll.append(data)
                print(f"{data}, added successfully in the linked list...")

            case 2:
                ll.print_list()

            case 3:
                ll.reverse_list()

            case 4:
                ll.print_reverse()

            case _:
                print("Exiting Application...")
                break

if __name__ == "__main__":
    start_application_linked_list()