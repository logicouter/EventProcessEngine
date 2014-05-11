#!/usr/bin/env python
#encoding=utf-8

__cycle__ = 5

from State import *

s_1 = State("s1")
s_2 = State("s2")
e_event1 = s_1 > 0
e_event2 = s_2 < 50
e_main1 = e_event1.ands(e_event2.nots())

e_main1.then().alert("halo", "wuchangwei").doPlan("planid_1")

