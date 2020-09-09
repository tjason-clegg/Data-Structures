"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        if self.head is None and self.tail is None:
            self.length += 1
            self.head = ListNode(value)
            self.tail = self.head
        else:
            self.length += 1
            self.head.insert_before(value)
            self.head = self.head.prev

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        value = self.head.value

        if self.head is None and self.tail is None:
            return None
        elif self.head == self.tail:
            self.length -= 1
            self.head = None
            self.tail = None
        else:
            self.length -= 1
            self.head.delete()

        return value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        if self.head is None and self.tail is None:
            self.length += 1
            self.head = ListNode(value)
            self.tail = self.head
        else:
            self.length += 1
            self.tail.insert_after(value)
            self.tail = self.tail.next

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        value = self.tail.value

        if self.head is None and self.tail is None:
            return None
        elif self.head == self.tail:
            self.length -= 1
            self.head = None
            self.tail = None
        else:
            self.length -= 1
            self.tail.delete()

        return value

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        if node is self.head:
            return
        elif node is self.tail:
            self.tail = node.prev
        node.delete()
        self.head.prev = node
        node.prev = None
        node.next = self.head
        self.head = node

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        if node is self.tail:
            return
        elif node is self.head:
            self.head = node.next
        node.delete()
        self.tail.next = node
        node.prev = self.tail
        node.next = None
        self.tail = node

        return self.tail

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        if not self.head and not self.tail:
            return

        self.length -= 1
        if self.head is self.tail:
            self.head = None
            self.tail = None
        elif self.head is node:
            self.head = node.next
            node.delete()
        elif self.tail is node:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        if not self.head:
            return None

        max_value = self.head.value
        current = self.head

        while current is not None:
            if current.value > max_value:
                max_value = current.value

            current = current.next
        return max_value
