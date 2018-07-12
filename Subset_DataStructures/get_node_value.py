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

def getNode(head, positionFromTail):
    curr = head
    temp = head

    for i in range(positionFromTail):
        temp = temp.next

    while (temp.next):
        curr = curr.next
        temp = temp.next

    return curr.data

def main():
    node1 = SinglyLinkedListNode(1)
    node2 = SinglyLinkedListNode(2)
    node3 = SinglyLinkedListNode(3)

    node1.next = node2
    node2.next = node3

    print (getNode(node1, 2))

if __name__ == "__main__":
    main()
