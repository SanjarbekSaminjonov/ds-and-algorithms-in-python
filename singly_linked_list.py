from typing import Optional


class Node:
    def __init__(self, data):
        self.data = data
        self.next: Optional[Node] = None


class SinglyLinkedList:
    def __init__(self):
        self._head: Optional[Node] = None

    def __iter__(self):
        curr = self._head
        while curr:
            yield curr.data
            curr = curr.next

    def __len__(self):
        count = 0
        curr = self._head
        while curr:
            curr = curr.next
            count += 1
        return count

    def __str__(self):
        return str(tuple(self))

    def append(self, data=None, new_node: Optional[Node] = None):
        if data:
            new_node = Node(data)
        elif new_node is None:
            return
        if self._head is None:
            self._head = new_node
            return
        curr = self._head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self._head
        self._head = new_node

    @staticmethod
    def insert_after_node(prev_node: Node, data):
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_by_value(self, data):
        curr = self._head
        if curr and curr.data == data:
            self._head = curr.next
            return
        prev = None
        while curr and curr.data != data:
            prev = curr
            curr = curr.next
        if curr is None:
            return
        prev.next = curr.next

    def delete_by_position(self, postion):
        curr = self._head
        if curr and postion == 0:
            self._head = curr.next
            return
        prev = None
        count = 0
        while curr and count != postion:
            prev = curr
            curr = curr.next
            count += 1
        if curr is None:
            return
        prev.next = curr.next

    def swap_nodes(self, key1, key2):
        if key1 == key2:
            return

        prev1 = None
        curr1 = self._head
        while curr1 and curr1.data != key1:
            prev1 = curr1
            curr1 = curr1.next

        prev2 = None
        curr2 = self._head
        while curr2 and curr2.data != key2:
            prev2 = curr2
            curr2 = curr2.next

        if not curr1 or not curr2:
            return

        if prev1:
            prev1.next = curr2
        else:
            self._head = curr2

        if prev2:
            prev2.next = curr1
        else:
            self._head = curr1

        curr1.next, curr2.next = curr2.next, curr1.next

    def reverse_iterative(self):
        prev = None
        curr = self._head
        while curr:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
        self._head = prev

    def reverse_recursive(self):
        def _revese(curr, prev):
            if curr is None:
                return prev
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
            return _revese(curr, prev)

        head = self._head
        self._head = _revese(head, None)


if __name__ == '__main__':
    llist = SinglyLinkedList()

    node = Node(3)

    llist.append(2)
    llist.prepend(1)
    llist.append(new_node=node)
    llist.insert_after_node(node, 4)
    llist.append(5)
    # llist.delete_by_value(3)
    # llist.delete_by_position(1)
    # llist.swap_nodes(1, 5)

    print(llist)
    llist.reverse_recursive()
    llist.reverse_iterative()
    print(llist)
