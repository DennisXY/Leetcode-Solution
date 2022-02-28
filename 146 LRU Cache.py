# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
#
# Implement the LRUCache class:
#
# LRUCache(int capacity) Initialize the LRU cache with positive size capacity. int get(int key) Return the value of
# the key if the key exists, otherwise return -1. void put(int key, int value) Update the value of the key if the key
# exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this
# operation, evict the least recently used key.

# Example:
# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]
#
# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4


# 在双向链表的实现中，使用一个伪头部（dummy head）和伪尾部（dummy tail）标记界限，这样在添加节点和删除节点的时候就不需要检查相邻的节点是否存在

class DLinkedNode():
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None


class LRUCache:
    def add_node(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node):
        prev = node.prev
        new = node.next
        prev.next = new
        new.prev = prev

    def move_to_head(self, node):
        self.remove_node(node)
        self.add_node(node)

    def pop_tail(self):
        result = self.tail.prev
        self.remove_node(result)
        return result

    def __init__(self, capacity: int):
        self.cache = dict()
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = DLinkedNode(), DLinkedNode()

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        result = self.cache.get(key, None)
        if not result:
            return -1
        print(result)
        self.move_to_head(result)
        return result.value

    def put(self, key: int, value: int) -> None:
        result = self.cache.get(key)
        if not result:
            newNode = DLinkedNode()
            newNode.key = key
            newNode.value = value
            self.cache[key] = newNode
            self.add_node(newNode)
            self.size += 1

            if self.size > self.capacity:
                tail = self.pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            result.value = value
            self.move_to_head(result)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)