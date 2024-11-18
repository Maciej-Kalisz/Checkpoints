class ListNode:
    def __init__(self, payload, next):
        self.payload = payload
        self.next = next

    def get_payload(self):
        return self.payload

    def get_next(self):
        return self.next


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        if not type(self.head) is ListNode:
            return None

        cur = self.head

        while not cur.get_next() is None:
            print(cur.get_payload())
            cur = cur.get_next()

        print(cur.get_payload())

    def add_head(self, payload):
        prev_head = self.head
        self.head = ListNode(payload, prev_head)

    def remove_head(self):
        if not self.head is None:
            self.head = self.head.get_next()

def build_list():
    node1 = ListNode("Node 1", None)
    node2 = ListNode("Node 2", node1)
    node3 = ListNode("Node 3", node2)

    return node3

def print_list(list_node: ListNode):
    if not type(list_node) is ListNode:
        return None

    cur = list_node

    while not cur.get_next() is None:
        print(cur.get_payload())
        cur = cur.get_next()

    print(cur.get_payload())

