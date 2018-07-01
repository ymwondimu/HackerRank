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

# Complete the insertNodeAtTail function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtTail(head, data):
    curr = head
    if head == None:
        head.data = data
    else:
        while (curr.next):
            curr = curr.next
        curr.next = SinglyLinkedListNode(data)
    return head

def main():
    node1 = SinglyLinkedListNode(1)
    node2 = SinglyLinkedListNode(2)
    node3 = SinglyLinkedListNode(3)

    node1.next = node2
    node2.next = node3

    l = SinglyLinkedList()
    l.head = node1

    insertNodeAtTail(l.head, 4)

    curr = l.head
    while (curr):
        print (curr.data)
        curr = curr.next

if __name__ == "__main__":
    main()