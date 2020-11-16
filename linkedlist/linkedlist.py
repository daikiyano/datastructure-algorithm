from typing import Any
class Node:
    def __init__(self,data,next_node):
        self.data = data
        self.next = next_node


class LinkedList:
    def __init__(self,head):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_none.next = new_node

    def insert



