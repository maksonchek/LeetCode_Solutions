class DLLNode:
    def __init__(self, key, val):
        self.prev = None
        self.next = None
        self.val = val
        self.key = key
    
class DLL:
    def __init__(self):
        self.head = DLLNode(0,0)
        self.tail = DLLNode(0,0)
        self.size = 0
        self.head.next = self.tail
        self.tail.prev = self.head

    def __str__(self):
        node = self.head
        res = []
        while node:
            res.append(node.val)
            node = node.next
        return " ".join(map(str, res))
    
    def append(self, key, val):
        node = DLLNode(key, val)
        pr = self.tail.prev
        self.tail.prev = node
        node.prev = pr
        node.next = self.tail
        pr.next = node
        return node

    def remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        return node
        
    def pop(self):
        return self.remove(self.head.next)
        
class LRU:
    def __init__(self, capacity):
        self.size = capacity
        self.dict = {}
        self.dll = DLL()
    
    def put(self, key, val):
        if key in self.dict:
            node = self.dll[key]
            self.dll.remove(node)
        node = self.dll.append(key, val)
        self.dict[key] = node

        if len(self.dict) > self.size:
           node = self.dict.pop()
           self.dict.pop(node.key)
    
    def get(self, key):
        if key in self.dict:
            node = self.dict[key]
            val = node.val
            self.dll.remove(node)
            new_node = self.dll.append(key, val)
            self.dict[key] = new_node
            return val
        else:
            return -1
