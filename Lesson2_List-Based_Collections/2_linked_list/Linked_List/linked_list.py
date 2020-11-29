# https://classroom.udacity.com/courses/ud513/lessons/7117335401/concepts/78875247320923
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        # A pointer that start at the current head node
        current = self.head
        
        if self.head:
            # Walk through the linked list
            # until the end of it
            # (there's something after it).
            while current.next:
                current = current.next # Keep moving.
            # At the end, create new node.
            current.next = new_element
        
        # If no current head assigned,
        else:
            # create new head
            self.head = new_element

    def get_position(self, position):
        current_pos = 1
        current = self.head

        if position < 1:
            return None
        while current and current_pos <= position:
            if current_pos == position:
                return current
            current = current.next
            current_pos += 1
        return None

    def insert(self, new_element, position):
        current_pos = 1
        current = self.head

        if position > 1:
            while current and current_pos < position:
                if current_pos == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                current_pos += 1
        elif position == 1:
            new_element.next = self.head
            self.head = new_element
    
    # From the HackerRank's video: Data Structures: Linked Lists
    # https://www.youtube.com/watch?v=njTh_OwMljA
    def delete(self, value):
        # Special cases, if the node to be deleted
        # is the head node
        if self.head.value == value:
            self.head = self.head.next
            return

        # Set pointer to current head that 
        # walk through the linked list
        current = self.head

        # Walk through as long as we're 
        # not at the last element
        while current.next:
            # If the next value is one to be deleted
            if current.next.value == value:
                # cut out that next value
                current.next = current.next.next
            
            # Guaranteed cases, move on to the next element
            current = current.next


    # From the audacity course's solution
    # https://classroom.udacity.com/courses/ud513/lessons/7117335401/concepts/78875247320923
    def delete2(self, value):
        current = self.head
        previous = None

        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next

    def printList(self):
        current = self.head
        count = 1
        while current:
            print(current.value, end=" ")
            current = current.next

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print(ll.head.next.next.value)
# Should also print 3
print(ll.get_position(3).value)

# Test insert
ll.insert(e4,3)
# Should print 4 now
print(ll.get_position(3).value)

# Test delete
ll.delete(1)
# Should print 2 now
print(ll.get_position(1).value)
# Should print 4 now
print(ll.get_position(2).value)
# Should print 3 now
print(ll.get_position(3).value)

# Should print 2 4 3 now
ll.printList()