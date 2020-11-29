# https://www.youtube.com/watch?v=WwfhLC16bis\
"""
 h
[6]-->[3]-->[4]-->[2]-->[1]
"""

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
    
    def countNodes(self):
        count = 1
        current = self.head
        while current.next:
            count += 1
            current = current.next
        
        return count

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
        



# Set up nodes
node_a = Node(6)
node_b = Node(3)
node_c = Node(4)
node_d = Node(2)
node_e = Node(1)
ll = LinkedList(node_a)
ll.append(node_b) 
ll.append(node_c) 
ll.append(node_d) 
ll.append(node_e)
print(ll.countNodes())