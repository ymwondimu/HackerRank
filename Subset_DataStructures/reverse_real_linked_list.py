#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def reverse(head):
    if head == None:
        return head

    prev = None
    curr = head
    next = None

    while (curr):
        next = curr.next
        curr.next = prev

        prev = curr
        curr = next
    head = prev

    return head



def main():
    node1 = SinglyLinkedListNode(1)
    node2 = SinglyLinkedListNode(2)
    node3 = SinglyLinkedListNode(3)

    node1.next = node2
    node2.next = node3

    curr = reverse(node1)

    while (curr):
        print (curr.data)
        curr = curr.next


if __name__ == "__main__":
    main()