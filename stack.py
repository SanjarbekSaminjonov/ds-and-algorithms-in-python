class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def is_empty(self):
        return self._items == []

    def peek(self):
        if not self.is_empty():
            return self._items[-1]

    def get_stack(self):
        return self._items
