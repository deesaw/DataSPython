# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 12:56:20 2021

@author: deesaw
"""


class DoublyLinkedListNode(object):
    
    def __init__(self,value):
        
        self.value = value
        self.next_node = None
        self.prev_node = None
        
a = DoublyLinkedListNode(1)
b = DoublyLinkedListNode(2)
c = DoublyLinkedListNode(3)

# Setting b after a
b.prev_node = a
a.next_node = b

b.next_node = c
c.prev_node = b