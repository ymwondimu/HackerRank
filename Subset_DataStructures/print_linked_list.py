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

def printLinkedList(head):
    curr = head
    while curr != None:
        print (curr.data)
        curr = curr.next

def main():

    l = SinglyLinkedList()
    l.insert_node(1)
    l.insert_node(2)
    l.insert_node(3)

    printLinkedList(l.head)

if __name__ == '__main__':
    main()