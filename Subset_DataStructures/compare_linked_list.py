#!/bin/python3

import os
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

def compare_lists(llist1, llist2):
    curr1 = llist1
    curr2 = llist2

    same = True

    while (curr1 and curr2):
        if curr1.data != curr2.data:
            same = False
            break
        curr1 = curr1.next
        curr2 = curr2.next

    if ((curr1 and not curr2) or (curr2 and not curr1)):
        same = False

    return same

def main():
    node1 = SinglyLinkedListNode(1)
    node2 = SinglyLinkedListNode(2)

    node3 = SinglyLinkedListNode(1)
    node4 = SinglyLinkedListNode(2)

    node1.next = node2
    node3.next = node4

    print (compare_lists(node1, node3))

if __name__ == "__main__":
    main()