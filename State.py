#!/usr/bin/env python
#encoding=utf-8

from Event import *

class State():

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def getValue(self):
        return 0 #todo

    def __le__(self, other):
        return Event(self, "<=", other)
    def __ge__(self, other):
        return Event(self, ">=", other)
    def __lt__(self, other):
        return Event(self, "<", other)
    def __gt__(self, other):
        return Event(self, ">", other)
    def __ne__(self, other):
        return Event(self, "<>", other)
    def __eq__(self, other):
        return Event(self, "==", other)



if "__main__" == __name__:
    s = State('hello')
    print s.name

