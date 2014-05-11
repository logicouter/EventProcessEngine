#!/usr/bin/env python

import code
import ast
import sched
import time

schedule = sched.scheduler(time.time, time.sleep)

def alert(receivers, content):
    print "\"%s\" -> %s" % (content, receivers)

# todo
def doPlan(planId):
    print "do plan(%d)" % planId

rules = []

def addRule(rule):
    # execute script
    aRule = () # for grammar check
    exec("import %s as aRule" % rule)
    # interpreter.runsource("doRule()")
    cycle = getattr(aRule, "__cycle__")
    for key in dir(aRule):
        if (key.startswith('e_')):
            eventObject = getattr(aRule, key)
            if None == eventObject: continue
            global rules
            rules.append((cycle, eventObject))

if "__main__" == __name__:
    addRule("aRule")
    print rules



