class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
    
    def delete_value(self, value):
        if self.head is None:
            return False
        
        if self.head.data == value:
            self.head = self.head.next
            return True
        
        current = self.head
        while current.next is not None:
            if current.next.data == value:
                current.next = current.next.next
                return True
            current = current.next
        return False
    
    def traverse(self):
        elements = []
        current = self.head
        while current is not None:
            elements.append(current.data)
            current = current.next
        return elements

# Test
if __name__ == "__main__":
    ll = LinkedList()
    for i in [10, 20, 30, 40]:
        ll.insert_at_end(i)
    
    print(f"List: {ll.traverse()}")
    print(f"Delete 20: {ll.delete_value(20)}")
    print(f"Final: {ll.traverse()}")