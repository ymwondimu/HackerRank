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

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


def insertNodeAtHead(llist, data):
    if llist == None:
        llist.data = data
        return llist
    else:
        new_head = SinglyLinkedListNode(data)
        new_head.next = llist
        return new_head

def main():
    node1 = SinglyLinkedListNode(1)
    node2 = SinglyLinkedListNode(2)
    node3 = SinglyLinkedListNode(3)

    node1.next = node2
    node2.next = node3

    ll = SinglyLinkedList()
    ll.head = node1
    ll.tail=node3

    curr = insertNodeAtHead(ll.head, 4)
    while (curr):
        print (curr.data)
        curr = curr.next

if __name__ == "__main__":
    main()