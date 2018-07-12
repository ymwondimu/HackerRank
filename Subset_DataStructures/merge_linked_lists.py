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

def mergeLists(head1, head2):
    curr1 = head1
    curr2 = head2

    if curr1 == None:
        return curr2

    if curr2 == None:
        return curr1

    h = SinglyLinkedListNode(0)
    temp = h
    while (curr1 and curr2):
        if curr1.data > curr2.data:
            temp.next = curr2
            curr2 = curr2.next
        else:
            temp.next = curr1
            curr1 = curr1.next
        temp = temp.next

    if curr1:
        temp.next = curr1

    if curr2:
        temp.next = curr2

    return h.next

def main():
    node1 = SinglyLinkedListNode(1)
    node2 = SinglyLinkedListNode(2)
    node3 = SinglyLinkedListNode(3)
    node4 = SinglyLinkedListNode(4)
    node5 = SinglyLinkedListNode(5)
    node6 = SinglyLinkedListNode(6)

    node1.next = node3
    node3.next = node5

    node2.next = node4
    node4.next = node6

    final_h = mergeLists(node1, node2)

    while (final_h):
        print (final_h.data)
        final_h = final_h.next

if __name__ == "__main__":
    main()