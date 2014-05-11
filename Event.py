#!/usr/bin/env python
#encoding=utf-8

from Action import *

class Event():
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
        self.action = None
    def evaluate(self):
        if "==" == self.op:
            return self.left.getValue() == self.right
        elif ">" == self.op:
            return self.left.getValue() > self.right
        elif "<" == self.op:
            return self.left.getValue() < self.right
        elif ">=" == self.op:
            return self.left.getValue() >= self.right
        elif "<=" == self.op:
            return self.left.getValue() <= self.right
        elif "<>" == self.op:
            return self.left.getValue() <> self.right
        if "and" == self.op:
            return self.left.evaluate() and self.right.evaluate()
        elif "or" == self.op:
            return self.left.evaluate() or self.right.evaluate()
        elif "not" == self.op:
            return not self.right.evaluate()
    def ands(self, other):
        e = Event(self, "and", other)
        return e
    def ors(self, other):
        e = Event(self, "or", other)
        return e
    def nots(self):
        e = Event(self, "not", self)
        return e
    def then(self):
        self.action = Action("BEGIN", ())
        return self.action

if "__main__" == __name__:
    pass
