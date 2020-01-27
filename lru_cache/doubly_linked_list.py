"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        if not self.head:
            self.head = ListNode(value)
            self.length = 1
            self.tail = self.head
        else:
            temp = self.head
            self.head = ListNode(value)
            temp.prev = self.head
            self.head.next = temp
            self.length += 1

    def remove_from_head(self):
        if self.head:
            temp = self.head.next
            self.head.delete()
            self.head = temp
            self.length -= 1
            if self.head:
                self.head.prev = None
            else:
                self.tail = None

    def add_to_tail(self, value):
        if self.tail:
            self.tail.next = ListNode(value, self.tail)
            self.tail = self.tail.next
            self.length += 1
        else:
            self.add_to_head(value)

    def remove_from_tail(self):
        if self.tail:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            temp.delete()
            self.length -= 1

    def move_to_front(self, node):
        node.delete()
        self.head.prev = node
        node.next = self.head
        self.head = node

    def move_to_end(self, node):
        node.delete()
        self.tail.next = node
        node.prev = self.tail
        self.tail = self.tail.next


    def delete(self, node):
        node.delete()
        self.length -= 1

    def get_max(self):
        current = self.head
        if not current: return 0
        highest = 0
        while current:
            highest = max(current.value, highest)
            current = current.next
        return highest
