from Doubly_Linked_List import DoublyLinkedList

class LRUCache:
    def __init__(self, capacity: int):
        self.size = capacity
        self.list = DoublyLinkedList()
        self.h = {}

    def get(self, key: int) -> int:
        if key in self.h:
            node = self.h[key]
            self.list.remove(node)
            self.h[key] = self.list.append(key, node.val)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.h:
            self.list.remove(self.h[key])

        node = self.list.append(key, value)
        self.h[key] = node

        if self.list.size > self.size:
            d = self.list.pop()
            del self.h[d.key]
    