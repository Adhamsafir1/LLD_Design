# OOP-based transactional key-value store without using built-in list, dict, set
# Only strings and integers are allowed

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedMap:
    def __init__(self):
        self.head = None

    def put(self, key, value):
        curr = self.head
        while curr:
            if curr.key == key:
                curr.value = value
                return
            curr = curr.next
        new_node = Node(key, value)
        new_node.next = self.head
        self.head = new_node

    def get(self, key):
        curr = self.head
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        return None

    def remove(self, key):
        curr = self.head
        prev = None
        while curr:
            if curr.key == key:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                return
            prev = curr
            curr = curr.next

    def count(self, value):
        curr = self.head
        count = 0
        while curr:
            if curr.value == value:
                count += 1
            curr = curr.next
        return count

    def clone(self):
        new_map = LinkedMap()
        nodes = []
        curr = self.head
        while curr:
            # We'll use a simple array replacement using string concatenation
            key_val_pair = (curr.key, curr.value)
            nodes.append(key_val_pair)
            curr = curr.next
        for i in range(len(nodes) - 1, -1, -1):  # reverse order to maintain insertion
            key, value = nodes[i]
            new_map.put(key, value)
        return new_map

class StackNode:
    def __init__(self, map_snapshot):
        self.map_snapshot = map_snapshot
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, map_snapshot):
        node = StackNode(map_snapshot)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top is None:
            return None
        popped = self.top
        self.top = self.top.next
        return popped.map_snapshot

    def is_empty(self):
        return self.top is None

class KeyValueStore:
    def __init__(self):
        self.db = LinkedMap()
        self.tx_stack = Stack()

    def set(self, key, value):
        self.db.put(key, value)

    def get(self, key):
        val = self.db.get(key)
        return val if val is not None else "null"

    def unset(self, key):
        self.db.remove(key)

    def count(self, value):
        return self.db.count(value) or "null"

    def begin(self):
        self.tx_stack.push(self.db.clone())

    def rollback(self):
        if self.tx_stack.is_empty():
            print("NO TRANSACTION")
        else:
            self.db = self.tx_stack.pop()

    def commit(self):
        if self.tx_stack.is_empty():
            print("NO TRANSACTION")
        else:
            self.tx_stack = Stack()  # reset stack

# ------------------ Console Interface ------------------
def run_console():
    kvs = KeyValueStore()
    while True:
        try:
            cmd = input("=> ").strip().split()
            if not cmd:
                continue
            op = cmd[0].upper()

            if op == 'END':
                break
            elif op == 'SET' and len(cmd) == 3:
                kvs.set(cmd[1], cmd[2])
            elif op == 'GET' and len(cmd) == 2:
                print(kvs.get(cmd[1]))
            elif op == 'UNSET' and len(cmd) == 2:
                kvs.unset(cmd[1])
            elif op == 'COUNT' and len(cmd) == 2:
                print(kvs.count(cmd[1]))
            elif op == 'BEGIN':
                kvs.begin()
            elif op == 'ROLLBACK':
                kvs.rollback()
            elif op == 'COMMIT':
                kvs.commit()
            else:
                print("INVALID COMMAND")
        except Exception as e:
            print("ERROR:", str(e))

# Uncomment below to run interactively:
# run_console()
