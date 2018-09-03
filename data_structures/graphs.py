# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 14:30:23 2017

@author: michael

graphs
"""


import data_structures.priority_queue as pq


def find_path(graph, start, end, path=[]):
    path = path + [start]

    if start == end:
        return path

    for node in graph[start]:
        if node not in path:
            new_path = find_path(graph, node, end, path)
            if new_path:
                return new_path


def breadth_first(graph, start):
    queue = [start]
    queued = []
    path = []
    while queue:
        vertex = queue.pop(0)
        for candidate in graph[vertex]:
            if candidate not in queued:
                queue.append(candidate)
                queued.append(candidate)
                path.append(vertex + '>' + candidate)
    return path


def depth_first(graph, start):
    stack = [start]
    parents = {start: start}
    path = []
    while stack:
        vertex = stack.pop(-1)
        for candidate in graph[vertex]:
            if candidate not in parents:
                parents[candidate] = vertex
                stack.append(candidate)
        path.append(parents[vertex] + '>' + vertex)
    return path[1:]


def prim(graph, start):
    treepath = {}
    total = 0
    queue = pq.priority_queue()
    queue.push(0, (start, start))
    while queue:
        weight, (node_start, node_end) = queue.pop()
        if node_end not in treepath:
            treepath[node_end] = node_start
            if weight:
                total += weight
            for next_node, weight in graph[node_end].items():
                queue.push(weight, (node_end, next_node))
    return treepath


def represent_tree(treepath):
    progression = list()
    for node in treepath:
        if node != treepath[node]:
            progression.append((treepath[node], node))
    return sorted(progression, key=lambda x: x[0])


if __name__ == '__main__':

    import networkx as nx
    import matplotlib.pyplot as plt

    Graph = nx.Graph()

    posts = {'A': [0.00, 0.50],
             'B': [0.25, 0.75],
             'C': [0.25, 0.25],
             'D': [0.75, 0.75],
             'E': [0.75, 0.25],
             'F': [1.00, 0.50]}

    graph = {'A': {'B': 2, 'C': 3},
             'B': {'A': 2, 'C': 2, 'D': 2},
             'C': {'A': 3, 'B': 2, 'D': 3, 'E': 2},
             'D': {'B': 2, 'C': 3, 'E': 1, 'F': 3},
             'E': {'C': 2, 'D': 1, 'F': 1},
             'F': {'D': 3, 'E': 1}}

    for node in graph:
        Graph.add_nodes_from(node)
        for edge, wght in graph[node].items():
            Graph.add_edge(node, edge, weight=wght)

    labels = nx.get_edge_attributes(Graph, 'weight')
    nx.draw(Graph, posts, with_labels=True)
    nx.draw_networkx_edge_labels(Graph, posts, edge_labels=labels)
    nx.draw_networkx(Graph, posts)
    plt.show()

    print find_path(graph, 'A', 'E')
    print breadth_first(graph, 'A')
    print depth_first(graph, 'A')
    print represent_tree(prim(graph, 'A'))
