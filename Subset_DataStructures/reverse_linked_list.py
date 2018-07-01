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

def reversePrint(head):
    curr = head
    l = []
    if curr == None:
        return
    else:
        while (curr):
            l.append(curr.data)
            curr = curr.next

    for i in range(len(l)-1, -1, -1):
        print (l[i])

def main():
    node1 = SinglyLinkedListNode(1)
    node2 = SinglyLinkedListNode(2)
    node3 = SinglyLinkedListNode(3)

    node1.next = node2
    node2.next = node3

    reversePrint(node1)

if __name__ == "__main__":
    main()