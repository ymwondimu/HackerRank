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

def removeDuplicates(head):
    curr = head.next
    prev = head


    return head

def main():
    node1 = SinglyLinkedListNode(1)
    node2 = SinglyLinkedListNode(2)
    node3 = SinglyLinkedListNode(3)
    node4 = SinglyLinkedListNode(3)
    node5 = SinglyLinkedListNode(4)
    node6 = SinglyLinkedListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6

    h = removeDuplicates(node1)

    while (h):
        print (h.data)
        h = h.next

if __name__ == "__main__":
    main()

