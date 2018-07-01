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


def deleteNode(head, position):
    count = 1
    curr = head

    if (curr.next == None):
        curr = None
    else:
        if position == 0:
            head = curr.next
            return head
        prev = curr
        curr = curr.next
        while (curr and count < position):
            prev = prev.next
            curr = curr.next
            count += 1

        prev.next = curr.next
        curr.next = None

    return head

def main():
    node1 = SinglyLinkedListNode(11)
    node2 = SinglyLinkedListNode(12)
    node3 = SinglyLinkedListNode(8)
    node4 = SinglyLinkedListNode(18)
    node5 = SinglyLinkedListNode(16)
    node6 = SinglyLinkedListNode(5)
    node7 = SinglyLinkedListNode(18)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7

    head = node1
    curr = deleteNode(head, 0)

    while (curr):
        print (curr.data)
        curr = curr.next

if __name__ == "__main__":
    main()