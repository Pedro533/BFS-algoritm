# tree.py

class Node:

    def __init__(self, data, children=None):
        self.data = data
        self.children = None
        self.parent = None
        self.cost = None
        self.set_children(children)

    def set_children(self, children):
        self.children = children
        if self.children is not None:
            for child in self.children:
                child.parent = self

    def get_children(self):
        return self.children

    def get_parent(self):
        return self.parent

    def set_parent(self, parent):
        self.parent = parent

    def get_data(self):
        return self.data

    def set_cost(self, cost):
        self.cost = cost

    def get_cost(self):
        return self.cost

    def equals(self, node):
        return self.get_data() == node.get_data()

    def in_list(self, node_list):
        for n in node_list:
            if self.equals(n):
                return True
        return False

    def __str__(self):
        return str(self.get_data())
