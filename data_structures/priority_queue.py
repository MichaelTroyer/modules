# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 17:55:46 2017

@author: michael

priority queue
"""

from heapq import heapify, heappop, heappush


class priority_queue():

    def __init__(self):
        self.queue = list()
        heapify(self.queue)
        self.index = dict()

    def push(self, priority, label):
        if label in self.index:
            self.queue = [(w, l) for w, l in self.queue if l != label]
            heapify(self.queue)
        heappush(self.queue, (priority, label))
        self.index[label] = priority

    def pop(self):
        if self.queue:
            return heappop(self.queue)

    def __contains__(self, label):
        return label in self.index

    def __len__(self):
        return len(self.queue)

