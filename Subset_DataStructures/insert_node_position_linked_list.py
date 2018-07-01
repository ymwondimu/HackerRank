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


def insertNodeAtPosition(head, data, position):
    count = 0
    if head == None:
        head = SinglyLinkedListNode(data)
    else:
        curr = head
        while (curr.next and count < position - 1):
            curr = curr.next
            count += 1
        new_node = SinglyLinkedListNode(data)
        temp = curr.next
        curr.next = new_node
        new_node.next = temp

    return head

def main():
    node1 = SinglyLinkedListNode(16)
    node2 = SinglyLinkedListNode(13)
    node3 = SinglyLinkedListNode(7)

    node1.next = node2
    node2.next = node3

    curr = insertNodeAtPosition(node1, 1, 2)

    while (curr):
        print (curr.data)
        curr = curr.next

if __name__ == "__main__":
    main()