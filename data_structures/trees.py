# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 19:06:38 2017

@author: michael

Binary tree
"""


class binaryTree:
    def __init__(self, node_data, left=None, right=None):
        self.node_data = node_data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.node_data)


def traverse(tree):
    if tree.left:
        traverse(tree.left)
    if tree.right:
        traverse(tree.right)
    print tree.node_data


# Todo: balanced binary
# Todo: unbalanced
# Todo: heaps (max and min)