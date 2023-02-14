from typing import Optional


class Node:
    def __init__(self, data):
        self.data = data
        self.next: Optional[Node] = None


class SinglyLinkedList:
    def __init__(self):
        self.head: Optional[Node] = None

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr.data
            curr = curr.next

    def __len__(self):
        count = 0
        curr = self.head
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
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    @staticmethod
    def insert_after_node(prev_node: Node, data):
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_by_value(self, data):
        curr = self.head
        if curr and curr.data == data:
            self.head = curr.next
            return
        prev = None
        while curr and curr.data != data:
            prev = curr
            curr = curr.next
        if curr is None:
            return
        prev.next = curr.next

    def delete_by_position(self, postion):
        curr = self.head
        if curr and postion == 0:
            self.head = curr.next
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


if __name__ == '__main__':
    llist = SinglyLinkedList()

    node = Node(3)

    llist.append(2)
    llist.prepend(1)
    llist.append(new_node=node)
    llist.insert_after_node(node, 4)
    llist.delete_by_value(3)
    llist.delete_by_position(1)

    print(len(llist))
    print(*llist)
